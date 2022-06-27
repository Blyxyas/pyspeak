.PHONY: target install
.DEFAULT_GOAL := target
SHELL := /bin/bash

TOTAL = 6

install:
	( \
		source venv/bin/activate; \
		pip install -r requirements-dev.txt; \
	);

target: ./src/**/*

# 1. Check if we're in a venv.

# This means that we're in a venv
ifeq (,$(findstring venv/lib/python3.10/site-packages/pip,$(shell pip -V)))
	@echo -e "\033[1;35m================================================================================\n\033[1;31mERROR: Please activate your Virtual Environment with name 'venv'\n\033[1;35m================================================================================\033[0m"
	@exit 1
else
	@echo -e "\033[1;35m[ 1/$(TOTAL) ] \033[1;32mVirtual Environment Detected!\033[0m"
endif

# Clean lock.sha1
	@echo -e "\033[1;35m[ 2/$(TOTAL) ] \033[1;36mCleaning...\033[0m"
	@rm -rf ./.filehash/lock.sha1
# 2. Generate the Sha1 Sum and save it to .filehash/lock.sha1
	@echo -e "\033[1;34m[ 3/$(TOTAL) ] \033[1;35mGenerating Sha1 Sums...\033[0m"
	@for file in $^; do \
		sha1sum $${file} >> .filehash/lock.sha1;\
	done

# 3. Generate the stub files (https://peps.python.org/pep-0484/#stub-files) with MyPy
	@echo -e "\033[1;35m[ 4/$(TOTAL) ] \033[1;33mGenerating stubs\033[0m"
	@stubgen ./src/ -q

	@echo -e "\033[1;32mDone!\033[0m"

# 4. Check types with MyPy
	@echo -e "\033[1;35m[ 5/$(TOTAL) ] \033[1;34mChecking static types\033[0m"
	@mypy ./src/

# 5. Test all tests

	@echo -e "\033[1;35m[ 6/$(TOTAL) ] \033[1;35mTesting...\033[0m"
	@pytest -v