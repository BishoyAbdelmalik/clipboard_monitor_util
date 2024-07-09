from watchdog.observers import Observer
from EventHandler import MyEventHandler
import os
import time
if __name__ == "__main__":

    path = os.getenv('CLIPBOARD_PATH')
    if path==None:
        path="file"
    if not os.path.exists(path):
        with open(path, 'w'): 
            pass
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()