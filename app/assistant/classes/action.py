from .core import Core
from .entity import Entity
from app.assistant.classes.engine import get_engine


class Action(Core):
    def __init__(self, order, by, description, to, perspective):
        self.description = description
        self.order = order

        engine = get_engine()

        if type(to) is Entity:
            self.to = to.gid
        elif type(to) is int:
            self.to = engine.getEntityByGid(to)
        else:
            self.to = None

        if type(by) is Entity:
            self.by = by.gid
        elif type(by) is int:
            self.by = engine.getEntityByGid(by)
        else:
            self.by = None

        if type(perspective) is Entity:
            self.perspective = by.gid
        elif type(perspective) is int:
            self.perspective = engine.getEntityByGid(perspective)
        else:
            self.perspective = None

    def setDescription(self, description):
        self.description = description

    def setTo(self, to):
        if type(to) is Entity:
            self.to = to.gid
        else:
            self.to = None

    def setBy(self, by):
        if type(by) is Entity:
            self.by = by.gid
        else:
            self.by = None

    def setOrder(self, order):
        self.order = order

    def serialize(self):
        to_ret = {}
        to_ret["order"] = self.order
        to_ret["description"] = self.description
        to_ret["to"] = self.to.serialize()
        to_ret["by"] = self.by.serialize()
        to_ret["perspective"] = self.perspective.serialize()

        return to_ret
