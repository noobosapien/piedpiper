class Entity:
    def __init__(self):
        self.uid = None
        self.name = None
        self.general = None
        self.main = None
        self.relation = None
        self.single = True

        self.statements = []
        self.actions_to = []
        self.actions_from = []
        self.related_entities = []

    def setName(self, name):
        self.name = name

    def setGeneral(self, general):
        self.general = general

    def setMain(self, main):
        self.main = main

    def setRelation(self, relation):
        self.relation = relation

    def setSingle(self, single):
        self.single = single

    def addStatement(self, statement):
        self.statements.append(statement)

    def addActionTo(self, action):
        self.actions_to.append(action)

    def addActionFrom(self, action):
        self.actions_from.append(action)

    def addRelatedEntities(self, entity):
        self.related_entities.append(entity)
