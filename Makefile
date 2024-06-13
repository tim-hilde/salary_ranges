.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################

setup_project:
	@echo "Creating virtual environment"
	@if pyenv virtualenvs | grep -q "salary_ranges"; then \
		echo "Virtual environment "salary_ranges" already exists."; \
	else \
		pyenv virtualenv salary_ranges; \
	fi
	@pyenv local salary_ranges

	@echo "Creating local folders"
	@if [ ! -d notebooks ]; then \
		mkdir notebooks; \
	fi
	@if [ ! -d models ]; then \
		mkdir models; \
	fi

	@echo "Installing packages"
	@pip install --upgrade pip
	@pip install -e .

install:
	@pip install --upgrade pip
	@pip install -e .

reinstall_package:
	@pip uninstall -y salary_ranges || :
	@pip install -e .
