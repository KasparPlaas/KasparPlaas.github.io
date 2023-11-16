FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN /venv/bin/python -m pip install --upgrade pip && \
    /venv/bin/python -m pip install -r requirements.txt

COPY ./app /app

EXPOSE 80

CMD ["/venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]