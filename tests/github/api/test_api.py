import requests
from src.config.config import *
from src.applications.github.api.github_api import GitHubAPI


def test_search_for_existing_repo():
    github_api_client = GitHubAPI()
    existing_repo_name = "tic_tac_toee"
    repos = github_api_client.search_repo(existing_repo_name)
    assert repos['total_count'] != 0

def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPI()
    nonexisting_repo_name = "asbhfhassfak"
    repos = github_api_client.search_repo(nonexisting_repo_name)
    assert repos['total_count'] == 0

def test_search_for_existing_branch():
    github_api_client = GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    existing_branch_name = "master"
    list_of_branches = github_api_client.search_branches(owner,repo)
    assert existing_branch_name in list_of_branches


def test_search_for_nonexisting_branches():
    github_api_client = GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    existing_branch_name = "masterr"
    list_of_branches = github_api_client.search_branches(owner,repo)
    assert existing_branch_name not in list_of_branches

def test_branch_rename():
    github_api_client =GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    branch = "develop"
    new_name = "develop_changed"
    call = github_api_client.rename_branch(owner,repo,branch,new_name)
    # according to documentation changing branch name by api call may take some time so the only instant way of checking if the operation was 
    # successfull is cheking the status code
    assert call.status_code == 201
    
    

def test_branch_restore():
    #restoring original branch name to prevent previous tc from failing
    github_api_client =GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    branch = "develop_changed"
    new_name = "develop"
    call = github_api_client.rename_branch(owner,repo,branch,new_name)  
    assert call.status_code == 201  

   



    
    
    
    
     
     