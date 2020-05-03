from shutil import move
from pathlib import Path
import os

folder_to_track = "C:\\Users\\chand\\Desktop\\rex"
documents = "C:\\Users\\chand\\Desktop\\documents"
images = "C:\\Users\\chand\\Desktop\\images"
videos = "C:\\Users\\chand\\Desktop\\videos"
music = "C:\\Users\\chand\\Desktop\\music"
dirs = "C:\\Users\\chand\\Desktop\\dirs"


class Myhandler():
    def modified(self):
        for files in Path("C:\\Users\\chand\\Desktop\\rex").rglob("*.*"):
            filename, file_extension = os.path.splitext(files)
            if file_extension == ".jpg" or file_extension == ".png":
                move(str(files), images)
            elif file_extension == ".docx":
                move(str(files), documents)
            elif file_extension == ".mp4":
                move(str(files), videos)
            elif file_extension == ".mp3":
                move(str(files), music)


event_handler = Myhandler()

while True:
    event_handler.modified()
