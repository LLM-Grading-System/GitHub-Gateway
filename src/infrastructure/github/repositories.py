import json

import httpx

from src.infrastructure.github.schemas import RepositoryResponse


# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository
async def get_repository(personal_access_token: str, repo_owner: str, repo_name: str) -> RepositoryResponse:
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'
    headers = {
        'Authorization': f'Bearer {personal_access_token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': "2022-11-28"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
    return RepositoryResponse(**json.loads(response.read()))
