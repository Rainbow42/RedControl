from master_node.controller import ControllerSSHServer


class GitController:
    def __init__(self, controller: ControllerSSHServer):
        self.controller = controller

    @staticmethod
    def gitlab_token_https(token: str, https_git: list) -> str:
        return 'https://' + 'oauth2:' + token + '@' + '/'.join(https_git[2:])

    def get_https_token(self, token: str, https_git: str) -> str:
        """Получим ссылку в которую вшит токен"""
        https_git = https_git.split('/')
        # TODO добавить вшивание токена для github
        return self.gitlab_token_https(token, https_git) \
            if 'gitlab.com' in https_git else None

    def git_clone_project(self, token: str, https_git: str) -> str:
        https = self.get_https_token(token, https_git)
        return f'git clone {https}'
