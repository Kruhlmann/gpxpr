fix:
	black --safe --quiet src/ tests/
	isort src/ tests/

lint:
	black --check -q src/ tests/
	flake8 src/ tests/
	mypy src/ tests/
