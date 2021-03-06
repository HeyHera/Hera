import subprocess
import threading

# LOCAL IMPORTS
try:
    import wake_word_detection.wake_word_detection_script as wwd_module
    import automatic_speech_recognition.automatic_speech_recognition_script as asr_module
    import nlu.intent_classification.intent_classifier as intent_classifier_module
    import tts.speak as tts_module
    import skills.greetings as greeting_skill
    import skills.music_playback as music_playback_skill
    import skills.launch_application as launch_application_skill
    print("\nLocal imports successful")
except Exception as e:
    print("\nLocal imports unsuccessful.\n" + str(e))

# TO RUN INDEFINITELY
main_pass_no = 0
while(True):
    main_pass_no += 1
    print("\n[__main__] Pass #{}".format(main_pass_no))
    start_char = input("Press Enter to continue: ")
    if start_char != "":
        print("Exiting")
        exit()
    else:
        try:
            # CALLING WAKE-WORD-DETECTION IN A SEPARATE THREAD
            print("\n{} Wake Word Detection thread starting {}".format(
                '='*20, '='*20))
            wwd_thread = threading.Thread(
                target=wwd_module.listener, name="Wake-Word-Detection-Thread")
            wwd_thread.start()
            wwd_thread.join()  # WAITING wwd_thread TO STOP EXECUTING
        except Exception as e:
            print("An error occurred while starting Wake Word Detection thread")

        # CALLING TEXT-TO-SPEECH FOR GREETING THE USER
        # tts_module.tts(greeting_skill.greeting())
        subprocess.call(["/usr/bin/mpg123", 'assets/audible-feedback/Assistant-Module_Assets_listen.mp3'], stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)

        # CALLING AUTOMATIC-SPEECH-RECOGNITION TO RECOGNIZE COMMAND
        try:
            print("\n{} Automatic Speech Recognition initializing {}".format(
                '='*20, '='*20))
            spoken = asr_module.asr()
            spoken = str(spoken).lower()
            print(spoken)
        except Exception as e:
            print(
                "\nError encountered. Couldn't connect with Automatic Speech Recognition.\n" + str(e))

        # AUDIBLE PROCESSING SOUND
        subprocess.call(["mpg321", 'assets/audible-feedback/Assistant-Module_Assets_processing.mp3'], stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)

        # PASSING THE COMMAND TO INTENT CLASSIFIER
        print("\n{} Classifying Intent {}".format(
            '='*20, '='*20))
        matched_intent = intent_classifier_module.classify(spoken)
        print("Matched Intent: {}".format(matched_intent))

        # MATCHING THE INTENT WITH CORRESPONDING SKILL
        statement = spoken.lower()
        skill_response = None
        print("\n{} Skill match starting {}".format(
            '='*20, '='*20))

        # POSSIBLE LABELS {'LAUNCH_APPLICATION', 'MUSIC_PLAYBACK_RANDOM_SONG','MUSIC_PLAYBACK_ALBUM_SONG', 'UNDEFINED'} etc
        if matched_intent == 'UNDEFINED':
            print("Nothing received as command")
            # AUDIBLE FALLBACK SOUND
            subprocess.call(["mpg321", 'assets/audible-feedback/Assistant-Module_Assets_fallback.mp3'], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)

        elif matched_intent in ['MUSIC_PLAYBACK_ALBUM_SONG', 'MUSIC_PLAYBACK_SPECIFIC_SONG', 'MUSIC_PLAYBACK_RANDOM_SONG']:
            print("Matched Skill: {}".format(matched_intent))
            skill_response = music_playback_skill.music_playback(
                statement, matched_intent)

        elif matched_intent == 'LAUNCH_APPLICATION':
            print("Matched Skill: {}".format(matched_intent))
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
