
from fastapi import status
from fastapi.responses import RedirectResponse

""" The example URL from csstats.gg
https://steamcommunity.com/openid/login?
openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&
openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&
openid.mode=checkid_setup&
openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&
openid.realm=https%3A%2F%2Fcsstats.gg&
openid.return_to=https%3A%2F%2Fcsstats.gg%2Flogin%2Ffc815c99369f80f3f4ff9d9a9498da915fa85b6f%2Freturn
"""


class SteamLogin:
    def __init__(self, home_url: str):
        self.__baseurl = "https://steamcommunity.com/openid/login?"
        self.__params = {
            "openid.claimed_id": "https://specs.openid.net/auth/2.0/identifier_select",
            "openid.identity": "http://specs.openid.net/auth/2.0/identifier_select",
            "openid.mode": "checkid_setup",
            "openid.ns": "http://specs.openid.net/auth/2.0",
            "openid.realm": home_url,
            "openid.return_to": home_url,
        }
        self.__validationParams = {}

    def __createUrl(self) -> str:
        return "%s?%s"

    def __redirect(self) -> RedirectResponse:
        url = self.__createUrl()
        response = RedirectResponse(
            url=url,
            status_code=status.HTTP_303_SEE_OTHER,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        return response

    def __validateLogin(self, data):
        pass

    def login(self):
        pass
