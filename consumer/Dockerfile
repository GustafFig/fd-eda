# Um Dockerfile para o ambiente de desenvolvimento
FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends \
                                  git \
                                  curl \
                                  wget \
                                  vim \
                                  gcc \
                                  sudo \
                                  sqlite3
                                  
RUN curl -sfL $(curl -s https://api.github.com/repos/powerman/dockerize/releases/latest | grep -i /dockerize-$(uname -s)-$(uname -m)\" | cut -d\" -f4) | install /dev/stdin /usr/local/bin/dockerize

# cria um usuário chamado python
RUN useradd -ms /bin/bash python

# entra como o usuário python
USER python

RUN pip install --user pdm

# Trabalha na pasta HOME do usuário python
WORKDIR /home/python/app/consumer

ENV MY_PYTHON_PACKAGES=/home/python/app/consumer/__pypackages__/3.10
# adiciona o diretório ao PYTHONPATH para encontrar os módulos dentro do src/
# colons separated
ENV PYTHONPATH=$PYTHONPATH:/home/python/app/consumer:${MY_PYTHON_PACKAGES}/lib
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

RUN echo 'eval "$(python -m pdm --pep582)"' >> ~/.bashrc

# Coloca apenas o CMD pois é container de desenvolvimento e não é um serviço
# Aponta para o tail /dev/null para manter o container de pé
CMD [ "bash", "./.docker/start-app.sh" ]
