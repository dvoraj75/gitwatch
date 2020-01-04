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

    def push(self, repository: GitRepo, branch: str = "master", remote: str = "origin") -> None:
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

    def commit(self, repository: GitRepo, commit_message: str) -> None:
        """
        Commit staged changes
        Args:
            repository (GitRepo): git repository
            commit_message (str): commit message
        Raises:
            GitCommandException: raises if nothing to commit or commit_message is empty string
        """
        try:
            repository.repo.git.commit(m=commit_message)
        except git.CommandError as e:
            err_msg = "nothing to commit" if commit_message else "commit_message can't be empty string"
            self.logger.error(f"Can't commit changes, {err_msg}")
            self.logger.error(e)
            raise GitCommandException(f"Can't commit changes, {err_msg}")

    def add(self, repository: GitRepo, path: str) -> None:
        """
        Stage changes
        Args:
            repository (GitRepo): git repository
            path (str): path to file
        Raises:
            GitCommandException: raises if path does not exist
        """
        try:
            repository.repo.git.add(path)
        except git.GitCommandError as e:
            self.logger.error(f"Can't add file {path}. File does not exist")
            self.logger.error(e)
            raise GitCommandException(f"Can't add file {path}. File does not exist")

    def checkout(self, repository: GitRepo, branch: str) -> None:
        """
        Checkout to branch, if branch does not exist, create it.
        Args:
            repository (GitRepo): git repository
            branch (str): name of git branch
        """
        try:
            repository.repo.git.checkout(branch)
        except git.GitCommandError:
            self.logger.warning(f"Branch {branch} in {repository.url} does not exist.")
            self.logger.info(f"Creating branch: {branch}")
            repository.repo.git.checkout(b=branch)

    def branch(self, repository: GitRepo) -> str:
        """
        Return active branch of repository
        Args:
            repository (GitRepo): git repository
        Returns:
            str: name of active branch
        """
        return repository.repo.active_branch.name
