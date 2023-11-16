FROM python:3.8-slim

COPY requirements.txt .

RUN pip install -r requirements.txt --upgrade pip

RUN mkdir -p app

COPY ./app app

WORKDIR /app

EXPOSE 80

ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0", "--port", "80"]