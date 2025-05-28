from app.adapters.idp import UnauthorizedError
from app.application.errors.common import AccessDeniedError, ApplicationError
from app.application.errors.user_errors import UserDoesNotExistsError


error_code = {
    ApplicationError: 500,
    UserDoesNotExistsError: 404,
    UnauthorizedError: 401,
    AccessDeniedError: 403,
}

error_unique_code = {
    ApplicationError: "APPLICATION_ERROR",
    UserDoesNotExistsError: "USER_DOES_NOT_EXISTS_ERROR",
    UnauthorizedError: "UNAUTHORIZED_ERROR",
    AccessDeniedError: "ACCESS_DENIED_ERROR",
}