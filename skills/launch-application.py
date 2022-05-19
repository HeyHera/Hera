# LAUNCH PRELISTED APPLICATIONS
# COMMAND LIKE: "Launch Google Chrome"
# "Open Weather"

def launch_applications(command):
    import subprocess
    import webbrowser
    import difflib

    command = str(command).lower()
    app_to_launch = ""
    application_list = ['FireFox,Web Browser', 'Google Chrome',
                        'Weather', 'Calculator', 'Terminal,Command Prompt', 'Files,Explorer']
    app_dist = {
        'Firefox': 'firefox',
        'Google Chrome': 'google-chrome',
        'Weather': 'gnome-weather',
        'Calculator': 'gnome-calculator',
        'Terminal': 'gnome-terminal',
        'Files': 'nautilus'
    }
    if command.startswith("open"):
        app_to_launch = command.split("open")[1].strip().title()
    elif command.startswith("launch"):
        app_to_launch = command.split("launch")[1].strip().title()
    elif app_to_launch == "":
        return("Please specify the application to launch")
    else:
        print("An error occurred during pattern matching")
    closest_matched_apps = difflib.get_close_matches(
        app_to_launch, application_list)
    if len(closest_matched_apps) != 0:
        try:
            to_be_launched = closest_matched_apps[0].split(',')[0]
            print("Opening {}".format(to_be_launched))
            subprocess.call("/usr/bin/"+app_dist[to_be_launched], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
        except:
            return("Sorry! An error encountered | App")
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
            except Exception as e:
                return("Sorry! An error encountered | Sites", e)
        else:
            return("Sorry! Unable to launch")


if __name__ == '__main__':
    spoken = launch_applications("Open Command Prompt")
    # spoken = launch_applications("Launch Wikipedia")
    if spoken != None:
        print(spoken)
