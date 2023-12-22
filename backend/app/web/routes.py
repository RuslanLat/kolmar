from aiohttp.web_app import Application


def setup_routes(app: Application):
    from app.admin.routes import setup_routes as admin_setup_routes
    from app.users.routes import setup_routes as user_setup_routes
    from app.roles.routes import setup_routes as role_setup_routes
    from app.positions.routes import setup_routes as position_setup_routes
    from app.departments.routes import setup_routes as department_setup_routes
    from app.subdivisions.routes import setup_routes as subdivision_setup_routes
    from app.emails.routes import setup_routes as email_setup_routes
    from app.predicts.routes import setup_routes as predict_setup_routes
    from app.ratings.routes import setup_routes as rating_setup_routes
    from app.groups.routes import setup_routes as group_setup_routes
    from app.stimuls.routes import setup_routes as stimul_setup_routes
    from app.web import views

    admin_setup_routes(app)
    user_setup_routes(app)
    role_setup_routes(app)
    position_setup_routes(app)
    department_setup_routes(app)
    subdivision_setup_routes(app)
    email_setup_routes(app)
    predict_setup_routes(app)
    rating_setup_routes(app)
    group_setup_routes(app)
    stimul_setup_routes(app)
    app.router.add_get("/", views.index, name="home")
