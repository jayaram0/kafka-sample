FROM python:3.8-slim

WORKDIR /app/consumer_2

COPY src/ .
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY src/ .

CMD ["python", "./main.py"]
