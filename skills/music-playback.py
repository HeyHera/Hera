# MUSIC PLAYBACK
# COMMAND LIKE: "Play the song Magic"


def music_playback(command):
    import os
    import subprocess
    import yaml
    import random
    from importlib.machinery import SourceFileLoader
    import difflib
    tts_module = SourceFileLoader(
        "Text-To-Speech", "text-to-speech/espeak.py").load_module()

    def random_song(music_list):
        tts_module.tts("Playing a random song")
        return(music_list[random.randint(0, len(music_list)-1)])

    os_username = os.getlogin()
    command = str(command).lower()
    music_list = []
    try:
        with open('configs/'+os_username+'.yaml', 'r') as config_file:
            yaml_load = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

    exp_user_path = os.path.expanduser(yaml_load['Directories']['Music'])
    # print(exp_user_path)
    file_list = os.listdir(exp_user_path)
    song_file = None
    for file in file_list:
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
            music_list.append(file)
    file = None
    random_flag = 0
    song_details = None
    if "play the song" in command:
        song_details = command.split("play the song")[1].strip()
    elif "play song" in command:
        song_details = command.split("play song")[1].strip()
    elif "any song" in command or "play a song" in command\
            or "play some song" in command or "play some music" in command\
            or "play any music" in command or "play some music" in command\
            or "play some song" in command or "random song" in command:
        song_file = random_song(music_list=music_list)
        random_flag = 1
    elif "play" in command:
        song_details = command.split("play")[1].strip()
    else:
        tts_module.tts("Please specify the song")
        return(2)  # 2 = Return Prompt
    if song_details == '':
        song_file = random_song(music_list=music_list)
        random_flag = 1
    search_success = 0
    if random_flag == 0:
        # for song in music_list:
        #     if song_details in str(song).lower():
        #         song_file = str(song)
        #         search_success = 1
        #         break
        closest_matched_songs = difflib.get_close_matches(
            song_details, music_list, cutoff=0.3)
        if len(closest_matched_songs) > 0:
            search_success = 1
            song_file = closest_matched_songs[0]
    if search_success == 0 and random_flag == 0:
        tts_module.tts("Sorry! I couldn't find the requested song")
        return(1)  # 1 = Fail
    else:
        vlc_path = "/usr/bin/vlc"
        try:
            print("Playing {}".format(song_file))
            subprocess.call([vlc_path, str(exp_user_path) +
                            "/"+song_file], stderr=subprocess.STDOUT)
            return(0)  # 0 = Success
        except:
            tts_module.tts("Sorry! An error encountered")
            return(1)  # 1 = Fail


if __name__ == '__main__':
    skill_response = None
    skill_response = music_playback("i like to dance in random songs")
    # skill_response = music_playback("Play the song in the end")
    if skill_response != None:
        if skill_response == 0:
            print("Success")
        elif skill_response == 1:
            print("Fail")
        else:
            print("Return Prompt")
    else:
        print("Error")
