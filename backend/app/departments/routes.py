import typing

from app.departments.views import (
    DepartmentAddView,
    DepartmentListView,
    DepartmentDeleteView,
    DepartmentBotUpdateView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/department.add", DepartmentAddView)
    app.router.add_view("/department.delete", DepartmentDeleteView)
    app.router.add_view("/department.list", DepartmentListView)
    app.router.add_view("/department.bot.update", DepartmentBotUpdateView)
