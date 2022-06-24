# LAUNCH PRELISTED APPLICATIONS
# COMMAND LIKE: "Launch Google Chrome"
# "Open Weather"

def launch_applications(command):
    import subprocess
    import webbrowser
    import difflib
    from importlib.machinery import SourceFileLoader
    tts_module = SourceFileLoader(
        "Text-To-Speech", "tts/speak.py").load_module()
    entity_extractor_module = SourceFileLoader(
        "Entity_Extractor", "nlu/entity_extraction/entity_extractor.py").load_module()

    command = str(command).lower()
    entity = entity_extractor_module.extract(model_test_sentence=command, entity_label="APPLICATION", model_path="nlu/entity_extraction/output/launch_applications/model-best")
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
    closest_matched_apps = difflib.get_close_matches(
        app_to_launch, application_list, cutoff=0.4)
    if len(closest_matched_apps) != 0:
        try:
            to_be_launched = closest_matched_apps[0].split(',')[0]
            print("Opening {}".format(to_be_launched))
            subprocess.call("/usr/bin/"+app_dist[to_be_launched], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            return(0)  # 0 = Success
        except Exception as e:
            tts_module.tts("Sorry! An error encountered.")
            print("App " + str(e))
            return(1)  # 1 = Fail
    else:
        sites = ["www.gmail.com", "www.youtube.com", "www.wikipedia.com", "www.flipkart.com",
                 "www.amazon.in", "www.in.bookmyshow.com", "www.hotstar.com", "www.primevideo.com"]
        closest_matched_sites = difflib.get_close_matches(
            app_to_launch, sites, cutoff=0.3)
        if len(closest_matched_sites) != 0:
            to_be_launched = None
            try:
                to_be_launched = closest_matched_sites[0]
                print("Launching : " + to_be_launched)
                webbrowser.open_new_tab(to_be_launched)
                return(0)  # 0 = Success
            except Exception as e:
                tts_module.tts("Sorry! An error encountered")
                print("Sites " + str(e))
                return(1)  # 1 = Fail
        else:
            tts_module.tts("Sorry! Unable to launch")
            return(1)  # 1 = Fail


if __name__ == '__main__':
    skill_response = None
    skill_response = launch_applications("Open the wikipedia")
    # spoken = launch_applications("Launch Wikipedia")
    if skill_response != None:
        if skill_response == 0:
            print("Success")
        elif skill_response == 1:
            print("Fail")
        else:
            print("Return prompt")
    else:
        print("Error")