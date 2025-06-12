import hashlib
import os
import json

HASH_FILE = "hashes.json"

def calculate_hash(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

def save_hashes(files):
    hashes = {}
    for file in files:
        if os.path.exists(file):
            hashes[file] = calculate_hash(file)
        else:
            print(f"[X] {file} does not exist!")
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f)

def compare_hashes(files):
    if not os.path.exists(HASH_FILE):
        print("No saved hash file. Run save_hashes first.")
        return
    with open(HASH_FILE, "r") as f:
        old_hashes = json.load(f)
    for file in files:
        if os.path.exists(file):
            new_hash = calculate_hash(file)
            if file not in old_hashes:
                print(f"[✓] {file} is new.")
            elif old_hashes[file] != new_hash:
                print(f"[!] {file} has changed!")
            else:
                print(f"[✔] {file} is unchanged.")
        else:

            print(f"[X] {file} does not exist!")

files_to_check = ['testfile.txt', 'notes.docx']

#save_hashes(files_to_check)
compare_hashes(files_to_check)