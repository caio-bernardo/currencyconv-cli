from rich.panel import Panel
from rich.table import Table

# Details for different error types
error_details = {
    "unsupported-code": "Currency code invalid or unsupported. Check your currency inputs",
    "malformed-request": "Invalid request",
    "invalid-key": "Your API key is invalid",
    "inactive-account": "Your account is inactive. Go exchangerate-api to activate",
    "quota-reached": "Your account has reached the limit of requests of your plan. ",
}


def success_output(data: dict) -> Panel:
    """Formats the data for 200 OK responses"""

    title = "Conversion Completed"
    subtitle = f"Next Update: {data['time_next_update_utc']}"

    grid = Table.grid(expand=True)
    grid.add_column(justify="center", style="bold green")

    grid.add_row(
        f"[white]{data['base_code']}[/white] [blue]into[/blue] [white]{data['target_code']}[/white]"
    )
    grid.add_row(f"[blue]RATE:[/blue] {data['conversion_rate'] :.2f}")
    grid.add_row(f"[blue]BASE:[/blue] ${data['amount'] :.2f}")
    grid.add_row(f"[blue]RESULT:[/blue] ${data['conversion_result']:.2f}")

    return Panel(grid, title=title, subtitle=subtitle, style="#D4AF37")


def error_output(data: dict) -> Panel:
    """Formats the data for ERROR responses"""
    error_type = data["error-type"]

    title = "Conversion Failed"

    grid = Table.grid(expand=True)
    grid.add_column(justify="center")
    grid.add_row(f"AN ERROR HAS OCCURRED: {error_type}")
    grid.add_row(f"DETAILS: {error_details[error_type]} ")
    return Panel(grid, title=title, style="bold deep_pink2")
