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
     
    def get_emoji_status_code_by_unique_code(self, emoji_unique_code):
        r = requests.get(f"https://github.githubassets.com/images/icons/emoji/unicode/{emoji_unique_code}")
       
        return r.status_code
    
    def get_emoji_key(self, emoji_key):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body.get(emoji_key)
    
    def get_commits(self, OWNER, REPO):
        list = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/commits") 
        body = list.json()

        return body
      
    def count_commits(self, OWNER, REPO):
        list_commits = self.get_commits(OWNER, REPO)

        return len(list_commits)
    
    def check_email_and_commit_by_user_and_by_repo(self, OWNER, REPO, expected_email, expected_message):
        list = self.get_commits(OWNER, REPO)
        quantity_of_all_commits = self.count_commits(OWNER, REPO)
        commit_email = None
        commit_message = None
        for index in range(0, quantity_of_all_commits):
            commit = list[index]
            if commit["commit"]["author"]['email'] == expected_email and commit["commit"]["message"] == expected_message:
                commit_email = commit["commit"]["author"]['email']
                commit_message = commit["commit"]["message"]
                break
            
        return commit_email, commit_message 