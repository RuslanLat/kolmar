import typing

from app.store.database.database import Database

if typing.TYPE_CHECKING:
    from app.web.app import Application


class Store:
    def __init__(self, app: "Application"):
        from app.store.admin.accessor import AdminAccessor
        from app.store.users.accessor import UserAccessor
        from app.store.users.accessor import UserLoginAccessor
        from app.store.roles.accessor import RoleAccessor
        from app.store.positions.accessor import PositionAccessor
        from app.store.departments.accessor import DepartmentAccessor
        from app.store.emails.accessor import EmailAccessor
        from app.store.predicts.accessor import PredictAccessor
        from app.store.ratings.accessor import RatingAccessor
        from app.store.subdivisions.accessor import SubdivisionAccessor

        self.admins = AdminAccessor(app)
        self.users = UserAccessor(app)
        self.user_logins = UserLoginAccessor(app)
        self.roles = RoleAccessor(app)
        self.positions = PositionAccessor(app)
        self.departments = DepartmentAccessor(app)
        self.emails = EmailAccessor(app)
        self.predicts = PredictAccessor(app)
        self.ratings = RatingAccessor(app)
        self.subdivisions = SubdivisionAccessor(app)



def setup_store(app: "Application"):
    app.database = Database(app)
    app.on_startup.append(app.database.connect)
    app.on_cleanup.append(app.database.disconnect)
    app.store = Store(app)
