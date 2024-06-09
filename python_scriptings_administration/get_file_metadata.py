import os
import stat
import time

def get_file_metadata(file_path):
    try:
        if not os.path.isfile(file_path):
            raise ValueError(f"Error: '{file_path}' is not a valid file.")

        file_stats = os.stat(file_path)

        metadata = {
            "File Size (bytes)": file_stats.st_size,
            "Creation Time": time.ctime(file_stats.st_ctime),
            "Modification Time": time.ctime(file_stats.st_mtime),
            "Access Time": time.ctime(file_stats.st_atime),
            "File Permissions": stat.filemode(file_stats.st_mode),
            "Owner User ID": file_stats.st_uid,
            "Owner Group ID": file_stats.st_gid
        }

        print(f"\nMetadata for '{file_path}':")
        for key, value in metadata.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error retrieving metadata: {e}")

def main():
    while True:
        file_path = input("Enter the file path to get metadata (or 'exit' to quit): ").strip()
        
        if file_path.lower() == 'exit':
            print("Exiting.")
            break

        get_file_metadata(file_path)

if __name__ == '__main__':
    main()
