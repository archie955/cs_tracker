# This entire router will be refactored into a service layer + router

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from exceptions.app_exceptions import InvalidCredentialsError
from schemas import user_schemas
from utils.steam_login import SteamLogin, SteamValidator

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", status_code=status.HTTP_303_SEE_OTHER, response_class=RedirectResponse)
def login(request: Request):
    url = f"{request.url_for('validate_login')}"
    steam = SteamLogin(url)
    return steam.Redirect()


@router.get(
    "/validatelogin", status_code=status.HTTP_200_OK, response_model=user_schemas.login
)
def validate_login(request: Request):
    validator = SteamValidator()
    steamID = validator.ValidateLogin(request.query_params)

    if not steamID or not isinstance(steamID, str):
        raise InvalidCredentialsError()

    # commit to database when I know what details I actually want

    # update schema when database models completed
    return user_schemas.login(steam_id=steamID)
