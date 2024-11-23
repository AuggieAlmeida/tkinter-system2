FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar código fonte
COPY . .

# Configurar variáveis de ambiente
ENV PYTHONPATH=/app
ENV DISPLAY=:0

CMD ["python3", "main.py"] 