from pydantic import BaseModel, Field


class CreateCommentRequest(BaseModel):
    username: str = Field(examples=["octocat"])
    repo_name: str = Field(examples=["task-1"])
    pull_request_number: int = Field(examples=[1])
    comment: str = Field(examples=["Хорошая работа"])


class RepositoryInfoResponse(BaseModel):
    current_repo_url: str = Field(examples=["https://github.com/LLM-Grading-System/GitHub-Gateway"])
    parent_repo_url: str = Field(examples=["https://github.com/LLM-Grading-System/GitHub-Gateway"])
