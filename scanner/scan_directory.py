import os
from detectors.regex_detectors import RegexDetector

IGNORED_DIRS = {".git", '.idea', '__pycache__', '.venv', 'venv'}
IGNORED_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".bmp", ".gif", ".svg", ".webp", ".ico",
    ".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar",
    ".bin", ".exe", ".dll", ".so", ".dylib", ".pdf", ".mp3", ".mp4",
    "iso", "img"
}

def scan_directory(path: str):
    print(f'Scanning directory: {path}')
    findings = []

    detector = RegexDetector()

    for root, dirs, filenames in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext.lower() in IGNORED_EXTENSIONS:
                continue

            full_path = os.path.join(root, filename)
            try:
                with open(full_path, encoding='utf-8', errors='ignore') as f:
                    for line_number, line in enumerate(f, start=1):

                        matches = detector.detect(line)

                        if matches:
                            for match in matches:
                                findings.append({
                                    'file': full_path,
                                    'line': line_number,
                                    'type': match['type'],
                                    'value': match['value']
                                })
            except OSError:
                continue
    return findings