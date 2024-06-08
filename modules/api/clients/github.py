import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
 
    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", 
                         params={"q": name})
        body = r.json()

        return body
    
    def get_emoji_url(self, emoji_name):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()
        return body.get(emoji_name)

    def get_commits(self, OWNER, REPO):
        list= requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/commits") 
        body = list.json()

        return body
    
    def count_commits(self, OWNER, REPO):
        list_commits = self.get_commits(OWNER, REPO)

        return len(list_commits)
    