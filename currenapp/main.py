import re
import typer
import requests
import os
from dotenv import load_dotenv
from rich import print as rprint
from rich.console import Console

console = Console()


load_dotenv()
# Disable local variables on error logs on production
app = typer.Typer(
    pretty_exceptions_show_locals=os.getenv("SHOW_LOCALS", False))


def get_apidata(amount: float, base: str, target: str) -> dict:
    API_KEY = os.getenv("API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base}/{target}/{amount}"

    response = requests.get(url)
    return response.json()


def is_validargs(base: str, target: str) -> bool:
    # check for valid currency code
    # Note: Only checking if the input is on the right format (3 uppercase letters from A-Z)
    pattern = r"^[A-Z]{3}$"
    return re.match(pattern, base) and re.match(pattern, target)


@app.command()
def main(base: str = "USD", target: str = "BRL"):
    if not is_validargs(base, target):
        rprint(
            f"[bold red]Invalid currency codes![/bold red] Received: {base}, {target}. Check your inputs.")
        raise typer.Abort()

    try:
        amount = float(typer.prompt("Value to convert $"))
    except ValueError:
        rprint("[bold red]Expected a number![/bold red].")
        raise typer.Abort()

    with console.status("Making the conversion", spinner="bouncingBall"):
        data = get_apidata(amount, base, target)

    result = data.get("result")
    match result:
        case "success":
            rprint("Conversion")
            rprint(
                f"${base}: {amount} = ${target}: {data.get('conversion_result')}")
            rprint(f"Conversion rate: {data.get('conversion_rate')}")
            rprint(f"Next Update in {data.get('time_next_update_utc')}")

        case "error":
            rprint("Something went wrong...")
            print(f"Error Type: {data.get('error_type')}")
            typer.Exit(code=1)


if __name__ == "__main__":
    app()
