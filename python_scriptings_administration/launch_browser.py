import webbrowser
import re
import argparse

def is_valid_url(url):
    # Simple regex to check if the URL is valid
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def launch_browser(url):
    if is_valid_url(url):
        webbrowser.open(url)
        print(f"Opening {url} in your default web browser.")
    else:
        print(f"Error: '{url}' is not a valid URL.")

def main():
    parser = argparse.ArgumentParser(description="Launch a web browser with the specified URL.")
    parser.add_argument("url", help="The URL to open in the web browser.")
    
    args = parser.parse_args()
    launch_browser(args.url)

if __name__ == '__main__':
    main()
