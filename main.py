import requests

def fetch_latest_release_from_acorn() -> str|None:
    owner = "FirefoxUX" 
    repo = "acorn-icons"    
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.json())
        return response.json()["id"]
    
print(fetch_latest_release_from_acorn())