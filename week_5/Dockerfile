
FROM python:3.11-slim

WORKDIR /app

# Install OS deps if needed (optional, can be skipped if not required)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY week_5/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire repo so week_2 and week_4 are available
COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "week_5.app:app", "--host", "0.0.0.0", "--port", "8000"]
