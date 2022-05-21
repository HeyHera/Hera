from importlib.machinery import SourceFileLoader
import threading

# LOCAL IMPORTS
wwd_module = SourceFileLoader(
    "Wake-Word-Detection", "wake-word-detection/wake-word-detection.py").load_module()
asr_module = SourceFileLoader(
    "Automatic-Speech-Recognition", "speech-recognition/automatic-speech-recognition.py").load_module()
tts_module = SourceFileLoader(
    "Text-To-Speech", "text-to-speech/espeak.py").load_module()
greeting_skill = SourceFileLoader(
    "Greeting-Skill", "skills/greetings.py").load_module()
music_playback_skill = SourceFileLoader(
    "Music-Playback-Skill", "skills/music-playback.py").load_module()
launch_application_skill = SourceFileLoader(
    "Launch-Application", "skills/launch-application.py").load_module()

# TO RUN INDEFINITELY
while(True):

    # CALLING WAKE-WORD-DETECTION IN A SEPARATE THREAD
    wwd_thread = threading.Thread(
        target=wwd_module.listener(), name="Wake-Word-Detection-Thread")
    wwd_thread.start()
    wwd_thread.join()  # WAITING wwd_thread TO STOP EXECUTING

    # WHILE WAKE WORD IS NOT WORKING
    start_char = input(
        "\n{} PRESS ENTER TO CONTINUE {}\n".format('='*20, '='*20))
    if start_char != "":
        print("Please press Enter")
    else:

        # CALLING TEXT-TO-SPEECH FOR GREETING THE USER
        tts_module.tts(greeting_skill.greeting())

        # CALLING AUTOMATIC-SPEECH-RECOGNITION TO RECOGNIZE COMMAND
        try:
            print("{} Automatic Speech Recognition Initialized {}".format(
                '='*20, '='*20))
            spoken = asr_module.asr()
            print(spoken)
        except Exception as e:
            tts_module.tts(
                "Error encountered. I couldn't connect with Automatic Speech Recognition")
            print(e)

        # MATCHING THE COMMAND WITH CORRESPONDING SKILL
        statement = spoken.lower()
        skill_response = None
        if "play" in statement or "music" in statement or "song" in statement:
            print("Skill: music_playback_skill")
            skill_response = music_playback_skill.music_playback(statement)
        elif statement.startswith("launch") or statement.startswith("open"):
            print("Skill: launch_application_skill")
            skill_response = launch_application_skill.launch_applications(
                statement)
        print(skill_response)
        if skill_response != None:
            if skill_response == 0:
                print("Success")
            elif skill_response == 1:
                print("Fail")
            else:
                print("Return prompt")
        else:
            tts_module.tts("Sorry! I did't understood that.")
