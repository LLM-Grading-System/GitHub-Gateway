from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl


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

#get-a-repository
class Owner(BaseModel):
    login: str
    id: int

class ParentRepository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    owner: Owner
    private: bool
    html_url: HttpUrl
    description: Optional[str]
    fork: bool
    svn_url: HttpUrl
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: bool
    topics: List[str]
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    archived: bool
    disabled: bool
    visibility: str
    pushed_at: datetime
    created_at: datetime
    updated_at: datetime

class RepositoryResponse(BaseModel):
    id: int
    name: str
    full_name: str
    owner: Owner
    private: bool
    description: Optional[str]
    fork: bool
    svn_url: HttpUrl
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    open_issues: int
    is_template: bool
    topics: List[str]
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    has_discussions: bool
    archived: bool
    disabled: bool
    visibility: str
    pushed_at: datetime
    created_at: datetime
    updated_at: datetime
    subscribers_count: int
    network_count: int
    parent: Optional[ParentRepository]
