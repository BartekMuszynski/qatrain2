import pytest
from src.applications.github.api.github_api import GitHubAPI


@pytest.fixture(scope='session')
def git_api_client():
    github_api_client = GitHubAPI()
    yield github_api_client

