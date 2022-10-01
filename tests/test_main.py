from currenapp.main import app, is_validargs
from typer.testing import CliRunner
import pytest
from httmock import urlmatch, HTTMock
import json


runner = CliRunner()


@pytest.fixture
def cmd_args():
    return ["--base", "USD", "--target", "BRL"]


def test_args_validation_wth_wrong_inputs():
    mock_args = (("1b", "_BR"), ("abcd", "-az"), ("142", "!aW"))
    for margs in mock_args:
        assert not is_validargs(*margs)


def test_args_validation_wth_right_inputs():
    mock_args = ("ABC", "DEF")
    assert is_validargs(*mock_args)


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


@urlmatch(netloc=r"(.*\.)?exchangerate-api")
def api_mock(url, request):
    return json.dumps({"result": "sucess"})
