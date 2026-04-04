FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# O servidor Flask precisa ouvir em todas as interfaces (0.0.0.0)
CMD ["python", "server.py"]