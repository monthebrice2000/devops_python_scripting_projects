import configparser
import argparse

def read_config_file(config_file):
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        if not config.sections():
            print(f"No sections found in the configuration file: {config_file}")
            return

        print(f"Configuration values from '{config_file}':")
        for section in config.sections():
            print(f"[{section}]")
            for key, value in config.items(section):
                print(f"{key} = {value}")
    except Exception as e:
        print(f"Error reading configuration file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Read configuration values from a file.")
    parser.add_argument("config_file", help="Path to the configuration file.")
    
    args = parser.parse_args()
    read_config_file(args.config_file)

if __name__ == '__main__':
    main()
