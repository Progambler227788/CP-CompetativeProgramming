import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoPushHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print('File event detected:', event)
        os.chdir("E:/CP")
        
        # Add all changes
        add_output = os.system("git add .")
        print('git add output:', add_output)

        # Commit changes
        commit_output = os.system('git commit -m "Auto commit: {}"'.format(time.ctime()))
        print('git commit output:', commit_output)

        # Push changes
        push_output = os.system("git push origin main")
        print('git push output:', push_output)

if __name__ == "__main__":
    path = "E:/CP"
    event_handler = GitAutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
