import glob
import os

def pattern_match_files_and_directories(directory, pattern):
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"Error: '{directory}' is not a valid directory.")
        
        search_path = os.path.join(directory, pattern)
        matches = glob.glob(search_path)
        
        if not matches:
            print(f"No matches found for pattern '{pattern}' in directory '{directory}'.")
            return
        
        print(f"\nMatches for pattern '{pattern}' in directory '{directory}':")
        for match in matches:
            print(match)

    except Exception as e:
        print(f"Error during pattern matching: {e}")

def main():
    while True:
        directory = input("Enter the directory to search (or 'exit' to quit): ").strip()
        
        if directory.lower() == 'exit':
            print("Exiting.")
            break
        
        pattern = input("Enter the pattern to match (e.g., '*.txt', 'subdir/*'): ").strip()
        
        pattern_match_files_and_directories(directory, pattern)

if __name__ == '__main__':
    main()
