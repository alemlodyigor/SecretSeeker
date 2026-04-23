import pytest
from detectors.regex_detectors import RegexDetector
from detectors.entropy_detector import EntropyDetector

def test_entropy_detector():
    detector = EntropyDetector()
    line = '533lknikodujhdfgb98NIKKLK3452sdzf'
    results = detector.detect(line)

    assert len(results) > 0
    assert results[0]['entropy'] >= 3.5

def test_entropy_detector_negative():
    detector = EntropyDetector()
    line = 'This line does not contain any secrets.'
    results = detector.detect(line)
    assert len(results) == 0

def test_regex_detector_aws():
    detector = RegexDetector()

    line = "My secret key is AKIAIOSFODNN7EXAMPLE"

    results = detector.detect(line)

    assert len(results) > 0

    assert results[0]['type'] == 'AWS Access Key'
    assert results[0]['value'] == 'AKIAIOSFODNN7EXAMPLE'

def test_regex_detector_negative():
    detector = RegexDetector()

    line = 'This line does not contain any secrets.'
    results = detector.detect(line)

    assert len(results) == 0