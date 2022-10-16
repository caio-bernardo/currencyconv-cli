import currenapp.ui as ui
from rich.console import Console
import pytest


@pytest.fixture
def console():
    return Console()


@pytest.fixture
def mock_data():
    return {
        "amount": 1.0,
        "base_code": "abc",
        "target_code": "def",
        "conversion_result": 0.1,
        "conversion_rate": 0.8,
        "time_next_update_utc": "MON, 18 JAN 2020 2:00:00",
    }


# NOT A TEST. EASY WAY TO SHOW UI AND NOT CLOG THE ui.py
def show_full_ui():
    data = {
        "amount": 1.0,
        "base_code": "abc",
        "target_code": "def",
        "conversion_result": 0.1,
        "conversion_rate": 0.8,
        "time_next_update_utc": "MON, 18 JAN 2020 2:00:00",
    }

    Console().print(ui.success_output(data))


def show_full_error_ui():
    data = {"result": "error", "error-type": "malformed-request"}
    Console().print(ui.error_output(data))


def test_success_output(capsys, console, mock_data):

    console.print(ui.success_output(mock_data))
    captured = capsys.readouterr()

    for data in mock_data.values():
        assert str(data) in captured.out


def test_remove_trailing_zeros_from_nums(capsys, console, mock_data):
    mock_data["conversion_result"] = 0.1000
    console.print(ui.success_output(mock_data))
    captured = capsys.readouterr()

    assert "0.1" in captured.out


def test_convert_utc_time_to_local_time():
    pass


def test_error_output(capsys, console):
    mock_data = {"error-type": "malformed-request"}

    console.print(ui.error_output(mock_data))
    captured = capsys.readouterr()

    assert "Conversion Failed" in captured.out
    assert mock_data["error-type"] in captured.out


if __name__ == "__main__":
    show_full_ui()
    show_full_error_ui()
