from fastapi import APIRouter

from auth_jit.web.common.response import ApiResponse

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    return ApiResponse()
