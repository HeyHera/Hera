# MUSIC PLAYBACK
# COMMAND LIKE: "Play the song Magic by Coldplay"

import os
import subprocess
import yaml

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
    file_list = os.listdir(exp_user_path)

    for file in file_list:
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
            music_list.append(file)
    song_details = ""
    if "play the song" in command:
        song_details = command.split("play the song")[1].strip()
    elif "play song" in command:
        song_details = command.split("play song")[1].strip()
    if song_details == "":
        return("Please specify the song")
    search_success = 0
    song_file = ""
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


if __name__ == '__main__':
    spoken = music_playback("Play the song Faded")
