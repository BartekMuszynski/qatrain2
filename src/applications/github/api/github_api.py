import requests
from src.config.config1 import *

class GitHubAPI:
    """Class used for api calls used in tests"""



    def search_repo(self, repo_name):
        #function searching for repository and returning it properties 
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})
        body = r.json()
        return body
    
    def search_branches(self, owner, repo):
        #function returning list of branches in provided repo
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches")
        body = r.json()
        branch_names  = []
        for provider in body :
            branch_names.append(provider["name"])
        return branch_names
    
    def rename_branch(self,owner,repo,branch,new_name):
        #function that changes branch name in given repo 
        url = f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}/rename"
        gh_auth_client = GitHubAuth()
        data = {"new_name": new_name}
        posted_data = gh_auth_client.gh_session_authetication_client().post(
            url,
            json = data
        )
        return posted_data
    

    def create_variable(self,owner,repo,name,value) :
        #function for creating  reposiotyr variavbles in given repository
        url = f"https://api.github.com/repos/{owner}/{repo}/actions/variables"
        gh_auth_client = GitHubAuth()
        data = {"name": name, "value": value}
        posted_var = gh_auth_client.gh_session_authetication_client().post(
            url,
            json = data 
        )
        return posted_var
    

    def get_variable(self,owner,repo,name) :
        url = f"https://api.github.com/repos/{owner}/{repo}/actions/variables/{name}"
        gh_auth_client = GitHubAuth()
        r = gh_auth_client.gh_session_authetication_client().get(url)
        variable_data = r.json()

        return variable_data
    
    def update_variable(self,owner,repo,name,value) :
        url = f"https://api.github.com/repos/{owner}/{repo}/actions/variables/{name}"
        gh_auth_client = GitHubAuth()
        data = {"name": name, "value" : value}
        r = gh_auth_client.gh_session_authetication_client().patch(
            url,
            json = data
        )
        return r
    
    def delete_variable(self,owner,repo,name) :
        url = f"https://api.github.com/repos/{owner}/{repo}/actions/variables/{name}"
        gh_auth_client = GitHubAuth()
        r = gh_auth_client.gh_session_authetication_client().delete(url)
        return r
        
class GitHubAuth:
        # Github client made for operations requiring authetication

    def gh_session_authetication_client(self):
            gh_session = requests.Session()
            gh_session.auth = (owner,git_token)
            return gh_session
        



    

        
    


     

    
    
    

    

