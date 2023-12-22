import typing

from app.stimuls.views import (
    StimulAddView,
    StimulListView,
    # StimulDeleteView,
    # StimulListAddView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/stimul.add", StimulAddView)
    # app.router.add_view("/email.delete", StimulDeleteView)
    app.router.add_view("/stimul.list", StimulListView)
    # app.router.add_view("/email.user.list", StimulUserListView)
    # app.router.add_view("/email.add.all", StimulListAddView)
