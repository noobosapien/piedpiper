from .core import Core


class Entity(Core):
    def __init__(self, gid, name="", main=False, multiple=False):
        self.uid = None
        self.gid = gid
        self.name = name
        self.general = None
        self.main = main
        self.relation = None
        self.multiple = multiple

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

    def serialize(self):
        to_ret = {}

        to_ret["gid"] = self.gid
        to_ret["name"] = self.name
        to_ret["main"] = self.main
        to_ret["multiple"] = self.multiple

        return to_ret
