import typer
import os
from dotenv import load_dotenv
from rich.console import Console


import currenapp.ui as ui
import currenapp.tools as tools

console = Console()


load_dotenv()
# Disable local variables on error logs for production
app = typer.Typer(pretty_exceptions_show_locals=bool(os.getenv("SHOW_LOCALS")))


@app.command()
def main(base: str = "USD", target: str = "BRL"):
    """Converts values from and to different currencies

    Receives inputs of currency codes and ask for an amount to convert.
    using an API request, converts and prints the results.
    """
    if not tools.is_validargs(base, target):
        console.print(
            f"[bold red]Invalid currency codes![/bold red] Received: {base}, {target}. Check your inputs."
        )
        raise typer.Abort()

    # Prompting
    try:
        amount = float(typer.prompt("Value to convert $"))
    except ValueError:
        console.print("[bold red]Expected a number![/bold red].")
        raise typer.Abort()

    with console.status("Making the conversion", spinner="bouncingBall"):
        data = tools.get_apidata(amount, base, target)

    match data.get("result"):
        case "success":
            # adds amount to the api response for pratical reasons.
            data["amount"] = amount
            console.print(ui.success_output(data))
        case "error":
            console.print(ui.error_output(data))
            typer.Exit(code=1)


if __name__ == "__main__":
    app()
