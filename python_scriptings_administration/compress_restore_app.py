import zipfile
import os

def compress_directory(directory, output_filename):
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory))
        print(f"Successfully created ZIP file '{output_filename}' from directory '{directory}'.")
    except Exception as e:
        print(f"Error compressing directory: {e}")

def restore_zip_file(zip_filename, extract_to_directory):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(extract_to_directory)
        print(f"Successfully extracted ZIP file '{zip_filename}' to directory '{extract_to_directory}'.")
    except Exception as e:
        print(f"Error restoring ZIP file: {e}")

def main():
    while True:
        print("\nOptions:")
        print("1. Compress directory to ZIP")
        print("2. Restore ZIP to directory")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            directory = input("Enter the directory to compress: ").strip()
            if not os.path.isdir(directory):
                print(f"Error: '{directory}' is not a valid directory.")
                continue
            
            output_filename = input("Enter the name of the output ZIP file (e.g., archive.zip): ").strip()
            if not output_filename.endswith('.zip'):
                print("Error: Output file name must end with '.zip'.")
                continue
            
            compress_directory(directory, output_filename)
        
        elif choice == '2':
            zip_filename = input("Enter the ZIP file to restore: ").strip()
            if not os.path.isfile(zip_filename):
                print(f"Error: '{zip_filename}' is not a valid file.")
                continue
            
            extract_to_directory = input("Enter the directory to extract to: ").strip()
            if not os.path.exists(extract_to_directory):
                try:
                    os.makedirs(extract_to_directory)
                except Exception as e:
                    print(f"Error creating directory '{extract_to_directory}': {e}")
                    continue
            
            restore_zip_file(zip_filename, extract_to_directory)
        
        elif choice == '3':
            print("Exiting.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
