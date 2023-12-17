from typing import List, Optional
from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import joinedload
from app.departments.models import (
    Department,
    DepartmentModel,
    DepartmentBot,
    DepartmentBotModel,
)
from app.base.base_accessor import BaseAccessor


class DepartmentAccessor(BaseAccessor):
    async def create_department(
        self, department: str, email: str, telegram_id: int
    ) -> Optional[Department]:
        new_department: DepartmentModel = DepartmentModel(
            department=department, email=email, telegram_id=telegram_id
        )

        async with self.app.database.session.begin() as session:
            session.add(new_department)

        return Department(
            department_id=new_department.department_id,
            department=new_department.department,
            email=new_department.email,
            telegram_id=new_department.telegram_id,
        )

    async def create_boot_department(
        self, department_id: int, telegram_id: int
    ) -> Optional[DepartmentBot]:
        new_department: DepartmentBotModel = DepartmentBotModel(
            department_id=department_id, telegram_id=telegram_id
        )

        async with self.app.database.session.begin() as session:
            session.add(new_department)

        return DepartmentBot(
            department_id=new_department.department_id,
            telegram_id=new_department.telegram_id,
            link=new_department.link,
        )

    async def update_department_telegram_id(
        self, department_id: int, telegram_id: int
    ) -> Optional[Department]:
        query = (
            update(DepartmentModel)
            .where(DepartmentModel.department_id == department_id)
            .values(telegram_id=telegram_id)
            .returning(DepartmentModel)
        )

        async with self.app.database.session.begin() as session:
            department: DepartmentModel = await session.scalar(query)

        if not department:
            return None

        return Department(
            department_id=department.department_id,
            department=department.department,
            email=department.email,
            telegram_id=department.telegram_id,
        )

    async def update_boot_department(
        self, department_id: int, telegram_id: int
    ) -> Optional[DepartmentBot]:
        query = (
            update(DepartmentBotModel)
            .where(DepartmentBotModel.department_id == department_id)
            .values(telegram_id=telegram_id)
            .returning(DepartmentBotModel)
        )

        async with self.app.database.session.begin() as session:
            department: DepartmentBotModel = await session.scalar(query)

        if not department:
            return None

        return DepartmentBot(
            department_id=department.department_id,
            telegram_id=department.telegram_id,
            link=department.link,
        )

    async def get_id_department(self, department: str) -> Optional[Department]:
        query = select(DepartmentModel).where(DepartmentModel.department == department)

        async with self.app.database.session.begin() as session:
            department: DepartmentModel = await session.scalar(query)

        if not department:
            return None

        return Department(
            department_id=department.department_id,
            department=department.department,
            email=department.email,
            telegram_id=department.telegram_id,
        )

    async def delete_department(self, department: str) -> Optional[Department]:
        query = (
            delete(DepartmentModel)
            .where(DepartmentModel.department == department)
            .returning(DepartmentModel)
        )

        async with self.app.database.session.begin() as session:
            department: DepartmentModel = await session.scalar(query)

        if not department:
            return None

        return Department(
            department_id=department.department_id,
            department=department.department,
            email=department.email,
            telegram_id=department.telegram_id,
        )

    async def list_departments(self) -> List[Optional[Department]]:
        query = select(DepartmentModel)

        async with self.app.database.session() as session:
            departments: List[DepartmentModel] = await session.scalars(query)

        if not departments:
            return []

        return [
            Department(
                department_id=department.department_id,
                department=department.department,
                email=department.email,
                telegram_id=department.telegram_id,
            )
            for department in departments.all()
        ]
