# KHdownloader
Small python script to download full music albums from the KH Insider video game music website


## Usage

This script works parsing the web page of an album from downloads.khinsider.com by every song download page url, and then parses that page for the mp3 url

        python khdownloader.py <album_url>


## Options

Inside the url_file_download.py file is the MUSIC_FOLDER variable to set the base location for the mp3 files to be saved.
Same script checks and if necessary, creates a folder with the album name.

## ToDo

1. Add some error management
1. Create and read from a settings file
1. Organize folder structure
1. Think about something else to add to this
