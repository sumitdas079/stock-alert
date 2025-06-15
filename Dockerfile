# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set environment variables to ensure Python outputs logs to stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set environment variables to prevent Python from writing .pyc files and to buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /stock-alert

# Copy only requirements first to leverage Docker's caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project
COPY . .

# Command to run FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]