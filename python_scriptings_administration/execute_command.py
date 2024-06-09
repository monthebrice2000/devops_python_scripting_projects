import subprocess
import argparse

def execute_command(command):
    try:
        # Execute the command and capture its output
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        # Print the command output
        print("Command output:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Execute an external command and capture its output.")
    parser.add_argument("command", help="The command to execute.")

    args = parser.parse_args()
    execute_command(args.command)

if __name__ == '__main__':
    main()
