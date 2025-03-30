class ServiceError(Exception):
    message: str


class UserDoesntInstallAppError(ServiceError):
    ...

class NoParentRepositoryError(ServiceError):
    ...
