from fastapi import APIRouter

from auth_jit.web.api.echo.schema import Message
from auth_jit.web.common.response import ApiResponse

router = APIRouter()


@router.post("/", response_model=Message)
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    return ApiResponse(content=incoming_message)
