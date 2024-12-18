import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def get_emoji_url(self, emoji_name):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body.get(emoji_name)

    def get_emoji_status_code_by_unique_code(self, emoji_unique_code):
        r = requests.get(
            f"https://github.githubassets.com/images/icons/emoji/unicode/{emoji_unique_code}"
        )

        return r.status_code

    def get_emoji_key(self, emoji_key):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body.get(emoji_key)

    def get_commits(self, owner, repo):
        list_of_commits = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits"
        )
        body = list_of_commits.json()

        return body

    def _count_commits(self, owner, repo):
        list_commits = self.get_commits(owner, repo)

        return len(list_commits)

    def get_email_and_commit_by_user_and_by_repo(
        self, owner, repo, expected_email, expected_message
    ):
        # a copy of method below
        list_commits = self.get_commits(owner, repo)
        quantity_of_all_commits = len(list_commits)
        commit_email = None
        commit_message = None

        for index in range(0, quantity_of_all_commits):
            commit = list_commits[index]
            if (
                commit["commit"]["author"]["email"] == expected_email
                and commit["commit"]["message"] == expected_message
            ):
                commit_email = commit["commit"]["author"]["email"]
                commit_message = commit["commit"]["message"]
                break

        return commit_email, commit_message

    def check_email_and_commit_by_user_and_by_repo(
        self, owner, repo, expected_email, expected_message
    ):
        # Redesign so to have an answer on check itself
        list_commits = self.get_commits(owner, repo)

        for commit in list_commits:
            if (
                commit["commit"]["author"]["email"] == expected_email
                and commit["commit"]["message"] == expected_message
            ):
                return True
