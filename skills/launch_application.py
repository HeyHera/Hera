# LAUNCH PRELISTED APPLICATIONS
# COMMAND LIKE: "Launch Google Chrome"
# "Open Weather"
import sys


def launch_applications(status, pipe_end, command):
    import subprocess
    import webbrowser
    import difflib
    from importlib.machinery import SourceFileLoader
    tts_module = SourceFileLoader(
        "Text-To-Speech", "tts/speak.py").load_module()
    entity_extractor_module = SourceFileLoader(
        "Entity-Extractor-Module", "nlu/entity_extraction/entity_extractor.py").load_module()

    command = str(command).lower()
    entity = entity_extractor_module.extract(model_test_sentence=command, entity_label="APPLICATION",
                                             model_path="nlu/entity_extraction/output/launch_applications/model-best")
    app_to_launch = entity
    application_list = ['Firefox,Web Browser', 'Google Chrome',
                        'Weather', 'Calculator', 'Terminal,Command Prompt', 'Files,Explorer']
    app_dist = {
        'Firefox': 'firefox',
        'Google Chrome': 'google-chrome',
        'Weather': 'gnome-weather',
        'Calculator': 'gnome-calculator',
        'Terminal': 'gnome-terminal',
        'Files': 'nautilus'
    }
    try:
        closest_matched_apps = difflib.get_close_matches(
            app_to_launch, application_list, cutoff=0.4)
    except:
        msg = "Sorry! A critical error!"
        pipe_end.send(msg)
        tts_module.tts(msg)
        pipe_end.close()
        tts_module.tts(msg)
        status.value = 1
        sys.exit()
    if len(closest_matched_apps) != 0:
        try:
            to_be_launched = closest_matched_apps[0].split(',')[0]
            msg = "Opening " + to_be_launched
            pipe_end.send(msg)
            tts_module.tts("Opening")
            subprocess.call("/usr/bin/"+app_dist[to_be_launched], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            status.value = 0  # 0 = Success
        except Exception as e:
            msg = "Sorry! An error encountered"
            pipe_end.send(msg)
            tts_module.tts(msg)
            pipe_end.close()
            tts_module.tts(msg)
            status.value = 1
            print("App " + str(e))
    else:
        sites = ["www.gmail.com", "www.youtube.com", "www.wikipedia.com", "www.flipkart.com",
                 "www.amazon.in", "https://web.whatsapp.com/", "www.in.bookmyshow.com", "www.hotstar.com", "www.primevideo.com", "https://docs.google.com/presentation/"]
        try:
            closest_matched_sites = difflib.get_close_matches(
                app_to_launch, sites, cutoff=0.3)
        except:
            msg = "Sorry! A critical error!"
            pipe_end.send(msg)
            tts_module.tts(msg)
            pipe_end.close()
            tts_module.tts(msg)
            status.value = 1
            sys.exit()
        if len(closest_matched_sites) != 0:
            to_be_launched = None
            try:
                to_be_launched = closest_matched_sites[0]
                msg = "Opening " + to_be_launched
                pipe_end.send(msg)
                tts_module.tts("Opening")
                webbrowser.open_new_tab(to_be_launched)
                status.value = 0  # 0 = Success
            except Exception as e:
                msg = "Sorry! An error encountered"
                pipe_end.send(msg)
                tts_module.tts(msg)
                pipe_end.close()
                tts_module.tts(msg)
                status.value = 1
                print("Site " + str(e))
        else:
            msg = "Sorry! Unable to launch that"
            pipe_end.send(msg)
            tts_module.tts(msg)
            pipe_end.close()
            tts_module.tts(msg)
            status.value = 1


# if __name__ == '__main__':
#     skill_response = None
#     skill_response = launch_applications("Open presentation")
#     # spoken = launch_applications("Launch Wikipedia")
#     if skill_response != None:
#         if skill_response == 0:
#             print("Success")
#         elif skill_response == 1:
#             print("Fail")
#         else:
#             print("Return prompt")
#     else:
#         print("Error")
