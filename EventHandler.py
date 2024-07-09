from watchdog.events import FileSystemEventHandler,FileSystemEvent, FileModifiedEvent
import pyperclip

class MyEventHandler(FileSystemEventHandler):
    
    
    def on_modified(self, event: FileSystemEvent) -> None:
        """Called when a file or directory is modified.

        :param event:
            Event representing file/directory modification.
        :type event:
            :class:`DirModifiedEvent` or :class:`FileModifiedEvent`
        """
        if isinstance(event,FileModifiedEvent):
            pyperclip.copy(open(event.src_path).read())
