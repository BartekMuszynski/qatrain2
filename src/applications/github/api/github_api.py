import requests

class GitHubAPI:
    """Class used for api calls used in tests"""

    def __init__(self) -> None:
        pass


    def search_repo(self, repo_name):
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})
        body = r.json()
        return body

