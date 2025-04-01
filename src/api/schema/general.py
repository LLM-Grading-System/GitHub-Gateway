from pydantic import Field, BaseModel


class ErrorResponse(BaseModel):
    message: str = Field(examples=["Произошла ошибка при обработке запроса"])


class SuccessResponse(BaseModel):
    message: str = Field(examples=["Операция успешно выполнена"])
