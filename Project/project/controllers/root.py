from project.lib.base import BaseController
from tg import expose


class RootController(BaseController):

    @expose()
    def index(self):
        return "<h1>Hello World</h1>"

    @expose()
    def _default(self, *args, **kw):
        return "This page is not ready"

    @expose("project.templates.index")
    def index(self):
        return {}

    @expose("project.templates.facultet")
    def facultet(self):
        return {}

    @expose("project.templates.kafedra")
    def kafedra(self):
        return {}

    @expose("project.templates.teacher")
    def teacher(self):
        return {}

    @expose("project.templates.discipline")
    def discipline(self):
        return {}

    @expose("project.templates.academicLoad")
    def academicLoad(self):
        return {}

    @expose("project.templates.account")
    def account(self):
        return {}

    @expose("project.templates.autenfication")
    def autenfication(self):
        return {}

    @expose("project.templates.backUp")
    def backUp(self):
        return {}
