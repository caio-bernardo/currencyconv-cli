# Currency Converter CLI

## A Command Line Interface made with Python that convertes different currencies from all the world.

This is a small project using [Typer](https://github.com/tiangolo/typer) focusing in learning. The application takes an argument and two optional parameters, the base currency and the target currency, the default is 'BRL' (Brazilian Real) and 'USD' (US Dolar) in that order. After that, the program makes a request to [ExchangeRate-API](https://www.exchangerate-api.com/), which responds with the calculated conversion.

# Table of Contents

[Know Issues](#know-isssues) - [Instalation](#instalation) - [Making changes](#making-changes) - [Contributing](#contributing) - [License](#license)

## Know Issues

- ExchangeRate-API imposes a monthly quota of 1500 requests, limiting the usage of the application. Unfortanately, this can't be fixed.
- It is needed to use the command "main" after the application name. This is _not intended_ and will be fixed soon.
- In the case where the program crashes it exposes local variables.

## Instalation

To install you have to clone this repository

## Making changes

If you want to make changes to this project you need to clone this repository and have poetry installed.
After cloning, go to the project's directory and initialize the poetry, don't forget to install the dependencies.

```bash
poetry init
poetry install
```

To run the project use `poetry run python currenapp/main.py` or start the poetry shell to skip these commands.

```zsh
poetry shell
python currenapp/main.py
```

## Contributing

Issues and Pull Request are welcomed. If you want to make suggestions, ask or discuss anything, open a issue.

## License

[MIT](./LICENSE.md)
