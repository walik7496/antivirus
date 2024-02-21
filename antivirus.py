import tkinter as tk
from tkinter import filedialog
import hashlib

# Load the virus database
def load_virus_database():
    # Here you can load the virus database from a file or another source
    # In this example, we simply use some known hashes
    return {
        '62cdb92eb1beadd80350c5a90bd757eae41e56f' : 'Virus1',
        'ea5c8d0d2d47016e4d2a2a1b169cb4a02e9e57e2' : 'Virus2',
        'd3b07384d113edec49eaa6238ad5ff00' : 'Virus3'
    }

# Check file for viruses
def check_for_virus(file_path, virus_database):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_hash = hashlib.md5(file_data).hexdigest()
        if file_hash in virus_database:
            return True, virus_database[file_hash]
        else:
            return False, None

# Function to browse file and check for viruses
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        is_infected, virus_name = check_for_virus(file_path, virus_database)
        if is_infected:
            result_label.config(text=f'File is infected with {virus_name}!')
        else:
            result_label.config(text='File is clean.')

# Main application window
root = tk.Tk()
root.title("Antivirus")

# Load the virus database
virus_database = load_virus_database()

# GUI elements
label = tk.Label(root, text="Choose a file to scan for viruses:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
