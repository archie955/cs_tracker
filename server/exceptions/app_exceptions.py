class AppException(Exception):
    def __init__(
        self, status_code: int, message: str, headers: dict[str, str] | None = None
    ):
        self.status_code = status_code
        self.message = message
        self.headers = headers
        super().__init__(message)


class InvalidCredentialsError(AppException):
    def __init__(self, headers: dict[str, str] | None = None):
        super().__init__(
            status_code=401, message="Invalid credentials provided", headers=headers
        )
