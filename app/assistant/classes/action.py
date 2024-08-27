class Action:
    def __init__(self):
        self.description = None
        self.to_entity = False
        self.to = None
        self.by = None

    def setDescription(self, description):
        self.description = description

    def setToEntity(self, entity):
        self.to_entity = entity

    def setTo(self, to):
        self.to = to

    def setBy(self, by):
        self.by = by
