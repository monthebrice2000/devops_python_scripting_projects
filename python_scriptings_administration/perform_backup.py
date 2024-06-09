import os
import subprocess
import argparse

def perform_backup(source, destination, exclude=None, dry_run=False):
    try:
        # Validate source directory
        if not os.path.isdir(source):
            raise ValueError(f"Error: Source '{source}' is not a valid directory.")

        # Validate destination directory
        if not os.path.isdir(destination):
            raise ValueError(f"Error: Destination '{destination}' is not a valid directory.")

        # Construct rsync command
        rsync_command = ["rsync", "-avh", "--delete"]

        if dry_run:
            rsync_command.append("--dry-run")

        if exclude:
            for pattern in exclude:
                rsync_command.extend(["--exclude", pattern])

        rsync_command.extend([source, destination])

        # Execute rsync command
        result = subprocess.run(rsync_command, capture_output=True, text=True)
        
        # Check for errors
        if result.returncode != 0:
            raise RuntimeError(f"rsync error: {result.stderr}")

        print("Backup completed successfully.")
        if dry_run:
            print("Dry run output:\n", result.stdout)
        
    except Exception as e:
        print(f"Error during backup: {e}")

def main():
    parser = argparse.ArgumentParser(description="Backup files using rsync.")
    parser.add_argument("source", help="Source directory to back up.")
    parser.add_argument("destination", help="Destination directory for the backup.")
    parser.add_argument("-e", "--exclude", nargs='*', help="Patterns to exclude from the backup.")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Perform a dry run without making any changes.")
    
    args = parser.parse_args()

    perform_backup(args.source, args.destination, args.exclude, args.dry_run)

if __name__ == '__main__':
    main()
