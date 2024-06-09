import os
import argparse

def create_directory(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def delete_directory(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"Error: '{directory}' is not a valid directory.")
        
        os.rmdir(directory)
        print(f"Directory '{directory}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting directory: {e}")
    except Exception as e:
        print(f"Error: {e}")

def examine_filesystem(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"Error: '{directory}' is not a valid directory.")
        
        print(f"Contents of '{directory}':")
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
    except Exception as e:
        print(f"Error examining filesystem: {e}")

def main():
    parser = argparse.ArgumentParser(description="Filesystem operations: create, delete, or examine directories.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to perform")

    # Create subcommand
    parser_create = subparsers.add_parser("create", help="Create a directory")
    parser_create.add_argument("directory", help="Directory to create")

    # Delete subcommand
    parser_delete = subparsers.add_parser("delete", help="Delete a directory")
    parser_delete.add_argument("directory", help="Directory to delete")

    # Examine subcommand
    parser_examine = subparsers.add_parser("examine", help="Examine the contents of a directory")
    parser_examine.add_argument("directory", help="Directory to examine")

    args = parser.parse_args()

    if args.command == "create":
        create_directory(args.directory)
    elif args.command == "delete":
        delete_directory(args.directory)
    elif args.command == "examine":
        examine_filesystem(args.directory)

if __name__ == '__main__':
    main()
