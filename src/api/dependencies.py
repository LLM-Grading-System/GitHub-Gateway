from typing import Annotated

from fastapi import Depends

from src.services.comment import CommentService as CommentServiceClass
from src.services.info import InfoService as InfoServiceClass
from src.settings import app_settings


def get_comment_service() -> CommentServiceClass:
    return CommentServiceClass(
        app_settings.GITHUB_APPS_PRIVATE_KEY_PATH,
        app_settings.GITHUB_APPS_CLIENT_ID,
    )


def get_info_service() -> InfoServiceClass:
    return InfoServiceClass(
        app_settings.GITHUB_PERSONAL_ACCESS_TOKEN,
    )


CommentService = Annotated[CommentServiceClass, Depends(get_comment_service)]
InfoService = Annotated[InfoServiceClass, Depends(get_info_service)]
