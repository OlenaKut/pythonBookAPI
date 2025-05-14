# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]



# docker build -t olenakutasevych/bookapi .
# docker push olenakutasevych/bookapi
#


# Rebuild image locally
# docker buildx build --platform linux/amd64 -t olenakutasevych/bookapi:latest .

# Push with buildx (especially important on M1/M2 Macs)
# docker buildx build --platform linux/amd64 -t olenakutasevych/bookapi:latest --push .
