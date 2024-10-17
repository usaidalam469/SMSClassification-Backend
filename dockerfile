# Use the official Python image
FROM python:3.12-slim

# Install system dependencies, including those required to build psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev build-essential \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port
EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
