FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pip poetry setuptools wheel -U --no-cache-dir
RUN poetry config virtualenvs.in-project true

WORKDIR /usr/dinopedia/app

COPY pyproject.toml poetry.lock init.sh .
RUN poetry install --no-cache

COPY dinopedia dinopedia
RUN poetry install --no-cache

RUN useradd --user-group --no-create-home app
RUN chown -R app:app /usr/dinopedia/app

USER app

ENTRYPOINT ["/bin/bash"]
CMD ["init.sh"]
