import os
import shutil
import urllib.request

MUSIC_FOLDER = 'C:\\Users\\avathar\\Music\\KHinsider\\'


def save_file_from_url(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    directory = MUSIC_FOLDER + file_name.split('/')[0]
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = MUSIC_FOLDER + file_name
    with urllib.request.urlopen(url) as res, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(res, out_file)
    return file_name

