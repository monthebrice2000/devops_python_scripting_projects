import tarfile
import os

def create_tar_archive(directory, output_filename):
    try:
        with tarfile.open(output_filename, 'w:gz') as tar:
            tar.add(directory, arcname=os.path.basename(directory))
        print(f"Successfully created TAR archive '{output_filename}' from directory '{directory}'.")
    except Exception as e:
        print(f"Error creating TAR archive: {e}")

def examine_tar_contents(tar_filename):
    try:
        with tarfile.open(tar_filename, 'r:gz') as tar:
            print(f"Contents of TAR archive '{tar_filename}':")
            tar.list()
    except Exception as e:
        print(f"Error examining TAR contents: {e}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create TAR archive")
        print("2. Examine TAR contents")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            directory = input("Enter the directory to archive: ").strip()
            if not os.path.isdir(directory):
                print(f"Error: '{directory}' is not a valid directory.")
                continue
            
            output_filename = input("Enter the name of the output TAR file (e.g., archive.tar.gz): ").strip()
            if not output_filename.endswith('.tar.gz'):
                print("Error: Output file name must end with '.tar.gz'.")
                continue
            
            create_tar_archive(directory, output_filename)
        
        elif choice == '2':
            tar_filename = input("Enter the TAR file to examine: ").strip()
            if not os.path.isfile(tar_filename):
                print(f"Error: '{tar_filename}' is not a valid file.")
                continue
            
            examine_tar_contents(tar_filename)
        
        elif choice == '3':
            print("Exiting.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
