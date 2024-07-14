FROM python:3.10.12-slim-buster as base

FROM base as builder 

COPY ./requirements.txt ./scripts/install.sh ./
RUN ./install.sh && python -m venv /opt/venv

# setup venv as path
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

FROM base

RUN apt-get update \
    && apt-get -y install procps

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /opt/mlflow

COPY ./scripts/run.sh /opt/mlflow/

RUN chmod +x ./run.sh

# Main API
CMD ["./run.sh"]