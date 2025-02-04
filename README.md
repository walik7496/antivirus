# Antivirus File Scanner

This is a simple antivirus file scanner built with Python using the `tkinter` library for the graphical user interface (GUI) and `hashlib` for file hashing. It scans a file for known viruses by comparing its hash against a pre-defined virus database.

## Features
- GUI interface for easy file selection.
- Scans files by calculating their MD5 hash.
- Matches the file hash against a small virus database.
- Displays whether the file is clean or infected with a known virus.

## Requirements
- Python 3.x
- tkinter (usually comes pre-installed with Python)
- hashlib (part of Python's standard library)

## Installation

1. Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
   
2. Clone or download the project files.

3. No additional dependencies are required as `tkinter` and `hashlib` come with Python.

## How to Use

1. Run the script:  
   ```bash
   python antivirus_scanner.py
   ```
2. The application window will appear. Click the "Browse" button to choose a file to scan.

3. The file will be scanned for known viruses. The result will be displayed in the window:
 - If the file is clean, it will say "File is clean."
 - If the file is infected with a known virus, it will show the virus name.

## Virus Database

The virus database in this example is a mock database containing a few hardcoded hashes of known viruses:
- Virus1: 62cdb92eb1beadd80350c5a90bd757eae41e56f
- Virus2: ea5c8d0d2d47016e4d2a2a1b169cb4a02e9e57e2
- Virus3: d3b07384d113edec49eaa6238ad5ff00

To expand the functionality, you can modify the load_virus_database() function to load more hashes or even pull them from an external source.

## How It Works

1. The user selects a file using the "Browse" button.
2. The file’s MD5 hash is computed and checked against the database.
3. If a match is found, the file is flagged as infected and the virus name is displayed.
4. If no match is found, it confirms that the file is clean.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
