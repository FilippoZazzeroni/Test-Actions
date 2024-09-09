import requests
import json

def fetch_latest_release_from_acorn() -> dict|None:
    owner = "FirefoxUX" 
    repo = "acorn-icons"    
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    

latest_release_obj = fetch_latest_release_from_acorn()

file = open("test.json", "w")
json.dump(latest_release_obj, fp=file)
file.close()