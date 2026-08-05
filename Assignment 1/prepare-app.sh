#!/bin/bash

echo "Preparing app..."

docker volume create flask_db_data 2>/dev/null || true

if docker compose build; then
    echo "Preparing done."
else
    echo "Failed to prepare the application."
fi