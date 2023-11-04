import requests
from src.applications.github.api.github_api import GitHubAPI
from src.applications.github.api.github_api import GitHubAuth
import time
import pytest

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
    non_existing_branch_name = "masterr"
    list_of_branches = github_api_client.search_branches(owner,repo)

    assert non_existing_branch_name not in list_of_branches

@pytest.mark.skip()
def test_branch_rename():
    github_api_client =GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    branch = "develop"
    new_name = "develop_changed"
    call = github_api_client.rename_branch(owner,repo,branch,new_name)
    assert call.status_code == 201
    #according to documentation renaming the branch may take some time
    #so we stop for 20 second to ensure the new branch name is updated
    time.sleep(20)
    assert new_name in github_api_client.search_branches(owner, repo)
    
    
    
@pytest.mark.skip()
def test_branch_restore():
    #restoring original branch name to prevent previous tc from failing
    github_api_client = GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    branch = "develop_changed"
    new_name = "develop"
    call = github_api_client.rename_branch(owner,repo,branch,new_name)  
    assert call.status_code == 201  


def test_creation_of_variable():
    #creating a variable in  repository 
    github_api_client = GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    name = "var11"
    value = "babaa"
    call = github_api_client.create_variable(owner,repo,name,value)

    assert call.status_code == 201
    assert name.upper() == github_api_client.get_variable(owner,repo,name)["name"]
    assert value == github_api_client.get_variable(owner,repo,name)["value"]


def test_updating_variable():
    github_api_client = GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    name = "var11"
    value = "b"
    call  = github_api_client.update_variable(owner,repo,name,value)

    assert call.status_code == 204
    assert name.upper() == github_api_client.get_variable(owner,repo,name)["name"]
    assert value == github_api_client.get_variable(owner,repo,name)["value"]

def test_deleting_variable():
    github_api_client = GitHubAPI()
    owner = "bartekmuszynski"
    repo = "tic_tac_toee"
    name = "var11"
    call = github_api_client.delete_variable(owner,repo,name)
    
    assert call.status_code == 204
    assert name not in github_api_client.get_variable(owner,repo,name)

    
    



  



   



    
    
    
    
     
     