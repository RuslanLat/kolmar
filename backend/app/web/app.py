from typing import Optional, Dict
from aiohttp.web import (
    Application as AiohttpApplication,
    Request as AiohttpRequest,
    View as AiohttpView,
)
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp_session import setup as session_setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from app.admin.models import Admin
from app.users.models import User
from app.store import Store, setup_store
from app.store.database.database import Database
from app.web.config import Config, setup_config
from app.web.logger import setup_logging
from app.web.middlewares import setup_middlewares
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    config: Optional[Config] = None
    store: Optional[Store] = None
    database: Optional[Database] = None


class Request(AiohttpRequest):
    user: dict
    admin: Optional[Admin] = None
    user: Optional[User] = None

    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def database(self):
        return self.request.app.database

    @property
    def store(self) -> Store:
        return self.request.app.store

    @property
    def data(self) -> dict:
        return self.request.get("data", {})


app = Application()

description = """

KOLMAR HR API

Сервис прогнозирования увольнения на основе вовлеченности сотрудника


## Разработчик

* Руслан Латипов, @rus_lat116

"""

tags_metadata = [
    {
        "name": "admin",
        "description": "Аутентификация админа",
    },
    {
        "name": "user_logins",
        "description": "Аутентификация пользователей",
    },
    {
        "name": "users",
        "description": "Добавление/удаление пользователей",
    },
    {
        "name": "roles",
        "description": "Добавление/удаление ролей",
    },
    {
        "name": "positions",
        "description": "Добавление/удаление должностей",
    },
    {
        "name": "departments",
        "description": "Добавление/удаление отделов",
    },
    {
        "name": "subdivisions",
        "description": "Добавление/удаление подразделений",
    },
    {
        "name": "emails",
        "description": "Добавление/удаление электронных писем",
    },
    {
        "name": "predicts",
        "description": "Добавление/удаление предсказаний модели",
    },
    {
        "name": "ratings",
        "description": "Добавление/удаление рейтенга сотрудников",
    },
    {
        "name": "groups",
        "description": "Добавление/удаление групп для А/В тестов",
    },
    {
        "name": "stimuls",
        "description": "Добавление/удаление результатов беседы",
    },
]


def setup_app(config_path: str) -> Application:
    setup_logging(app)
    setup_config(app, config_path)
    session_setup(app, EncryptedCookieStorage(app.config.session.key))
    setup_routes(app)
    setup_aiohttp_apispec(
        app,
        title="KOLMAR HR API",
        version="0.0.1",
        swagger_path="/docs",
        url="/docs/json",
        info=dict(
            description=description,
            contact={
                "name": "Руслан Латипов",
                "url": "https://t.me/rus_lat116",
                "email": "rus_kadr03@mail.ru",
            },
        ),
        tags=tags_metadata,
    )
    setup_middlewares(app)
    setup_store(app)


    
    return app
