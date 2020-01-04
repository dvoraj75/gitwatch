import git


class GitApi:

    def __init__(self, logger):
        self.logger = logger

    def clone(self, url: str, to_path: str) -> git.Repo:
        """
        Clone git repository
        Args:
            url (str): url of git repository
            to_path(str): path to repository destination folder
        Raises:
            git.GitCommandError: raises if destination folder exists or url is not accessible
        Returns:
            git.Repo: instance of git repository
        """
        try:
            return git.Repo.clone_from(url, to_path)
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

