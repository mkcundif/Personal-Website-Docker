# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    FLASK_APP=app.py

# Install system dependencies for Pillow or other libs if needed (minimal)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app source
COPY . /app

# Create a non-root user
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Set default DB path inside container and ensure entrypoint runs
ENV PROJECTS_DB_PATH=/data/projects.db

# Make entrypoint executable and switch to root briefly to change permissions
USER root
RUN chmod +x /app/entrypoint.sh && chown -R appuser /data || true
USER appuser

ENTRYPOINT ["/app/entrypoint.sh"]
# Default command: run with gunicorn on port 5000 with 4 workers
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "4"]
