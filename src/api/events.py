from pydantic import BaseModel, Field

from src.api.schema.github import CreateCommentRequest


NEW_COMMENT_TOPIC = "new_comment"
NEW_COMMENT_CONSUMER_GROUP = "new_comment_group"


class NewCommentEventSchema(CreateCommentRequest):
    ...


COMMENT_CREATED_TOPIC = "comment_created"
COMMENT_CREATED_CONSUMER_GROUP = "comment_created_group"


class CommentCreatedEventSchema(BaseModel):
    username: str = Field(examples=["octocat"])
    pull_request_link: str = Field(examples=["/pull_request/1"])
