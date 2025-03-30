import httpx


async def comment_on_pull_request(repo_owner: str, repo_name: str, pull_request_number: int, installation_access_token: str, comment: str) -> None:
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pull_request_number}/comments'
    headers = {
        'Authorization': f'token {installation_access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'body': comment
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
