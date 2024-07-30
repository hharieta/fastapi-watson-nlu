FROM python:3.12.3-slim

LABEL maintainer="Inge Gatovsky | contacto@hharieta.lat"

ARG USERID=1000
ARG GROUPID=1000
ARG USERNAME=appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd --gid ${GROUPID} ${USERNAME} \
        && useradd --uid ${USERID} --gid ${GROUPID} --shell /bin/sh -m ${USERNAME}
USER ${USERNAME}

EXPOSE 8000


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
