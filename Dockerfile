FROM python:3.13-slim

# Set a working dir
WORKDIR /app

# Install system deps for building (if any) and to run gunicorn
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only what we need and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Optional: create instance folder and make sure sqlite path exists
RUN mkdir -p /app/instance

# Expose port (matches Procfile)
EXPOSE 8000

# Run with Gunicorn pointing at run:app (run.py creates `app = create_app()`)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]