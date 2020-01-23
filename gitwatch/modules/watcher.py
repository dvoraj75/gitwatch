from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWatcher:
    """
    Simple file system watcher which run Observer for file
    """
    def __init__(self, path: str):
        """
        Args:
            path(str): path to file or directory
        """
        self._observer = Observer()
        self.path = path

    def run(self) -> None:
        """
        Run simple observer for the file
        """
        event_handler = EventHandler()
        self._observer.schedule(event_handler, self.path, recursive=True)

    def stop(self) -> None:
        """
        Stop the observer
        """
        self._observer.stop()
        self._observer.join()


class EventHandler(FileSystemEventHandler):
    """
    Simple filesystem event handler
    """
    def on_any_event(self, event):
        pass
