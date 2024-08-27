class Place:
    def __init__(self, name=None, vague=True):
        self.name = name
        self.vague = vague


class Time:
    def __init__(self, time=None, date=None, vague=None):
        self.time = time
        self.date = date
        self.vague = vague


class Placetime:
    def __init__(self):
        self.uid = None
        self.timeline = None
        self.place = None
        self.time = None

        self.entities = []
        self.actions = []
        self.statements = []

    def setPlace(self, place):
        self.place = place

    def setTime(self, time):
        self.time = time

    def addEntity(self, entity):
        self.entities.append(entity)

    def addAction(self, action):
        self.actions.append(action)

    def addStatement(self, statement):
        self.statement = statement
