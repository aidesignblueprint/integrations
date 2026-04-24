FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "mcp==1.26.0" httpx

COPY server.py .

CMD ["python", "server.py"]
