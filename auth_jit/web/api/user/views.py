from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from auth_jit.web.common.response import ApiResponse

router = APIRouter()

# protect endpoint with function jwt_required(), which requires
# a valid access token in the request headers to access.
@router.get("/")
async def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return ApiResponse({"user": current_user})
