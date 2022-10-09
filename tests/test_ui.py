import currenapp.ui as ui
from rich.console import Console
import pytest


@pytest.fixture
def console():
    return Console()


def test_success_output(capsys, console):
    mock_data = {
        "base": 1.0,
        "base_code": "abc",
        "target_code": "def",
        "conversion_result":  0.1,
        "conversion_rate": 0.8,
        "time_last_update_utc": "MON, 18 JAN 2020 2:00:00"
    }

    console.print(ui.success_output(mock_data))
    captured = capsys.readouterr()

    for data in mock_data.values():
        assert str(data) in captured.out


def test_error_output(capsys, console):
    mock_data = {
        "error_type": "unknow"
    }

    console.print(ui.error_output(mock_data))
    captured = capsys.readouterr()

    assert "Conversion Failed" in captured.out
    assert mock_data["error_type"] in captured.out
