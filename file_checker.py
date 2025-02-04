import hashlib
import os
import json

# Function to calculate the hash of a file
def calculate_hash(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to save hash values to a JSON file
def save_hashes(hash_dict, hash_file):
    with open(hash_file, 'w') as f:
        json.dump(hash_dict, f, indent=4)

# Function to load hash values from a JSON file
def load_hashes(hash_file):
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            return json.load(f)
    return {}

# Function to check file integrity
def check_integrity(directory, hash_file='file_hashes.json', algorithm='sha256'):
    stored_hashes = load_hashes(hash_file)
    current_hashes = {}
    
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Checking file: {file_path}")
            file_hash = calculate_hash(file_path, algorithm)
            if file_hash:
                current_hashes[file_path] = file_hash
                if file_path in stored_hashes:
                    if stored_hashes[file_path] != file_hash:
                        print(f"[WARNING] File changed: {file_path}")
                    else:
                        print(f"[OK] File unchanged: {file_path}")
                else:
                    print(f"[NEW] File added: {file_path}")
    
    for file_path in stored_hashes:
        if file_path not in current_hashes:
            print(f"[DELETED] File removed: {file_path}")
    
    save_hashes(current_hashes, hash_file)
    print("Integrity check complete.")

# Main execution
def main():
    directory_to_monitor = input("Enter the directory to monitor: ").strip()
    if not directory_to_monitor:
        print("Error: No directory provided.")
        return
    check_integrity(directory_to_monitor)

if __name__ == "__main__":
    main()
