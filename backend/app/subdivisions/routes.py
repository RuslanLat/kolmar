import typing

from app.subdivisions.views import (
    SubdivisionAddView,
    SubdivisionListView,
    SubdivisionDeleteView,
    SubdivisionBotUpdateView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/subdivision.add", SubdivisionAddView)
    app.router.add_view("/subdivision.delete", SubdivisionDeleteView)
    app.router.add_view("/subdivision.list", SubdivisionListView)
    app.router.add_view("/subdivision.bot.update", SubdivisionBotUpdateView)
