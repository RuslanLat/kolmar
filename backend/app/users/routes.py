import typing

from app.users.views import (
    UserLoginCurrentView,
    UserLoginAddView,
    UserLoginUpdateView,
    UserLoginDeleteView,
    UserLoginListView,
    UserAddView,
    UserDeleteView,
    UserListView,
    UserUpdateView,
    UserInsertAddView,
    UserFullListView,
    UserBotFullListView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    from app.users.views import UserLoginView

    app.router.add_view("/user.login", UserLoginView)
    app.router.add_view("/user.login.current", UserLoginCurrentView)
    app.router.add_view("/user.login.add", UserLoginAddView)
    app.router.add_view("/user.login.update", UserLoginUpdateView)
    app.router.add_view("/user.login.delete", UserLoginDeleteView)
    app.router.add_view("/user.login.list", UserLoginListView)
    app.router.add_view("/user.add", UserAddView)
    app.router.add_view("/user.update", UserUpdateView)
    app.router.add_view("/user.delete", UserDeleteView)
    app.router.add_view("/user.list", UserListView)
    app.router.add_view("/user.insert.add", UserInsertAddView)
    app.router.add_view("/user.full.list", UserFullListView)
    app.router.add_view("/user.full.bot.list", UserBotFullListView)
