export PYTHONPATH := .:$(PYTHONPATH)

PACKAGE=src


all: style typecheck doccheck unit-tests coverage
.PHONY: all

style:
		###### Running style analysis ######
		poetry run flake8 $(PACKAGE)

typecheck:
		###### Running static type analysis ######
		poetry run mypy $(PACKAGE)

doccheck:
		###### Running documentation analysis ######
		poetry run pydocstyle -v $(MODULES)

static-tests: style typecheck doccheck
