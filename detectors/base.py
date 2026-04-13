class BaseDetector:
    def __init__(self):
        pass

    def detect(self, image):
        raise NotImplementedError('Every detector must implement detect!')