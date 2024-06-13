.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################

create_pyenv:
	@if pyenv virtualenvs | grep -q "salary_ranges"; then \
		echo "Virtual environment "salary_ranges" already exists."; \
	else \
		pyenv virtualenv salary_ranges; \
	fi
	@pyenv local salary_ranges

install:
	@pip install --upgrade pip
	@pip install -e .

reinstall_package:
	@pip uninstall -y salary_ranges || :
	@pip install -e .
