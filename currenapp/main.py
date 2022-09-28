import typer
import requests
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()
app = typer.Typer()


@app.callback()
def callback():
    # some Documentation
    """
    Curruncy Conversion

    Converts a passed VALUE from --BASE to --TARGET currency using  the exchangerate-api.
    """


@app.command()
def main(value: float, base: str = "USD", target: str = "BRL"):
    if len(base) != 3 or len(target) != 3:
        print(
            f"[bold red]Invalid currency codes![/bold red] Received: {base}, {target}. Check your inputs.")
        raise typer.Abort()

    API_KEY = os.getenv("API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base}/{target}/{value}"

    response = requests.get(url)
    data: dict = response.json()

    result = data.get("result")
    match result:
        case "success":
            print("Conversion")
            print(f"${base}: {value} = ${target}: {data.get('conversion_result')}")
            print(f"Conversion rate: {data.get('conversion_rate')}")
            print(f"Next Update in {data.get('time_next_update_utc')}")

        case "error":
            print("Something went wrong")
            print(f"Error Type: {data.get('error_type')}")
            typer.Exit(code=1)


if __name__ == "__main__":
    app()
