from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from auth_jit.models.user import User
from auth_jit.security.blacklist import backList
from auth_jit.web.common.response import ApiResponse

router = APIRouter()

# provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token to use authorization
# later in endpoint protected
@router.post("/login")
async def login(user: User, Authorize: AuthJWT = Depends()):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.username)
    return ApiResponse(content={"access_token": access_token})


@router.post("/refresh")
async def refresh(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    access_token = Authorize.create_access_token(subject=current_user, fresh=True)
    refresh_token = Authorize.create_refresh_token(subject=current_user)
    return ApiResponse(
        content={"access_token": access_token, "refresh_token": refresh_token},
    )


# Endpoint for revoking the current users access token
@router.delete("/revoke")
async def access_revoke(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    jti = Authorize.get_raw_jwt()["jti"]
    backList.invalidate_token(jti)
    return ApiResponse(content=None, message="Access token has been revoke")
