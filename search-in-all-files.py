
# Если нужно искать в .sty файлах, меняйте ниже чуть код! По умолчанию он ищет в .tex файлах


import os
import fnmatch


search_text = "Download"

def search_in_file(file_path, search_text, search_output_lines):
    """Search for search_text in the specified file and collect lines containing the search_text."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin1') as file:
            lines = file.readlines()
    
    # Collect lines containing search_text
    for line in lines:
        if search_text in line:
            search_output_lines.append(f"File: {file_path}\n{line}\n")

def search_in_directory(root_dir, search_text):
    """Walk through all directories in root_dir and search for search_text in .tex files."""
    search_output_lines = []
    for root, _, files in os.walk(root_dir):
        for filename in files:
                file_path = os.path.join(root, filename)
                search_in_file(file_path, search_text, search_output_lines)
    
    # Write the collected lines to out-search.txt
    with open("out-search.txt", 'w', encoding='utf-8') as outfile:
        outfile.writelines(search_output_lines)

# Define the directory to start the search
script_directory = os.path.dirname(os.path.abspath(__file__))
root_directory = script_directory  # Use the directory of the script itself


# Execute the search
search_in_directory(root_directory, search_text)
