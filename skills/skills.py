# MUSIC PLAYBACK
# COMMAND LIKE: "Play the song Magic by Coldplay"

import os
import subprocess
import webbrowser
import yaml
import random
import difflib

os_username = os.getlogin()


def music_playback(command):
    command = str(command).lower()
    music_list = []
    try:
        with open('configs/'+os_username+'.yaml', 'r') as config_file:
            yaml_load = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

    exp_user_path = os.path.expanduser(yaml_load['Directories']['Music'])
    print(exp_user_path)
    file_list = os.listdir(exp_user_path)
    song_file = ""
    for file in file_list:
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
            music_list.append(file)
    song_details = ""
    random_flag = 0
    if "play the song" in command:
        song_details = command.split("play the song")[1].strip()
    elif "play song" in command:
        song_details = command.split("play song")[1].strip()
    elif "play any song" or "play a song" or "play some song" or "play some music" in command:
        song_file = music_list[random.randint(0, len(music_list)-1)]
        print("random", song_file)
        random_flag = 1
    else:
        return("Please specify the song")
    search_success = 0
    if random_flag == 0:
        if "by" in song_details:
            song_title = song_details.split("by")[0].strip()
            artist_name = song_details.split("by")[1].strip()
            for song in music_list:
                if song_title in str(song).lower() and artist_name in str(song).lower():
                    song_file = str(song)
                    search_success = 1
                    break
        else:
            for song in music_list:
                if song_details in str(song).lower():
                    song_file = str(song)
                    search_success = 1
                    break
    if search_success == 0:
        return("Sorry! I couldn't find the requested song")
    else:
        song_title = song_file.split(".")[0].split(" - ")[0].title()
        artist_name = song_file.split(".")[0].split(" - ")[1].title()
        vlc_path = "/usr/bin/vlc"
        try:
            subprocess.call([vlc_path, str(exp_user_path) +
                            "/"+song_file], stderr=subprocess.STDOUT)
        except:
            return("Sorry! An error encountered")


# LAUNCH PRELISTED APPLICATIONS
# COMMAND LIKE: "Launch Google Chrome"
        # "Open Weather"


def launch_applications(command):
    command = str(command).lower()
    app_to_launch = ""
    application_list = ["firefox", "google-chrome", "gnome-weather",
                        "gnome-calculator", "gnome-terminal"]
    if command.startswith("open"):
        app_to_launch = command.split("open")[1].strip().title()
    elif command.startswith("launch"):
        app_to_launch = command.split("launch")[1].strip().title()
    if app_to_launch == "":
        return("Please specify the application to launch")
    closest_matched_apps = difflib.get_close_matches(
        app_to_launch, application_list)
    if len(closest_matched_apps) != 0:
        try:
            subprocess.call("/usr/bin/"+closest_matched_apps[0], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
        except:
            return("Sorry! An error encountered")
    else:
        sites = ["gmail.com", "youtube.com", "wikipedia.com", "flipkart.com",
                 "amazon.in", "in.bookmyshow.com", "hotstar.com", "primevideo.com"]
        closest_matched_sites = difflib.get_close_matches(
            app_to_launch, sites)
    if len(closest_matched_sites) != 0:
        try:
            webbrowser.open_new_tab(closest_matched_sites)
        except:
            return("Sorry! An error encountered")        
        return("Sorry! Unable to find the application")

# OPEN URL'S
# COMMAND LIKE: "O"
        # "Open Weather"


if __name__ == '__main__':
    #spoken = launch_applications("Open terminal")
    spoken = music_playback("Play any song")
    print(spoken)
