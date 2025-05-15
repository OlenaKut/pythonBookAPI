# Dokumentation för BookApp
Denna dokumentation beskriver implementationen av BookApp – ett fullständigt CI/CD-projekt deployat i Kubernetes. Dokumentet täcker systemets arkitektur, teknologier, CI/CD-flöde, API-endpoints, testning och Kubernetes-setup.

**1. Arkitekturöversikt**
Systemet består av:
En webbapplikation (frontend) byggd med HTML/JavaScript
Ett REST API byggt i Flask (Python)
En PostgreSQL-databas
Deployment i Kubernetes (med namespace, deployments, services och ingress)
CI/CD-flöde via AWS CodeBuild, Docker och GitHub

Användaren interagerar med webbgränssnittet för att lägga till, redigera eller ta bort böcker. Flask-API:t hanterar alla databasanrop och kommunicerar med PostgreSQL.

**2. CI/CD-processen**
Koden pushas till ett GitHub-repo https://github.com/OlenaKut/cloudstartgolangapiOlena
En buildspec.yml-fil triggar AWS CodeBuild

# Byggprocess:
Installerar beroenden via requirements.txt
Bygger en Docker-image
Pushar imagen till Docker Hub (olenakutasevych/bookapi)
Kubernetes uppdateras via kubectl rollout restart

# Verktyg:
GitHub
AWS CodeBuild
Docker
Kubernetes
DBeaver (för DB-inspektion)

**3. Teknologier**
API-backend
Python + Flask
PostgreSQL
CI/CD
AWS CodeBuild
Docker
Kubernetes
DBeaver
HTML + JavaScript

**4. API-endpoints + testning**
GET /books
 Returnerar alla böcker i databasen
 Testas via webbläsare eller curl

POST /books
 Lägger till en ny bok
 Testas via frontend eller API-klient

PUT /books/<id>
 Uppdaterar information om en bok

DELETE /books/<id>
 Raderar en specifik bok

DELETE /books/delete_all
 Tar bort alla böcker i databasen

**5. Systemarkitektur / Kubernetes**
- Ingress Controller hanterar routing till API och frontend
- bookapi Deployment innehåller Flask-applikationen, exponeras via en ClusterIP Service
- book-postgres Deployment kör PostgreSQL med Persistent Volume
- Allt är isolerat i namespace my-namespace
- kubectl port-forward används för lokal åtkomst till databasen i DBeaver

# Webbadress
Applikationen nås via:
 http://bookapi.soon.it (via Ingress och DNS)