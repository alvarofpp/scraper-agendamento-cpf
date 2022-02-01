# Variables
PACKAGE_NAME=mre
DOCKER_IMAGE_LINTER=alvarofpp/python-linter
ROOT=$(shell pwd)
LINT_COMMIT_TARGET_BRANCH=origin/main
SERVICE_NAME=scraper-cpf

# Commands
.PHONY: build
build: install-hooks
	@docker-compose build --pull

.PHONY: build-no-cache
build-no-cache: install-hooks
	@docker-compose build --no-cache --pull

.PHONY: install-hooks
install-hooks:
	git config core.hooksPath .githooks

.PHONY:
down:
	@docker-compose down

.PHONY:
up:
	@docker-compose up ${SERVICE_NAME}

.PHONY:
up-silent:
	@docker-compose up -d ${SERVICE_NAME}

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-yaml \
		&& lint-markdown \
		&& lint-python"

.PHONY: logs
logs:
	@docker-compose logs --follow
