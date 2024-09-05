FROM python:3.9.16-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m myuser
USER myuser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.api.app:server"]
