from fastapi import APIRouter, Request, Depends, status

from core.api.schemas.schemas import MessageForm
from core.api.dependencies.depends import get_message_repository

router = APIRouter()


@router.post("/send_message", status_code=status.HTTP_200_OK)
async def send_user(
    request: Request, form: MessageForm, repository=Depends(get_message_repository)
):
    if await repository.send_message(
        request=request, name=form.name, message=form.message
    ):
        return {"status": status.HTTP_200_OK, "message": "Message sent"}

    return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Internal server error"}
