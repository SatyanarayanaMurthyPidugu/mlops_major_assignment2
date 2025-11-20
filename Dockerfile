# Use an officially supported Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python dependencies without cache
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase
COPY . .

# Expose application port
EXPOSE 8000

# Start Gunicorn server for app:app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
