from os import scandir
from shutil import move

source_dir = "C:\\Users\\srsly\\Downloads"
dest_dir_sfx = "C:\\Users\\srsly\\Downloads\\sfx"
dest_dir_musics = "C:\\Users\\srsly\\Downloads\\music"
dest_dir_videos = "C:\\Users\\srsly\\Downloads\\videos"
dest_dir_documents = "C:\\Users\\srsly\\Downloads\\documents"
dest_dir_images = "C:\\Users\\srsly\\Downloads\\images"
dest_dir_images3 = "C:\\Users\\srsly\\Documents\\images"


image_extensions = (".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")

video_extensions = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def move_file(image_name, dest_dir):
    #print("image_name: " + image_name + "\ndest_dir: "+ dest_dir)
    move(image_name, dest_dir)
    
    
    


def cleaner():
    for i in range(len(image_extensions)):
        with scandir(source_dir) as entries:
            for entry in entries:
                if entry.name.endswith(image_extensions[i]):
                    move_file(entry, dest_dir_images)
    i = i+1

cleaner()

