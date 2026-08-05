#!/bin/bash

echo "Running app..."

if docker compose up -d; then
    echo "The app is available at http://localhost:5000"
else
    echo "Failed to start the application."
fi