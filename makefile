all: format check tests

format:
	ruff --fix src/ test/

check-format:
	ruff src/ test/

mypy:
	mypy src/ test/

check: check-format mypy

tests:
	pytest