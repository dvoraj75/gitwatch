from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWatcher:

    def __init__(self, path: str):
        self._observer = Observer()
        self.path = path

    def run(self):
        event_handler = EventHandler()
        self._observer.schedule(event_handler, self.path, recursive=True)

    def stop(self):
        self._observer.stop()
        self._observer.join()


class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        pass
