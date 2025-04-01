from fastapi import APIRouter, Body, Path

from src.api.dependencies import CommentService, InfoService
from src.api.schema.github import CreateCommentRequest, RepositoryInfoResponse

from src.api.schema.general import SuccessResponse

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


@router.get("/repositories/{owner}/{repo_name}", response_model=RepositoryInfoResponse)
async def get_parent_and_current_repo(info_service: InfoService, owner: str = Path(), repo_name: str = Path()):
    current_repo_url, parent_repo_url = await info_service.get_repository_urls(owner, repo_name)
    return RepositoryInfoResponse(
        current_repo_url=str(current_repo_url),
        parent_repo_url=str(parent_repo_url),
    )
