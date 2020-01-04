from dataclasses import dataclass

import git


@dataclass
class GitRepo:
    """
    Dataclass representing git repository
    """
    repo: git.Repo
    url: str
    destination: str


class GitApi:

    def __init__(self, logger):
        self.logger = logger

    def clone(self, url: str, to_path: str) -> GitRepo:
        """
        Clone git repository
        Args:
            url (str): url of git repository
            to_path(str): path to repository destination folder
        Raises:
            git.GitCommandError: raises if destination folder exists or url is not accessible
        Returns:
            GitRepo: instance of git repository
        """
        try:
            repo = git.Repo.clone_from(url, to_path)
            return GitRepo(repo, url, to_path)
        except git.GitCommandError as e:
            self.logger.error(e)
            raise

    def pull(self):
        pass

    def push(self):
        pass

    def commit(self):
        pass

    def add(self):
        pass

    def remote(self):
        pass

    def branch(self):
        pass

