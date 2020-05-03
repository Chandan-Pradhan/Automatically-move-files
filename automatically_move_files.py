from shutil import move
import os

folder_to_track = "C:\\Users\\chand\\Desktop\\rex"
documents = "C:\\Users\\chand\\Desktop\\documents"
images = "C:\\Users\\chand\\Desktop\\images"
videos = "C:\\Users\\chand\\Desktop\\videos"
music = "C:\\Users\\chand\\Desktop\\music"
dirs = "C:\\Users\\chand\\Desktop\\dirs"


class Myhandler():
    def modified(self):
        for files in os.listdir(folder_to_track):
            filename, file_extension = os.path.splitext(files)
            if file_extension == ".jpg" or file_extension == ".png":
                move(folder_to_track + "\\" + files, images)
            elif file_extension == ".docx":
                move(folder_to_track + "\\" + files, documents)
            elif file_extension == ".mp4":
                move(folder_to_track + "\\" + files, videos)
            elif file_extension == ".mp3":
                move(folder_to_track + "\\" + files, music)
            else:
                move(files, dirs)


event_handler = Myhandler()

while True:
    event_handler.modified()
