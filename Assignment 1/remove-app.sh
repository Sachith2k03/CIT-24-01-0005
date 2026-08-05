#!/bin/bash

echo "Removing app..."

docker compose down -v --rmi local

docker network rm flask_app_network 2>/dev/null || true
docker volume rm flask_db_data 2>/dev/null || true

echo "All app resources removed."