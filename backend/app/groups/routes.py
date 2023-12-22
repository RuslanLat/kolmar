import typing

from app.groups.views import (
    GroupAddView,
    GroupListView,
    GroupDeleteView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/group.add", GroupAddView)
    app.router.add_view("/group.delete", GroupDeleteView)
    app.router.add_view("/group.list", GroupListView)
