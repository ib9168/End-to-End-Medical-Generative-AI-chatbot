# Use a small Python image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Copy everything into the container
COPY . /app

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Exposes the port that Render assigns
ENV PORT=8080

# Run  Flask app server using Gunicorn (production-grade)
CMD gunicorn -b 0.0.0.0:$PORT app:app
