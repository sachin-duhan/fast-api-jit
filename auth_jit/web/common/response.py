from fastapi.responses import JSONResponse
from starlette import status


def did_success(status_code: int) -> bool:
    """
    Function to classify a status code as success or not.

    Args:
        status_code (int): The HTTP status code.

    Returns:
        bool: True if status code represents success, False otherwise.
    """
    return (
        status_code >= status.HTTP_200_OK and status_code < status.HTTP_400_BAD_REQUEST
    )


class ApiResponse(JSONResponse):
    def __init__(self, content=None, status_code=status.HTTP_200_OK, **kwargs):
        formatted_content = {
            "success": kwargs.get(
                "success",
                did_success(status_code),
            ),  # Default to True if not provided
            "data": content,
            "message": kwargs.get("message", "ok"),  # Default message if not provided
            "meta": kwargs.get("meta", {}),
        }

        super().__init__(content=formatted_content, status_code=status_code)
