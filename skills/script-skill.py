import yaml
import os
import difflib
import subprocess

from importlib.machinery import SourceFileLoader
tts_module = SourceFileLoader("Text-To-Speech", "tts/speak.py").load_module()


command='change wallpaper'

yaml_file = open('configs/script-map-keyword.yaml', 'r')
yaml_content = yaml.safe_load(yaml_file)

def scriptMatch(speech):
    flag=0
    for key, value in yaml_content.items():
        #print(f"{key}: {value}")
        match=difflib.get_close_matches(speech, value, cutoff=0.4)
        print(len(match))
        if(len(match) != 0):
            flag=1
            print("Script found",key)
            return(key)
    if(flag==0):
       return(False) 

def msg(res):
    tts_module.tts("Found a script match, do you want to run it")
    print(res)
    

def confirm(res):
    runScript(res)
    

def runScript(script_name):
    try:
        print("Running script {}".format(script_name))
        
        subprocess.run([script_name], stdout=subprocess.DEVNULL,
  stderr=subprocess.DEVNULL)
        tts_module.tts("Script ran successfully")
        return(0)  # 0 = Success
    except:
        tts_module.tts("Sorry! An error encountered")
        return(1)


# def main()


#if __name__ == '__main__':


res=scriptMatch(command)
if res != False:
    msg(res)
    confirm(res)