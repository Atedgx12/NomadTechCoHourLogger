import os

def print_directory_tree(root_dir, file, prefix=''):
    items = os.listdir(root_dir)
    items.sort()
    
    for i, item in enumerate(items):
        path = os.path.join(root_dir, item)
        if i == len(items) - 1:
            file.write(f"{prefix}└── {item}\n")
            if os.path.isdir(path):
                print_directory_tree(path, file, prefix + "    ")
        else:
            file.write(f"{prefix}├── {item}\n")
            if os.path.isdir(path):
                print_directory_tree(path, file, prefix + "│   ")

# Define the root directory
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Define the output file path
output_file_path = os.path.join(root_directory, 'dirStructure', 'directory_tree.txt')

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Open the file for writing with UTF-8 encoding and print the directory tree
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(f"{root_directory}\n")
    print_directory_tree(root_directory, file)
