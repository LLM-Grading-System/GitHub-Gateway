from pydantic import BaseModel, Field


class CreateCommentRequest(BaseModel):
    username: str = Field(examples=["octocat"])
    repo_name: str = Field(examples=["task-1"])
    pull_request_number: int = Field(examples=[1])
    comment: str = Field(examples=["Хорошая работа"])
