import os
import sys
import zipfile

letters = [chr(ord('a') + i) for i in range(26)]
version = os.environ.get('VERSION', '1.2.0')

def create_text_files():
    for letter in letters:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is a sample text for the file {filename}.")

def check_text_files():
    missing_files = []
    for file in letters:
        if not os.path.exists(f"{file}.txt"):
            missing_files.append(file)
    if missing_files:
        print("Error: Not all txt files were created.")
        sys.exit(1)

def create_zip_files():
    for letter in letters:
        zip_filename = f"{letter}_{version}.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(f"{letter}.txt", arcname=f"{letter}.txt")

def check_zip_files():
    missing_zip_files = []
    for letter in letters:
        if not os.path.exists(f"{letter}_{version}.zip"):
            missing_zip_files.append(f"{letter}_{version}.zip")
    if missing_zip_files:
        print("Error: Not all zip files were created.")
        sys.exit(1)

def remove_unused_text_files():
    for file in os.listdir():
        if file.endswith('.txt'):
            os.remove(file)

def main():
    create_text_files()
    check_text_files()
    create_zip_files()
    check_zip_files()
    remove_unused_text_files()
    print("success")

if __name__ == "__main__":
    main()
