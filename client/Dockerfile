FROM python:3.9-slim
RUN apt-get update && apt-get install -y python3-tk
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "client.py"]