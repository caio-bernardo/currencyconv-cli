from currenapp.main import app
from typer.testing import CliRunner
from httmock import HTTMock, all_requests
import pytest


runner = CliRunner()


@pytest.fixture
def cmd_args():
    return ["--base", "USD", "--target", "BRL"]


def test_cli_error_wrong_currency_values(cmd_args):
    cmd_args[1] = "ER"
    cmd_args[3] = "ROR"
    result = runner.invoke(app, cmd_args, input="30\n")

    assert result.exit_code == 1
    assert "Invalid" in result.stdout
    assert "ER" in result.stdout
    assert "RO" in result.stdout


def test_input_not_a_number(cmd_args):
    result = runner.invoke(app, cmd_args, input="null\n")

    assert result.exit_code == 1
    assert "Expected a number" in result.stdout


@all_requests
def api_mock(url, request):
    return {
        "status_code": 200,
        "content": {
            "result": "success",
            "documentation": "https://www.exchangerate-api.com/docs",
            "terms_of_use": "https://www.exchangerate-api.com/terms",
            "time_last_update_unix": 1585267200,
            "time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
            "time_next_update_unix": 1585270800,
            "time_next_update_utc": "Sat, 28 Mar 2020 01:00:00 +0000",
            "base_code": "EUR",
            "target_code": "GBP",
            "conversion_rate": 0.8,
            "conversion_result": 5.80,
        },
    }


# FULL test of the application
def main():
    with HTTMock(api_mock):
        app()


if __name__ == "__main__":
    main()
