from .entity import Entity
from .core import Core


class Statement(Core):
    def __init__(
        self,
        by=None,
        description="",
        perspective=None,
        thought=False,
        about=None,
        vague=True,
    ):
        self.description = description
        self.order = None
        self.thought = thought
        self.vague = vague

        if type(about) is Entity:
            self.about = about.gid
        else:
            self.about = None

        if type(by) is Entity:
            self.by = by.gid
        else:
            self.by = None

        if type(perspective) is Entity:
            self.perspective = perspective.gid
        else:
            self.perspective = None

    def setDescription(self, description):
        self.description = description

    def setOrder(self, order):
        self.order = order

    def setThought(self, thought):
        self.thought = thought

    def setAbout(self, about):
        if type(about) is Entity:
            self.about = about.gid
        else:
            self.about = None

    def setBy(self, by):
        if type(by) is Entity:
            self.by = by.gid
        else:
            self.by = None

    def setPerspective(self, perspective):
        if type(perspective) is Entity:
            self.perspective = perspective.gid
        else:
            self.perspective = None

    def serialize(self):
        to_ret = {}
        to_ret["order"] = self.order
        to_ret["description"] = self.description
        to_ret["thought"] = self.thought
        to_ret["vague"] = self.vague
        to_ret["by"] = self.by
        to_ret["perspective"] = self.perspective
        to_ret["about"] = self.about

        return to_ret
