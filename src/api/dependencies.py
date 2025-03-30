from __future__ import annotations

from typing import Annotated

from fastapi import Depends

from src.services.comment import CommentService as CommentServiceClass
from src.settings import app_settings


def get_comment_service() -> CommentServiceClass:
    return CommentServiceClass(
        app_settings.GITHUB_APPS_PRIVATE_KEY_PATH,
        app_settings.GITHUB_APPS_CLIENT_ID,
    )


CommentService = Annotated[CommentServiceClass, Depends(get_comment_service)]
