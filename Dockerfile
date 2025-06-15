# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set environment variables to ensure Python outputs logs to stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set environment variables to prevent Python from writing .pyc files and to buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies using apk
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    gcc \
    musl-dev \
    python3-dev \
    libressl-dev

# Create a non-root user and set workdir
RUN adduser -D appuser
WORKDIR /stock-alert

# Set permissions on the directory (as root)
RUN mkdir -p /stock-alert && chmod -R 777 /stock-alert

# Copy only requirements first to leverage Docker's caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optionally remove build dependencies to slim the image
RUN apk del build-base gcc musl-dev python3-dev libressl-dev libffi-dev

# Copy the whole project
COPY . .

# Change user to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Command to run FastAPI using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]