# MUSIC PLAYBACK
# COMMAND LIKE: "Play the song Magic"


def music_playback(status, pipe_end, command, intent):
    import os
    import subprocess
    import yaml
    import random
    import difflib
    from importlib.machinery import SourceFileLoader
    tts_module = SourceFileLoader(
        "Text-To-Speech", "tts/speak.py").load_module()
    entity_extractor_module = SourceFileLoader(
        "Entity-Extractor-Module", "nlu/entity_extraction/entity_extractor.py").load_module()

    def random_song(music_list):
        msg = "Playing a random song"
        pipe_end.send(msg)
        tts_module.tts(msg)
        pipe_end.close()
        return(music_list[random.randint(0, len(music_list)-1)])

    os_username = os.getlogin()
    music_list = []
    msg = None
    try:
        with open('configs/'+os_username+'.yaml', 'r') as config_file:
            yaml_load = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

    exp_user_path = os.path.expanduser(yaml_load['Directories']['Music'])
    file_list = os.listdir(exp_user_path)
    song_file = None
    for file in file_list:
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
            music_list.append(file)
    command = str(command).lower()
    song_details = None
    if intent == 'MUSIC_PLAYBACK_RANDOM_SONG':
        song_file = random_song(music_list=music_list)
    elif intent == 'MUSIC_PLAYBACK_SPECIFIC_SONG' or 'MUSIC_PLAYBACK_ALBUM_SONG':
        song_details = entity_extractor_module.extract(
            model_test_sentence=command, entity_label="MUSIC", model_path="nlu/entity_extraction/output/music_playback/model-best")
        if song_details == "None":
            msg = "Sorry! I couldn't find the requested song"
            pipe_end.send(msg)
            tts_module.tts(msg)
            pipe_end.close()
            tts_module.tts(msg)
            status.value = 1
            # return(1)  # 1 = Fail
        closest_matched_songs = difflib.get_close_matches(
            song_details, music_list, cutoff=0.4)
        if len(closest_matched_songs) > 0:
            song_file = closest_matched_songs[0]
        else:
            msg = "Sorry! I couldn't find the requested song"
            pipe_end.send(msg)
            tts_module.tts(msg)
            pipe_end.close()
            tts_module.tts(msg)
            status.value = 1
    else:
        msg = "Sorry! I couldn't find the requested song"
        pipe_end.send(msg)
        tts_module.tts(msg)
        pipe_end.close()
        tts_module.tts(msg)
        status.value = 1
    vlc_path = "/usr/bin/vlc"
    try:
        if intent != 'MUSIC_PLAYBACK_RANDOM_SONG':
            msg = "Playing " + song_file
            pipe_end.send(msg)
            tts_module.tts("Playing")
        subprocess.call([vlc_path, str(exp_user_path) +
                        "/"+song_file], stderr=subprocess.STDOUT)
        status.value = 0
    except:
        # tts_module.tts()
        msg = "Sorry! An error encountered"
        pipe_end.send(msg)
        tts_module.tts(msg)
        pipe_end.close()
        tts_module.tts(msg)
        status.value = 1

# if __name__ == '__main__':
#     skill_response = None
#     skill_response = music_playback(
#         "play the song from grandmaster", "MUSIC_PLAYBACK_ALBUM_SONG")
#     # skill_response = music_playback("Play the song in the end")
#     if skill_response != None:
#         if skill_response == 0:
#             print("Success")
#         elif skill_response == 1:
#             print("Fail")
#         else:
#             print("Return Prompt")
#     else:
#         print("Error")
