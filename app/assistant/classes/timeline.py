from .placetime import Placetime
import uuid


class Timeline:
    def __init__(self):
        self.uid = uuid.uuid4().hex
        self.placetimes = []

    def addPlacetime(self, pt):
        self.placetimes.append(pt)
