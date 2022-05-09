# MUSIC PLAYBACK
# COMMAND LIKE: "Play the song Magic by Coldplay"

import os


def music_playback(command):
    command = str(command).lower()
    music_list = []
    file_list = os.listdir(GV.pathDelimiter+"Music")
    for file in file_list:
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
            music_list.append(file)
    song_details = ""
    if "play the song" in command:
        song_details = command.split("play the song")[1].strip()
    elif "play song" in command:
        song_details = command.split("play song")[1].strip()
    if song_details == "":
        gtts_text = "Please specify the song"
        gtts(text=gtts_text)
        return
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
        gtts_text = "Sorry! I couldn't find the requested song"
        gtts(text=gtts_text)
    else:
        song_title = song_file.split(".")[0].split(" - ")[0].title()
        artist_name = song_file.split(".")[0].split(" - ")[1].title()
        gtts_text = "Playing " + song_title + " by " + \
            artist_name + " via VLC media player"
        gtts(text=gtts_text)
        vlc_path = "/usr/bin/vlc"
        try:
            subprocess.call([vlc_path, GV.pathDelimiter+"Music/"+song_file], stdout=GV.stdout_dump,
                            stderr=subprocess.STDOUT)
        except:
            gtts_text = "Sorry! An error encountered"
            gtts(text=gtts_text)
