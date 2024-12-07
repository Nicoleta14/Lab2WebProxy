FROM python:3.9-slim

# Setăm directorul de lucru în container la "/app".
WORKDIR /app
COPY app.py /app
RUN pip install flask redis

# Specificăm să ruleze scriptul "app.py" folosind Python.
CMD ["python", "app.py"]
