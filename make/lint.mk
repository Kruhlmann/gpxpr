fix:
	black --safe --quiet src/ tests/
	isort src/ tests/

lint: install-dev
	black --check -q src/ tests/
	flake8 src/ tests/
	mypy src/ tests/
