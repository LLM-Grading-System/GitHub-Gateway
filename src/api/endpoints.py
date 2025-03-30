from fastapi import APIRouter, Body

from src.api.dependencies import CommentService
from src.api.schemas import CreateCommentRequest
from src.api.general_schemas import SuccessResponse

router = APIRouter(tags=["github"], prefix="/github")


@router.post("/comment", response_model=SuccessResponse)
async def create_comment(comment_service: CommentService, data: CreateCommentRequest = Body()):
    await comment_service.add_comment(
        data.username,
        data.repo_name,
        data.pull_request_number,
        data.comment,
    )
    return SuccessResponse(message="Комментарий успешно добавлен")