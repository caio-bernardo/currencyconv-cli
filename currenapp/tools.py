"""
Helper functions

Functions that shouldn't be on main.py or ui.py but are involved with them.
"""
import re
import requests
import os
import typer


def get_apidata(amount: float, base: str, target: str) -> dict | None:
    """Request to the Exchangerate-API"""
    API_KEY = os.environ.get("EXCHANGERATE_KEY")
    if not API_KEY:
        return
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base}/{target}/{amount}"
    response = requests.get(url)

    return response.json()


def is_validargs(base: str, target: str) -> bool:
    """Checks if the params are valid currency code.

    INCOMPLETE FEATURE! Only testing if they are 3 uppercase ASCII letters.
    """
    # TODO check if the currency code is valid and supported
    pattern = r"^[A-Z]{3}$"
    return re.match(pattern, base) and re.match(pattern, target)
