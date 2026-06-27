# Web Application Deploment with Docker

## Deployment Requirements
* Docker Engine (v20.10.0 or higher)
* Docker Compose CLI Plugin

## Application Description
This application is a two-tier web featuring a python flask frontend and PostgreSQL relational DB backend. The web layer communicates securely with the db layer.

## Network and Volume Details
* **Network ('flask_app_network')**: An isolated bridge network that securly links the web container to db container.
* **Volume ('flask_db_data')**: A named persistent volume mapped to the PostgreSQL data directory to preserve database records across container restarts.

## Container Configuration
###Container List 
* **flask_web**: Custom Python Flask container running on port `5000`.
* **flask_db**: Standard `postgres:15-alpine` container running internally on port `5432`.

## Instructions
1. Run `./prepare-app.sh` to compile images and establish network resources.
2. Run `./start-app.sh` to initialize the containers.
3. Open a browser and navigate to `http://localhost:5000`.
4. Run `./stop-app.sh` to pause application instances safely.
5. Run `./remove-app.sh` to completely purge all containers, custom images, networks, and volumes.

## Example Workflow
```bash
# Create application resources
./prepare-app.sh
# Preparing app...

# Run the application
./start-app.sh
# Running app ...
# The app is available at http://localhost:5000

# Pause the application
./stop-app.sh
# Stopping app...

# Delete all application resources
./remove-app.sh
# Removed app.