#!/bin/bash

PROGRAM_NAME="cmdpxl"
REQUIREMENTS_FILE="requirements.txt"
INSTALL_DIR=$HOME
BIN_DIR="/usr/local/bin"
VENV_DIR=".venv"
MAIN_SCRIPT="cmdpxl.py"

echo "Creating virtual environment..."
python3 -m venv "$VENV_DIR"

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

if [[ -f "$REQUIREMENTS_FILE" ]]; then
    echo "Installing dependencies..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Requirements file #!/bin/bashnot found, skipping dependency installation."
fi

echo "Compiling Python files..."
pyinstaller --onefile $MAIN_SCRIPT
COMPILED_EXECUTABLE="dist/$PROGRAM_NAME"

echo "Copying necessary files..."
rm -rf "$INSTALL_DIR/$PROGRAM_NAME/$PROGRAM_NAME" || return 1
mkdir -p "$INSTALL_DIR/$PROGRAM_NAME/output"
mv "$COMPILED_EXECUTABLE" "$INSTALL_DIR/$PROGRAM_NAME"


echo "Creating symlink..."
sudo rm -rf "$BIN_DIR/$PROGRAM_NAME" || return 1
sudo ln -s $INSTALL_DIR/$PROGRAM_NAME/$PROGRAM_NAME $BIN_DIR/$PROGRAM_NAME

deactivate

echo "Cleaning up..."
rm -rf .venv
rm -rf build
rm -rf dist
rm -f "$PROGRAM_NAME.spec"

echo "Setup complete."
