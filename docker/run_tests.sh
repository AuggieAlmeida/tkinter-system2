#!/bin/bash

# Inicia o Xvfb em segundo plano
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99

# Aguarda o Xvfb iniciar
sleep 1

# Executa os testes
pytest "$@"

# Captura o código de retorno do pytest
exit_code=$?

# Mata o processo do Xvfb
pkill Xvfb

# Retorna o código de saída do pytest
exit $exit_code 