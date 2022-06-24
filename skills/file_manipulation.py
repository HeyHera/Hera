def move_copy_or_delete_file(command):
    import shutil
    import numpy as np
    import os
    import yaml
    command = str(command).lower()
    words = command.split()
    os_username = os.getlogin()
    try:
        with open('configs/'+os_username+'.yaml', 'r') as config_file:
            yaml_load = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)
        exit()
    import tts.speak as tts_module
    import nlu.entity_extraction.entity_extractor as entity_extractor_module
    entity = entity_extractor_module.extract(model_test_sentence=command, entity_label="FILE_MANIPULATION",
                                             model_path="nlu/entity_extraction/output/file_manipulation/model-best")
    source = entity
    try:
        file_list = os.listdir(+source)
    except FileNotFoundError:
        gtts_text = "Sorry! An error encountered"
        gtts(text=gtts_text)
        return
    modified_time_of_new_file = np.format_float_scientific(
        os.path.getmtime(GV.pathDelimiter+source+"/"+file_list[0]))
    filename = file_list[0]
    for i in file_list:
        mtime = np.format_float_scientific(
            os.path.getmtime(GV.pathDelimiter+source+"/"+i))
        if mtime > modified_time_of_new_file:
            modified_time_of_new_file = mtime
            filename = i
    if "delete" in command or "remove" in command:
        os.remove(GV.pathDelimiter+source+"/"+filename)
        gtts_text = "Deleted " + filename + " from " + source
        gtts(text=gtts_text)
    elif "copy" in command:
        destination = words[words.index("to")+1].title()
        shutil.copyfile(GV.pathDelimiter+source+"/"+filename,
                        GV.pathDelimiter+destination+"/"+filename)
        gtts_text = "Copied " + filename + " from " + source + " to " + destination
        gtts(text=gtts_text)
    elif "move" in command:
        destination = words[words.index("to")+1].title()
        shutil.move(GV.pathDelimiter+source+"/"+filename,
                    GV.pathDelimiter+destination+"/"+filename)
        gtts_text = "Moved " + filename + " from " + source + " to " + destination
        gtts(text=gtts_text)
    else:
        gtts_text = "Sorry! An error encountered"
        gtts(text=gtts_text)


if __name__ == '__main__':
    spoken = greeting()
    print(spoken)
