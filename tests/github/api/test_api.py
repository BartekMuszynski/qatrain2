import requests
from src.config.config import *
from src.applications.github.api.github_api import GitHubAPI


def test_search_for_existing_repo():
    github_api_client = GitHubAPI()
    existing_repo_name = "sergii"
    repos = github_api_client.search_repo(existing_repo_name)
    assert repos['total_count'] != 0

def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPI()
    nonexisting_repo_name = "asbhfhassfak"
    repos = github_api_client.search_repo(nonexisting_repo_name)
    assert repos['total_count'] == 0
