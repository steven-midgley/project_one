#!/bin/bash

PROJECT_DIR=$(pwd)
ENV_DIR="$PROJECT_DIR/my_env"

echo "Creating virtual environment..."
python3 -m venv "$ENV_DIR"

echo "Activating virtual environment..."
source "$ENV_DIR/bin/activate"

echo "Installing requirements..."
pip install -r "$PROJECT_DIR/requirements.txt" --force-reinstall

echo "Verifying installed packages..."
pip freeze

echo "Running application..."
gunicorn -w 4 -b 0.0.0.0:80 app:app



