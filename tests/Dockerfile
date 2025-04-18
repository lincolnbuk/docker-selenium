FROM python:3.11-slim

LABEL Name="docker-selenium-tests" \
      Version="1.0" \
      Description="Contêiner para executar testes Selenium com Python" \
      Maintainer="Seu Nome <seuemail@exemplo.com>"

WORKDIR /usr/src/app

COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para executar os testes
CMD ["python3", "-m", "unittest", "discover", "-s", "tests/SeleniumTests", "-p", "*.py"]
