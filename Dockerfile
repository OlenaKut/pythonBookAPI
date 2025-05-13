FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]




# - docker build -t git.systementor.se/olena/pythonapi .
# - docker push git.systementor.se/olena/pythonapi

# Rebuild image locally
# docker buildx build --platform linux/amd64 -t git.systementor.se/olena/pythonapi:latest .

# Push with buildx (especially important on M1/M2 Macs)
# docker buildx build --platform linux/amd64 -t git.systementor.se/olena/pythonapi:latest --push .