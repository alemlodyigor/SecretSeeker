import argparse
import os
import json
from scanner.scan_directory import scan_directory
from reporters.json_reporter import json_reporter

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

    findings = scan_directory(args.path)
    report = json_reporter(findings)

    with open(args.output, "w", encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(findings)
    print(f"Report saved to: {args.output}")

if __name__ == '__main__':
    main()