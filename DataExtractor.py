import requests
import os
import subprocess

GITHUB_TOKEN = "PAT"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def search_repositories(language="C++", stars=">100"):
    url = f"https://api.github.com/search/repositories?q=language:{language}+stars:{stars}&per_page=10"
    response = requests.get(url, headers=HEADERS)
    return response.json()["items"]

def clone_repository(clone_url, destination_folder="repositories"):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    subprocess.run(["git", "clone", clone_url, destination_folder], check=True)

if __name__ == "__main__":
    repos = search_repositories()
    for repo in repos:
        print(f"Cloning {repo['full_name']}...")
        clone_repository(repo["clone_url"])
