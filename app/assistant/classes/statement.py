from .entity import Entity
from .core import Core
from app.assistant.classes.engine import get_engine


class Statement(Core):
    def __init__(
        self,
        order,
        by=None,
        description="",
        perspective=None,
        thought=False,
        about=None,
        vague=True,
    ):
        self.description = description
        self.order = order
        self.thought = thought
        self.vague = vague

        engine = get_engine()

        if type(about) is Entity:
            self.about = about.gid
        elif type(about) is int:
            self.about = engine.getEntityByGid(about)
        else:
            self.about = None

        if type(by) is Entity:
            self.by = by.gid
        elif type(by) is int:
            self.by = engine.getEntityByGid(by)
        else:
            self.by = None

        if type(perspective) is Entity:
            self.perspective = perspective.gid
        elif type(perspective) is int:
            self.perspective = engine.getEntityByGid(perspective)
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
        elif type(about) is int:
            self.about = get_engine().getEntityByGid(about)
        else:
            self.about = None

    def setBy(self, by):
        if type(by) is Entity:
            self.by = by.gid
        elif type(by) is int:
            self.by = get_engine().getEntityByGid(by)
        else:
            self.by = None

    def setPerspective(self, perspective):
        if type(perspective) is Entity:
            self.perspective = perspective.gid
        elif type(perspective) is int:
            self.perspective = get_engine().getEntityByGid(perspective)
        else:
            self.perspective = None

    def serialize(self):
        to_ret = {}
        to_ret["order"] = self.order
        to_ret["description"] = self.description
        to_ret["thought"] = self.thought
        to_ret["vague"] = self.vague
        to_ret["by"] = self.by.serialize()
        to_ret["perspective"] = self.perspective.serialize()
        to_ret["about"] = self.about.serialize()

        return to_ret
