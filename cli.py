import argparse
import os
from scanner.scan_directory import scan_directory

def is_path_exists(path):
    return os.path.exists(path)

def main():
    parser = argparse.ArgumentParser(description="Secret Seeker")
    parser.add_argument('path', help="Path to scan")
    parser.add_argument('--output', default="report.json", help="Output file")
    args = parser.parse_args()

    if not is_path_exists(args.path):
        print("Path does not exist")
        exit(1)

    files = scan_directory(args.path)
    print(files)
if __name__ == '__main__':
    main()