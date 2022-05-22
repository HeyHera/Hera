from importlib.machinery import SourceFileLoader
import threading

# LOCAL IMPORTS
try:
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
    print("\nLocal imports successful")
except Exception as e:
    print("\nLocal imports unsuccessful.\n" + str(e))

# TO RUN INDEFINITELY
main_pass_no = 0
while(True):
    main_pass_no += 1
    print("\n[__main__] Pass #{}".format(main_pass_no))
    try:
        # CALLING WAKE-WORD-DETECTION IN A SEPARATE THREAD
        print("\n{} Wake Word Detection thread starting {}".format(
            '='*20, '='*20))
        wwd_thread = threading.Thread(
            target=wwd_module.listener(), name="Wake-Word-Detection-Thread")
        wwd_thread.start()
        wwd_thread.join()  # WAITING wwd_thread TO STOP EXECUTING
    except Exception as e:
        print("An error occurred while starting Wake Word Detection thread")

    # WHILE WAKE WORD IS NOT WORKING
    start_char = input("Press Enter to continue: ")
    if start_char != "":
        print("Exiting")
        exit()
    else:

        # CALLING TEXT-TO-SPEECH FOR GREETING THE USER
        tts_module.tts(greeting_skill.greeting())

        # CALLING AUTOMATIC-SPEECH-RECOGNITION TO RECOGNIZE COMMAND
        try:
            print("\n{} Automatic Speech Recognition initializing {}".format(
                '='*20, '='*20))
            spoken = asr_module.asr()
            print(spoken)
        except Exception as e:
            print(
                "\nError encountered. Couldn't connect with Automatic Speech Recognition.\n" + str(e))

        # MATCHING THE COMMAND WITH CORRESPONDING SKILL
        statement = spoken.lower()
        skill_response = None
        print("\n{} Skill match starting {}".format(
            '='*20, '='*20))
        if statement == "":
            print("Nothing received as command")
            # PLAY AN AUDITORY ERROR BELL
        if "play" in statement or "music" in statement or "song" in statement:
            print("Matched: music_playback_skill")
            skill_response = music_playback_skill.music_playback(statement)
        elif statement.startswith("launch") or statement.startswith("open"):
            print("Matched: launch_application_skill")
            skill_response = launch_application_skill.launch_applications(
                statement)
        print("Skill response: {}" .format(skill_response))
        if skill_response == 0:
            print("Success")
        elif skill_response == 1:
            print("Fail")
        elif skill_response == 2:
            print("Return prompt")
        elif skill_response != None:
            tts_module.tts("Sorry! I did't understood that.")