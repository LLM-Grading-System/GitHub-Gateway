import json

import httpx

from src.infrastructure.github.schemas import Installation, TokenResponse


# https://docs.github.com/ru/rest/apps/apps?apiVersion=2022-11-28#list-installations-for-the-authenticated-app
async def get_app_installations(signed_jwt: str) -> list[Installation]:
    url = "https://api.github.com/app/installations"
    headers = {
        "Authorization": f"Bearer {signed_jwt}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
    return [Installation(**data) for data in json.loads(response.read())]


# https://docs.github.com/ru/rest/apps/apps?apiVersion=2022-11-28#create-an-installation-access-token-for-an-app
async def get_access_token_by_installation_id(signed_jwt: str, installation_id: int) -> TokenResponse:
    url = f'https://api.github.com/app/installations/{installation_id}/access_tokens'
    headers = {
        'Authorization': f'Bearer {signed_jwt}',
        'Accept': 'application/vnd.github.v3+json'
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers)
        response.raise_for_status()
    return TokenResponse(**json.loads(response.read()))
