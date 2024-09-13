import requests
import json

def fetch_latest_release_from_acorn() -> dict|None:
    owner = "FirefoxUX" 
    repo = "acorn-icons"    
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    
def save_latest_release_if_needed(data: dict) -> bool:
    file = open("latest_acorn_release.json", "w")
    json.dump(data, fp=file)
    file.close()
    return True

latest_release_obj = fetch_latest_release_from_acorn()
if latest_release_obj:
    should_fetch_new_release = save_latest_release_if_needed(latest_release_obj)