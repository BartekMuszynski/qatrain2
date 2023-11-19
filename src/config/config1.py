from dotenv import load_dotenv
import os


load_dotenv()
existing_repo_name = os.getenv("EXISTING_REPO_NAME")
nonexisting_repo_name = os.getenv("nonexisting_repo_name")
owner = os.getenv("owner")
repo = os.getenv("repo")
existing_branch_name = os.getenv("existing_branch_name")
non_existing_branch_name = os.getenv("non_existing_branch_name")
original_branch_name = os.getenv("original_branch_name")
renamed_branch_name = os.getenv("renamed_branch_name")
repository_var_name = os.getenv("repository_var_name")
repository_var_value = os.getenv("repository_var_value")
repository_var_value_updated = os.getenv("repository_var_value_updated")
git_token = os.getenv("git_token")
base_url = os.getenv("base_url")



