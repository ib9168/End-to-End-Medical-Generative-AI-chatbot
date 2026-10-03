# Use a small Python image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install CPU-only PyTorch first (sentence-transformers needs it). The default
# PyPI build bundles ~3GB of CUDA libraries this app never uses. Doing it before
# COPY also keeps this heavy layer cached across code changes.
RUN pip install --no-cache-dir torch==2.7.1 --index-url https://download.pytorch.org/whl/cpu

# Copy everything into the container
COPY . /app

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Exposes the port that Render assigns
ENV PORT=8080

# Run  Flask app server using Gunicorn (production-grade)
CMD gunicorn -b 0.0.0.0:$PORT app:app
