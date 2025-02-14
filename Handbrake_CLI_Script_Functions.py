import os
import subprocess
import json

def Converions_Init(root, preset):
    Create_converted_dirs(root)
    if not os.path.isfile(root+r'\data.json'):
        with open(root+r'\data.json', 'w') as data_file:
            data = {'converted_files':['handbrake' +f'{preset}']}
            json.dump(data, data_file)

def Update_conversion_history(root,converted_file):
    with open(root+r'\data.json', 'r+') as data_file:
        history = json.load(data_file)
        history['converted_files'].append(converted_file)
        data_file.seek(0)
        json.dump(history,data_file)

def Check_history(root, converted_file):
    with open(root+r'\data.json', 'r') as data_file:
        history = json.load(data_file)
        if converted_file in history['converted_files']:
            return True

def Create_converted_dirs(root):
    # make a folder named converted inside all of the folders in root directorey
    directories = []
    for subdir, dirs, files in os.walk(root):
        directories.append(subdir)
    for item in directories:
        this_is_converted_dir = item.endswith('converted')
        converted_dir = item + r'\converted'
        converted_dir_existes = os.path.isdir(converted_dir)
        if not converted_dir_existes and not this_is_converted_dir:
            os.mkdir(converted_dir)

def Convert_with_handbrake_CLI(root, handbrake, preset, frame_rate):
    for subdir, dirs, files in os.walk(root):
        if not subdir.endswith('converted'):
            for file in files:
                if file.endswith((".mp4",".mkv",".ts")):
                    #add if statemtent here to replace mkv with mp4
                    file_path = subdir + '\\' + file
                    if file.endswith(".mkv"):
                        file = file.removesuffix(".mkv")+ ".mp4"
                    if file.endswith(".ts"):
                        file = file.removesuffix(".ts")+ ".mp4"
                    converted_path = subdir + '\\converted\\' + file
                    if Check_history(root,converted_path):
                        continue
                    if os.path.isfile(converted_path):
                        os.unlink(converted_path)
                    #handbrake command
                    handbrake_command = [handbrake,
                    "-i",f"{file_path}", "-o",f"{converted_path}",
                    "--preset" ,f"{preset}" ,"--rate", f"{frame_rate}","--crop-mode" ,"none"]
                    subprocess.run(handbrake_command, shell=True)
                    Update_conversion_history(root,converted_path)

def Delete_original_files(root):
    for subdir, dirs, files in os.walk(root):
        if not subdir.endswith('converted'):
            for file in files:
                if file.endswith((".mp4",".mkv",".ts")):
                    file_path = subdir + '\\' + file
                    os.unlink(file_path)

def Move_converted_files_and_delete_converted_dirs(root):
    for subdir, dirs, files in os.walk(root):
        if subdir.endswith('converted'):
            for file in files:
                before_move_path = subdir + '\\' + file
                if file.endswith(".mp4"):
                    after_move_path = subdir.removesuffix('\\converted') + '\\' + file
                    os.rename(before_move_path , after_move_path)
                else:
                    os.unlink(before_move_path)
            os.rmdir(subdir)  

def Mark_as_finished(root):
    if not os.path.isfile(root+r'\handbrake done.txt'):
        with open(root+r'\handbrake done.txt', "w") as file:
            file.write("hand brake done")

def Detele_convertsion_history(root):
    os.unlink(root+r'\data.json')
