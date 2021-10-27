install: setup.cfg ${VERSION_FILE}
	pip install -e .

install-dev: install-tests setup.cfg ${VERSION_FILE}
	pip install -e '.[dev]'

install-tests: setup.cfg ${VERSION_FILE}
	pip install -e '.[tests]'

install-all: install-dev install-tests install setup.cfg ${VERSION_FILE}
