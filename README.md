# Telegram Bot
Telegram bot to manage sources.

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# core based on:
  - Python 3.10 version
  - Pyrogram 2.0 version

# Technologies are used:
  - SQLAlchemy
  - validators

# How to run it?

### run with docker:

edit env configuration in env directory and then:

    docker compose up --build

or

### install dependencies:

create virtualenv

    python3.10 -m venv venv

active virtualenv

    source venv/bin/activate

install packages

    pip install -r requirements/local.txt

    pip install -r requirements/production.txt

run server

    sh scripts/run.sh
