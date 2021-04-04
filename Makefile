PROJ_BASE=$(shell pwd)
PYTHONVER=python3.8
PYTHONVENV=$(PROJ_BASE)/venv
VENVPYTHON=$(PYTHONVENV)/bin/$(PYTHONVER)
PYTEST=$(PYTHONVENV)/bin/pytest

.PHONY: install
install: bootstrap
	@echo "Installing pyopenweather"
	$(VENVPYTHON) setup.py install
	@echo "\nYou may want to activate the virtual environmnent with 'source venv/bin/activate'\n"

.PHONY: develop
develop: bootstrap
	@echo "Installing pyopenweather, with editible modules ('python setup.py develop')"
	$(VENVPYTHON) setup.py develop
	@echo "\nYou may want to activate the virtual environmnent with 'source venv/bin/activate'\n"


.PHONY: bootstrap
bootstrap:
	@echo "Creating virtual environment 'venv' for development."
	python3 -m virtualenv -p $(PYTHONVER) venv
	@echo "Installing python modules from requirements.txt"
	$(VENVPYTHON) -m pip install -r requirements.txt


.PHONY: clean_build
clean_build:
	@echo "Removing build artifacts"
	rm -rf $(PROJ_BASE)/build
	rm -rf $(PROJ_BASE)/dist
	rm -rf $(PROJ_BASE)/*.egg-info

.PHONY: build
build: clean_build
	@echo "Building python source distribution and wheel"
	$(VENVPYTHON) setup.py sdist bdist_wheel

.PHONY: test
test:
	$(VENVPYTHON) -m pip install -r ci-cd-requirements.txt
	$(VENVPYTHON) -m tox

.PHONY: docs
docs:
	$(VENVPYTHON) -m pip install -r $(PROJ_BASE)/docs/requirements-docs.txt
	cd docs && make html


.PHONY: upload
upload:
	$(PYTHONVENV)/bin/twine upload -r pypi dist/*

.PHONY: clean
clean:
	@echo "Removing Python virtual environment 'venv'."
	rm -rf $(PYTHONVENV)
	rm -rf .tox

.PHONY: sparkling
sparkling: clean
	rm -rf *.whl
	find . -name \*~ | xargs rm -f
	rm -rf dist build src/*.egg-info
	rm -rf **/__pycache__
	rm -rf docs/_build/*
	rm -f src/version.py
	rm -rf htmlcov
