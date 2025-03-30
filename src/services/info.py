from pydantic import HttpUrl

from src.infrastructure.github import get_repository
from src.services.exceptions import NoParentRepositoryError


class InfoService:
    def __init__(self, personal_access_token: str):
        self.personal_access_token = personal_access_token

    async def get_repository_urls(self, username: str, repo_name: str) -> tuple[HttpUrl, HttpUrl]:
        repo = await get_repository(self.personal_access_token, username, repo_name)
        if not repo.parent:
            raise NoParentRepositoryError(f"Репозиторий {repo.svn_url} не является форком")
        current_repo_url = repo.svn_url
        parent_repo_url = repo.parent.svn_url
        return current_repo_url, parent_repo_url
