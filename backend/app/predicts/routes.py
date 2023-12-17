import typing

from app.predicts.views import (
    PredictAddView,
    PredictListView,
    PredictDeleteView,
    PredictListAddView
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/predict.add", PredictAddView)
    app.router.add_view("/predict.delete", PredictDeleteView)
    app.router.add_view("/predict.list", PredictListView)
    app.router.add_view("/predict.add.all", PredictListAddView)
