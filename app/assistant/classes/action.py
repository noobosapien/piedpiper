from .core import Core
from .entity import Entity


class Action(Core):
    def __init__(self, by, description, to, perspective):
        self.description = description
        self.order = None

        if type(to) is Entity:
            self.to = to.gid
        else:
            self.to = None

        if type(by) is Entity:
            self.by = by.gid
        else:
            self.by = None

        if type(perspective) is Entity:
            self.perspective = by.gid
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
        to_ret["to"] = self.to
        to_ret["by"] = self.by
        to_ret["perspective"] = self.perspective

        return to_ret
