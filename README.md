# BizPlanner

BizPlanner is a simple command-line tool for planning and managing business budgets and resources. It allows you to create businesses, assign resources to them, categorize resources, and view business details, all stored in a local SQLite database.

## Features

- Add businesses with budgets and descriptions
- Add resources to businesses, assign budgets, descriptions, and categories
- Categorize resources (e.g., marketing, staffing)
- View all businesses and their resources

## Requirements

- Python 3.8 or 3.10
- [SQLAlchemy](https://www.sqlalchemy.org/)

All dependencies are managed via [Pipfile](Pipfile).

## Installation

1. Clone the repository:
    ```sh
    git clone <your-repo-url>
    cd bizplanner
    ```

2. Install dependencies:
    ```sh
    pip install pipenv
    pipenv install
    ```

## Usage

Run the CLI tool:

```sh
pipenv run python cli.py
```

Follow the on-screen prompts to add businesses, resources, and view your data.

## Project Structure

- [`cli.py`](cli.py): Command-line interface logic
- [`database.py`](database.py): Database setup (SQLAlchemy engine, session, base)
- [`models.py`](models.py): SQLAlchemy ORM models for Business, Resource, Category
- [`utils.py`](utils.py): Utility functions for input and output
- [`main.py`](main.py): (Currently empty, reserved for future use)
- [`Pipfile`](Pipfile), [`Pipfile.lock`](Pipfile.lock): Dependency management

## License

MIT License