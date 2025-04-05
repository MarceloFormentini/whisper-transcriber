FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get update && apt-get install -y ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]