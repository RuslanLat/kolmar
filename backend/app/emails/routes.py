import typing

from app.emails.views import (
    EmailAddView,
    EmailListView,
    EmailDeleteView,
    EmailUserListView,
    EmailListAddView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/email.add", EmailAddView)
    app.router.add_view("/email.delete", EmailDeleteView)
    app.router.add_view("/email.list", EmailListView)
    app.router.add_view("/email.user.list", EmailUserListView)
    app.router.add_view("/email.add.all", EmailListAddView)
