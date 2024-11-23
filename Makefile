# Detecta se está rodando em Windows
ifeq ($(OS),Windows_NT)
	YELLOW :=
	GREEN  :=
	RED    :=
	BLUE   :=
	NC     :=
else
	YELLOW := \033[1;33m
	GREEN  := \033[1;32m
	RED    := \033[1;31m
	BLUE   := \033[1;34m
	NC     := \033[0m
endif

# .PHONY indica que estes targets não são arquivos reais
.PHONY: test test-gui build-test

# Target para rodar a aplicação
run:
	docker compose -f docker/docker-compose.yml run --rm app python src/main.py

# Target para executar os testes
test:
	docker compose -f docker/docker-compose.yml run --rm unittest pytest

# Target para executar os testes GUI
test-gui:
	docker compose -f docker/docker-compose.yml run --rm app pytest

# Target para limpar containers e recursos
clean:
	docker compose -f docker/docker-compose.yml down
	docker compose -f docker/docker-compose.yml rm -f

dev-run:
	@echo "${BLUE}Iniciando ambiente de desenvolvimento...${NC}"
	python main.py

# Target para instalar dependências de desenvolvimento
dev-install:
	pip install -r requirements-dev.txt
	
dev-deps: dev-install
	@echo "${YELLOW}Verificando dependências de desenvolvimento...${NC}"
	@python -c "import customtkinter" || (echo "${RED}Instalando customtkinter...${NC}" && pip install customtkinter)
	@python -c "import sqlite3" || echo "${GREEN}SQLite já instalado${NC}"

dev-setup: dev-deps
	@echo "${BLUE}Iniciando ambiente de desenvolvimento...${NC}"
	python main.py

# Target para verificar estilo do código
lint:
	@echo "${YELLOW}Verificando estilo do código...${NC}"
	flake8 src tests
	black --check src tests

# Target para formatar o código
format:
	@echo "${BLUE}Formatando código...${NC}"
	black src tests

# Target para gerar relatório de cobertura
coverage:
	@echo "${YELLOW}Gerando relatório de cobertura...${NC}"
	pytest --cov=src tests/ --cov-report=html
	@echo "${GREEN}Coverage report generated in htmlcov/index.html${NC}"

# Target para construir a imagem de teste
build-test:
	@echo "${BLUE}Construindo imagem de teste...${NC}"
	docker compose -f docker/docker-compose.yml build unittest