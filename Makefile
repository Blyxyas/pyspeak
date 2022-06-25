.PHONY: target install check
.DEFAULT_GOAL := target


install:
	( \
		source venv/bin/activate; \
		pip install -r requirements-dev.txt; \
	);

target: ./src/**/*
# Clean lock.sha1
	rm -rf ./.filehash/lock.sha1
# 2. Generate the Sha1 Sum and save it to .filehash/lock.sha1
	@echo -e "\033[1;35mGenerating Sha1 Sums...\033[0m"
	@for file in $^; do \
		sha1sum $${file} >> .filehash/lock.sha1;\
	done

# 3. Check types with MyPy
	@echo -e "\033[1;34mChecking static types\033[0m"
	@mypy ./src/


# 3. Generate the stub files (https://peps.python.org/pep-0484/#stub-files) with MyPy
	@echo -e "\033[1;33mGenerating stubs\033[0m"
	@stubgen ./src/