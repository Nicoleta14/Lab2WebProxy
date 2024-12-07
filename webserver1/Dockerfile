FROM python:3.9-slim

WORKDIR /app

# Copiem fișierul "app.py" din directorul local în directorul de lucru al containerului.
COPY app.py /app
RUN pip install flask redis

# Specificăm să ruleze scriptul "app.py" folosind Python.
CMD ["python", "app.py"]
