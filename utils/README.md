# Utility Scripts

This directory contains utility scripts to help manage and automate tasks within the hardware project.

## Environment Setup (One-time)

Before running any utility scripts for the first time, you need to set up a Python virtual environment and install the required packages. This ensures that the scripts run in an isolated environment with the correct dependencies.

1.  **Open your terminal or command prompt.**
2.  **Navigate to the `utils` directory** within this project:
    ```sh
    cd path\to\hardware\utils
    ```
3.  **Create the virtual environment:**
    ```sh
    python -m venv .venv
    ```
    This will create a new folder named `.venv` in the `utils` directory.
4.  **Activate the virtual environment:**
    *   On Windows (PowerShell):
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
    *   On Windows (Command Prompt):
        ```cmd
        .\.venv\Scripts\activate.bat
        ```
    *   On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```
    Your terminal prompt should change to indicate that the virtual environment is active (e.g., `(.venv) ...`).
5.  **Install required packages:**
    With the virtual environment active, run the following command to install the necessary Python libraries:
    ```sh
    pip install PyYAML
    ```

You only need to perform these setup steps once. For subsequent uses, you just need to activate the virtual environment (step 4) before running a script.

## `cli_new_part.py`

### Purpose

The `cli_new_part.py` script is a command-line tool designed to streamline the creation of new part entries in this repository. It automates the process of:

1.  Generating a unique 5-digit part number.
2.  Creating a new directory for the part, named with this part number.
3.  Generating a `metadata.yaml` file within the new part directory, pre-filled with information provided by the user via interactive prompts.

This helps ensure consistency and reduces manual effort when adding new hardware components.

### How to Use

1.  **Open your terminal or command prompt.**
2.  **Navigate to the `utils` directory** within this project:
    ```sh
    cd path\to\hardware\utils
    ```
3.  **Activate the Python virtual environment** (if not already active):
    *   On Windows (PowerShell):
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
    *   On Windows (Command Prompt):
        ```cmd
        .\.venv\Scripts\activate.bat
        ```
    *   On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```
4.  **Run the script** using Python:
    ```sh
    python cli_new_part.py
    ```
5.  **Follow the prompts:** The script will ask you for various details about the new part, such as owner, name, description, etc. Provide the information as requested.
6.  Once all information is gathered, the script will create the new part directory and its `metadata.yaml` file in the main `hardware` directory (one level above `utils`).
7.  **Deactivate the virtual environment** when you are done (optional but good practice):
    ```sh
    deactivate
    ```

Example: If the script generates part number `12345`, it will create a directory `../12345/` and `../12345/metadata.yaml`.
