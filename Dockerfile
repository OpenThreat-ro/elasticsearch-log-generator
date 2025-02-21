FROM python:3.9-slim

WORKDIR /app

COPY log_generator.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "log_generator.py"]

