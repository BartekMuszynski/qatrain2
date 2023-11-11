from src.config.config1 import *
import time
import pytest




def test_search_for_existing_repo(git_api_client):
    repos = git_api_client.search_repo(existing_repo_name)

    assert repos['total_count'] != 0

def test_search_for_nonexisting_repo(git_api_client):
    repos = git_api_client.search_repo(nonexisting_repo_name)

    assert repos['total_count'] == 0

def test_search_for_existing_branch(git_api_client):
    list_of_branches = git_api_client.search_branches(owner,repo)

    assert existing_branch_name in list_of_branches


def test_search_for_nonexisting_branches(git_api_client):
    list_of_branches = git_api_client.search_branches(owner,repo)

    assert non_existing_branch_name not in list_of_branches


def test_branch_rename(git_api_client):
    call = git_api_client.rename_branch(owner,repo,original_branch_name,renamed_branch_name)
    assert call.status_code == 201
    #according to documentation renaming the branch may take some time
    #so we stop for 20 second to ensure the new branch name is updated
    time.sleep(20)
    assert renamed_branch_name in git_api_client.search_branches(owner, repo)
    
    
    

def test_branch_restore(git_api_client):
    #restoring original branch name to prevent previous tc from failing
    call = git_api_client.rename_branch(owner,repo,renamed_branch_name,original_branch_name)  
    assert call.status_code == 201  


def test_creation_of_variable(git_api_client):
    #creating a variable in  repository 
    call = git_api_client.create_variable(owner,repo,repository_var_name,repository_var_value)

    assert call.status_code == 201
    assert repository_var_name.upper() == git_api_client.get_variable(owner,repo,repository_var_name)["name"]
    assert repository_var_value == git_api_client.get_variable(owner,repo,repository_var_name)["value"]


def test_updating_variable(git_api_client):
    call  = git_api_client.update_variable(owner,repo,repository_var_name,repository_var_value_updated)

    assert call.status_code == 204
    assert repository_var_value_updated == git_api_client.get_variable(owner,repo,repository_var_name)["value"]

def test_deleting_variable(git_api_client):

    
    call = git_api_client.delete_variable(owner,repo,repository_var_name)
    
    assert call.status_code == 204
    assert repository_var_name not in git_api_client.get_variable(owner,repo,repository_var_name)

    
    



  



   



    
    
    
    
     
     