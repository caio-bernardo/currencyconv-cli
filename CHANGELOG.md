# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- [ ] Full Documentation
- [ ] Beautiful CLI
- [ ] Offering PiPy installation

## 0.2.0 — 2022-10-01

### Added

- Tests on tests/test_main.py
- Status bar for the conversion request
- Improve validation of currency code.
- HTTMock as a dependencie for tests.

### Modified

- Value to be converted comes from a prompt question instead of a argument.
- Move validation and request to the API to their own functions.
- Validation of currency code now uses RegEx.

### Fixed

- No more calling "main" as a command to use the application.

### Removed

- Callback with documetation, since it was causing the problem with "main".

### Security

- Hide local variables on production.

## 0.1.0 — 2022-09-28

### Added

- "main" command makes requests to Exchangerate API to convert values.
- Basic error handling of OPTIONS and the API response.
