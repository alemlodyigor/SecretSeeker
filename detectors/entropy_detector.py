from collections import Counter
import math
from detectors.base import BaseDetector

class EntropyDetector(BaseDetector):
    def __init__(self, threshold=4.0):
        super().__init__()
        self.threshold = threshold

    def detect(self, line: str):
        if not line.strip():
            return []

        words = line.split()

        results = []

        for word in words:
            if len(word) >= 8:
                entropy = self.calculate_entropy(word)
                if entropy >= self.threshold:
                    results.append({
                        'type': 'High entropy',
                        'value': word,
                        'line': line,
                        'entropy': round(entropy, 2)
                    })
        return results

    @staticmethod
    def calculate_entropy(line: str) -> float:
        if not line.strip():
            return 0.0

        characters = Counter(line)
        length = len(line)
        entropy = 0.0

        for count in characters.values():
            probability = count / length
            entropy += probability * math.log2(probability)

        return -entropy