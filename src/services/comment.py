from src.infrastructure.github import get_signed_jwt_token, get_access_token_by_installation_id, get_app_installations, comment_on_pull_request
from src.services.exceptions import UserDoesntInstallAppError


class CommentService:
    def __init__(self, secret_key_path: str, client_id: str):
        self.jwt_token = get_signed_jwt_token(secret_key_path, client_id)

    async def add_comment(self, username: str, repo_name: str, pull_request_number: int, comment: str) -> None:
        installations = await get_app_installations(self.jwt_token)
        installation_id = self._find_installation_id_by_login(installations, username)
        token_data = await get_access_token_by_installation_id(self.jwt_token, installation_id)
        installation_access_token = token_data.token
        await comment_on_pull_request(username, repo_name, pull_request_number, installation_access_token, comment)

    @staticmethod
    def _find_installation_id_by_login(installations, login: str) -> int:
        installation_id = None
        for installation in installations:
            if installation.account.login == login:
                installation_id = installation.id
        if not installation_id:
            raise UserDoesntInstallAppError(f"Пользователь {login} не подключил Github Apps к репозиторию")
        return installation_id
