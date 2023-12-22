from typing import List, Optional
from datetime import datetime
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.stimuls.schemes import (
    StimulRequestSchema,
    StimulResponseSchema,
    # StimulDeleteRequestSchema,
    # StimulUserRequestSchema,
    StimulListResponseSchema,

)
from app.web.app import View
from app.web.mixins import (
    AuthRequiredMixin,
    AuthUserRequiredMixin,
)
from app.web.utils import json_response
from app.stimuls.models import Stimul


class StimulAddView(AuthUserRequiredMixin, View):
    @request_schema(StimulRequestSchema)
    @response_schema(StimulResponseSchema, 200)
    @docs(
        tags=["stimuls"],
        summary="Add stimul add view",
        description="Add stimul to database",
    )
    async def post(self) -> Response:
        name: str = self.data["name"]
        lastname: str = self.data["lastname"]
        q1: str = self.data["q1"]
        q2: str = self.data["q2"]
        q3: str = self.data["q3"]
        q4: str = self.data["q4"]
        q5: str = self.data["q5"]
        q6: str = self.data["q6"]
        q7: str = self.data["q7"]
        q8: str = self.data["q8"]
        q9: str = self.data["q9"]
        q10: str = self.data["q10"]
        q11: str = self.data["q11"]
        
        user = await self.store.users.get_by_full_name(name=name, lastname=lastname)

        try:
            stimul: Stimul = await self.store.stimuls.create_stimul(
                user_id=user.id,
                q1=q1,
                q2=q2,
                q3=q3,
                q4=q4,
                q5=q5,
                q6=q6,
                q7=q7,
                q8=q8,
                q9=q9,
                q10=q10,
                q11=q11,
            )

        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=StimulResponseSchema().dump(stimul))



# class EmailDeleteView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
#     @request_schema(EmailDeleteRequestSchema)
#     @response_schema(EmailResponseSchema, 200)
#     @docs(
#         tags=["emails"],
#         summary="Add email delete view",
#         description="Delete email from database",
#     )
#     async def get(self) -> Response:
#         row_id: int = self.data["row_id"]
#         email: Email = await self.store.emails.delete_email(row_id=row_id)

#         return json_response(EmailResponseSchema().dump(email))


class StimulListView(AuthUserRequiredMixin, View):  # AuthRequiredMixin,
    @response_schema(StimulListResponseSchema, 200)
    @docs(
        tags=["stimuls"],
        summary="Add stimul list view",
        description="Get list stimuls from database",
    )
    async def get(self) -> Response:
        stimuls: List[Optional[Stimul]] = await self.store.stimuls.list_stimuls()
        return json_response(StimulListResponseSchema().dump({"stimuls": stimuls}))
