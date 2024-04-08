FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-devel

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY splade /app/splade
COPY conf /app/conf
COPY main_config /app/main_config
COPY data/toy_data /app/data/toy_data

WORKDIR /app

RUN mkdir -p /app/checkpoint /app/model_checkpoint  /app/output
# ENTRYPOINT [ "python", "main.py" ]
