from dataclasses import dataclass

import git


class GitCommandException(Exception):
    pass


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
            GitCommandException: raises if destination folder exists or url is not accessible
        Returns:
            GitRepo: instance of git repository
        """
        try:
            repo = git.Repo.clone_from(url, to_path)
            return GitRepo(repo, url, to_path)
        except git.GitCommandError as e:
            self.logger.error(f"Can't clone repository. Url: {url} to: {to_path}")
            self.logger.error(e)
            raise GitCommandException(f"Can't clone repository. Url: {url} to: {to_path}")

    def pull(self, repository: GitRepo, branch: str = "master", remote: str = "origin") -> None:
        """
        Pull from git repository
        Args:
            repository (GitRepo): git repository
            branch (str): branch to pull
            remote (str): name of remote
        Raises:
            GitCommandException: if branch or remote are not valid
        """
        try:
            repository.repo.git.pull(remote, branch)
        except git.GitCommandError as e:
            self.logger.error(f"Can't pull from repository: {repository.url} branch: {branch} remote: {remote}")
            self.logger.error(e)
            raise GitCommandException(f"Can't pull from repository: {repository.url} branch: {branch} remote: {remote}")

    def push(self, repository: GitRepo, branch: str = "master", remote: str = "origin"):
        """
        Push to git repository
        Args:
            repository (GitRepo): git repository
            branch (str): branch to pull
            remote (str): name of remote
        Raises:
            GitCommandException: if branch or remote are not valid
        """
        try:
            repository.repo.git.push(remote, branch)
        except git.CommandError as e:
            self.logger.error(f"Can't push to repository: {repository.url} branch: {branch} remote: {remote}")
            self.logger.error(e)
            raise GitCommandException(f"Can't push to repository: {repository.url} branch: {branch} remote: {remote}")

    def commit(self):
        pass

    def add(self):
        pass

    def remote(self):
        pass

    def branch(self):
        pass

