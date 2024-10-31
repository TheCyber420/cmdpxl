#!/bin/bash

PROGRAM_NAME="cmdpxl"
REQUIREMENTS_FILE="requirements.txt"
SYMLINK_PATH="/usr/local/bin/$PROGRAM_NAME"
$VENV_DIR=".venv"
MAIN_SCRIPT="cmdpxl.py"

echo "Creating virtual environment..."
python3 -m venv "$VENV_DIR"

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

if [[ -f "$REQUIREMENTS_FILE" ]]; then
    echo "Installing dependencies..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Requirements file not found, skipping dependency installation."
fi

echo "Compiling Python files..."
python3 -m compileall "$PROJECT_DIR"

echo "Creating symlink..."
ln -sf "$MAIN_SCRIPT" "$SYMLINK_PATH"

deactivate

echo "Setup complete."
