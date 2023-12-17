import typing

from app.roles.views import (
    RoleAddView,
    RoleListView,
    RoleUpdateView,
    RoleDeleteView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/role.add", RoleAddView)
    app.router.add_view("/role.update", RoleUpdateView)
    app.router.add_view("/role.delete", RoleDeleteView)
    app.router.add_view("/role.list", RoleListView)
