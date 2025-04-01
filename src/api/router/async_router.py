from src.api.dependencies import CommentService
from src.api.events import NewCommentEventSchema, NEW_COMMENT_TOPIC, NEW_COMMENT_CONSUMER_GROUP, COMMENT_CREATED_TOPIC, \
    CommentCreatedEventSchema
from src.infrastructure.faststream.router import create_faststream_router

async_router = create_faststream_router()


@async_router.subscriber(NEW_COMMENT_TOPIC, group_id=NEW_COMMENT_CONSUMER_GROUP, auto_commit=False)
@async_router.publisher(COMMENT_CREATED_TOPIC)
async def comment_and_notify(data: NewCommentEventSchema, comment_service: CommentService):
    await comment_service.add_comment(data.username, data.repo_name, data.pull_request_number, data.comment)
    pull_request_link = f"https://github.com/{data.username}/{data.repo_name}/pull/{data.pull_request_number}"
    return CommentCreatedEventSchema(username=data.username, pull_request_link=pull_request_link)
