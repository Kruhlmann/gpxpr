help:
	@printf "\e[92m%s\e[0m\n" "make install"
	@echo " - Installs dependencies and gpxpr."
	@printf "\e[92m%s\e[0m\n" "make test"
	@echo " - Run tests"
	@printf "\e[92m%s\e[0m\n" "make fix"
	@echo " - Fixes common code problems"
	@printf "\e[92m%s\e[0m\n" "make lint"
	@echo " - Lints your code."
.PHONY: help
.DEFAULT: help
