
class TokenNotFound(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class ValidationError(Exception):
    pass

class NotAcceptableError(Exception):
    pass

class ForbiddenError(Exception):
    pass

class NotFoundError(Exception):
    pass

class InvalidEventError(Exception):
    pass

Errors = {
    401: UnauthorizedError,
    422: ValidationError,
    406: NotAcceptableError,
    403: ForbiddenError,
    404: NotFoundError
}
