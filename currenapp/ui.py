import rich
from rich.panel import Panel
from rich.table import Table
from rich.console import Console


def success_output(data: dict) -> Panel:
    title = "Conversion Completed"
    subtitle = f"Last Update: {data['time_last_update_utc']}"

    grid = Table.grid(expand=True)
    grid.add_column(justify='right')
    grid.add_column(justify='center')
    grid.add_column(justify='left')

    grid.add_row('FROM', '-'*10, 'INTO')
    grid.add_row(data['base_code'], '', data['target_code'])
    grid.add_row(f'{data["base"]:2f}', f'{data["conversion_result"]:2f}')
    grid.add_row(None, f"Conversion rate: {data['conversion_rate']}", None)

    return Panel(grid, title=title, subtitle=subtitle)


def error_output(data: dict) -> Panel:
    title = "Conversion Failed"

    return Panel(f"Error: {data['error_type']}", title=title)
