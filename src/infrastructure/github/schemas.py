from datetime import datetime
from typing import List

from pydantic import BaseModel

# list-installations-for-the-authenticated-app
class Account(BaseModel):
    login: str

class Installation(BaseModel):
    id: int
    account: Account
    app_id: int

#create-an-installation-access-token-for-an-app
class Owner(BaseModel):
    login: str
    id: int

class Permission(BaseModel):
    contents: str
    metadata: str
    pull_requests: str
    repository_custom_properties: str

class TokenResponse(BaseModel):
    token: str
    expires_at: datetime
    permissions: Permission
