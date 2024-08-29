from .placetime import Placetime
from .core import Core
import uuid


class Timeline(Core):
    def __init__(self):
        self.uid = uuid.uuid4().hex
        self.placetimes = []

    def addPlacetime(self, pt):
        self.placetimes.append(pt)

    def getPlacetime(self, id):
        if id >= len(self.placetimes):
            return None

        return self.placetimes[id]

    def serialize(self):
        to_ret = {"placetimes": []}

        for pt in self.placetimes:
            to_ret["placetimes"].append(pt.serialize())

        return to_ret
