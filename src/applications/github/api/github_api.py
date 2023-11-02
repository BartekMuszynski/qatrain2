import requests
from src.helpers.helpers import * 

class GitHubAPI:
    """Class used for api calls used in tests"""


    def __init__(self) -> None:
        pass


    def search_repo(self, repo_name):
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})
        body = r.json()
        return body
    
    def search_branches(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches")
        body = r.json()
        branch_names  = []
        for provider in body :
            branch_names.append(provider["name"])
        return branch_names
    
    def rename_branch(self,owner,repo,branch,new_name):
        url = f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}/rename"
        gh_auth_client = GitHubAuth()
        data = {"new_name": new_name}
        posted_data = gh_auth_client.gh_session_authetication_client().post(
            url,
            json = data
        )
        return posted_data
        
    

        
    


     

    
    
    

    

