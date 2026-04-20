import re
from detectors.base import BaseDetector

class RegexDetector(BaseDetector):
    def __init__(self):
        self.rules = {
            'AWS Access Key': r'AKIA[0-9A-Z]{16}',
            'Generic Secret': r'[pP][aA][sS][sS][wW][oO][rR][dD]\s*[:=]\s*["\']?([a-zA-Z0-9!@#$%^&*()_+]{8,})["\']?'
        }

    def detect(self, line: str):
        findings = []

        for name, pattern in self.rules.items():
            matches = re.findall(pattern, line)
            if matches:
                for match in matches:
                    findings.append({
                        'type': name,
                        'value': match,
                        'line': line,
                    })
        return findings