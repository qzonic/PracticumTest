FROM python:3.9-slim

RUN mkdir /bot

COPY requirements.txt /bot

RUN pip3 install --upgrade pip

RUN pip3 install -r /bot/requirements.txt --no-cache-dir

COPY . /bot

WORKDIR /bot/

CMD ["python3", "./bot/__main__.py"]