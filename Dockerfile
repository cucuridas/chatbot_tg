FROM python:3.11.1-slim

ENV PYTHONUNBUFFERED 1
EXPOSE 8000
WORKDIR /app

RUN apt-get update && apt-get install vim curl build-essential -y && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install poetry && poetry config virtualenvs.in-project true 

#COPY pyproject.toml ./
COPY . ./
RUN poetry update
#poetry update --no-dev # 빌드 후 젠킨스에서 test 수행하기 위해 모두 설치

CMD poetry run alembic upgrade head && \
    poetry run uvicorn app.core.server:app --host 0.0.0.0 --port 8000
#    poetry run gunicorn --bind 0.0.0.0:8000 -w 1 --timeout 120 -k uvicorn.workers.UvicornWorker app.core.server:app
# poetry run uvicorn app.core.server:app --host 0.0.0.0 --port 8000 --workers 1
