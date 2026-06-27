#!/bin/bash
echo "Removed app..."

docker compose down -v

docker rmi $(docker images 'flask-web' -q) 2>/dev/null || true

docker network rm flask_app_network 2>/dev/null || true
docker volume rm flask_db_data 2>/dev/null || true

echo "All app resources removed."
