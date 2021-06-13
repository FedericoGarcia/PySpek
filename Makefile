setup:
	poetry install

run:
	poetry run python pyspek/main.py

lint:
	poetry run python -m flake8
	poetry run python -m pylint
	poetry run python -m mypy

test:
	poetry run python -m pytest -v tests/

prepare:
	make lint
	make test

update:
	poetry update