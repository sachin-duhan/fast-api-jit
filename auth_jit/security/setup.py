from fastapi import Request, FastAPI
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from auth_jit.settings import settings
from auth_jit.security.blacklist import backList

def jwt_setup(app: FastAPI):
    # exception handler for authjwt
    # in production, you can tweak performance using orjson response
    @AuthJWT.load_config
    def load_config():
        return settings

    @app.exception_handler(AuthJWTException)
    def authjwt_exception_handler(_, exc: AuthJWTException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message}
        )
    
    # For this example, we are just checking if the tokens jti
    # (unique identifier) is in the denylist set. This could
    # be made more complex, for example storing the token in Redis
    # with the value true if revoked and false if not revoked
    @AuthJWT.token_in_denylist_loader
    def check_if_token_in_denylist(decrypted_token):
        jti = decrypted_token['jti']
        return backList.is_token_invalid(jti)

