import currenapp.tools as tools
from httmock import all_requests, urlmatch, HTTMock
import json


def test_args_validation_wth_wrong_inputs():
    mock_args = (("1b", "_BR"), ("abcd", "-az"), ("142", "!aW"))
    for margs in mock_args:
        assert not tools.is_validargs(*margs)


def test_args_validation_wth_right_inputs():
    mock_args = ("ABC", "DEF")
    assert tools.is_validargs(*mock_args)


@all_requests
def api_mock_ok(url, request):
    data = {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "time_last_update_unix": 1585267200,
        "time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
        "time_next_update_unix": 1585270800,
        "time_next_update_utc": "Sat, 28 Mar 2020 01:00:00 +0000",
        "base_code": "EUR",
        "target_code": "GBP",
        "conversion_rate": 0.8412,
        "conversion_result": 5.8884,
    }
    return {"status_code": 200, "content": json.dumps(data)}


def test_getapi_ok_request():
    with HTTMock(api_mock_ok):
        data = tools.get_apidata(4.64, "EUR", "GBP")
        assert data == {
            "result": "success",
            "documentation": "https://www.exchangerate-api.com/docs",
            "terms_of_use": "https://www.exchangerate-api.com/terms",
            "time_last_update_unix": 1585267200,
            "time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
            "time_next_update_unix": 1585270800,
            "time_next_update_utc": "Sat, 28 Mar 2020 01:00:00 +0000",
            "base_code": "EUR",
            "target_code": "GBP",
            "conversion_rate": 0.8412,
            "conversion_result": 5.8884,
        }


@urlmatch(netloc=r"(.*\.)?exchangerate-api")
def api_mock_bad(url, request):
    data = {"result": "error", "error_type": "malformed-request"}

    return {"status_code": 400, "content": json.dumps(data)}


def test_getapi_bad_request():
    with HTTMock(api_mock_bad):
        data = tools.get_apidata(4.64, "EUR", "GBP")

    assert data == {"result": "error", "error_type": "malformed-request"}
