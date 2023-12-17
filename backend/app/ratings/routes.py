import typing

from app.ratings.views import (
    RatingAddView,
    RatingListView,
    RatingDeleteView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/rating.add", RatingAddView)
    app.router.add_view("/rating.delete", RatingDeleteView)
    app.router.add_view("/rating.list", RatingListView)