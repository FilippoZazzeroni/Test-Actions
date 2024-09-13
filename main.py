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
    file = open("latest_acorn_release.json", "r+")
    should_fetch_new_icons = False
    if len(file.read()) == 0:
        json.dump(data, fp=file, indent=4)
        should_fetch_new_icons = True
    else:
        file.close()
        current_fetched_id = data["id"]
        file = open("latest_acorn_release.json", "w")
        saved_id = json.load(file)["id"]
        if current_fetched_id == saved_id:
            # new release has to be fetched
            json.dump(data, fp=file, indent=4)
            should_fetch_new_icons = True
    file.close()
    return should_fetch_new_icons

latest_release_obj = fetch_latest_release_from_acorn()
if latest_release_obj:
    should_fetch_new_release = save_latest_release_if_needed(latest_release_obj)