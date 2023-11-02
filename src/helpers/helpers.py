import requests

class GitHubAuth:
        # Github client made for operations requiring authetication
        # github token is saved in local file, that is in .gitignore
        #later it will be coming from config file, no time for now

    def gh_session_authetication_client(self):
        with open("git_token.txt") as file:
            token = file.read()
            username = "bartekmuszynski"
            gh_session =requests.Session()
            gh_session.auth = (username,token)
            return gh_session
    



        
