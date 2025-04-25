# syntax=docker/dockerfile:1

# Build stage
FROM python:3.9-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy only necessary files from builder
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy application code
COPY app.py .
COPY database.py .
COPY config.py .
COPY templates/ templates/
COPY static/ static/

# Create necessary directories
RUN mkdir -p uploads database_file
COPY database_file/ database_file/

# Create non-root user and set permissions
RUN useradd -m appuser && \
    chown -R appuser:appuser /app && \
    chmod 755 /app/database_file

USER appuser

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

EXPOSE 5000
