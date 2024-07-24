import os
import subprocess

def Move_converted_file_and_delete_converted(root):
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


rootdir = r"O:\handbrake CLI"
handbrake_dir = r"O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64\folder1\HandBrakeCLI.exe"

preset_720 = "Very Fast 720p30"
preset_1080 = "Very Fast 1080p30"

# make a folder named converted inside all of the folders in root directorey
directories = []
for subdir, dirs, files in os.walk(rootdir):
    directories.append(subdir)
for item in directories:
    this_is_converted_dir = item.endswith('converted')
    converted_dir = item + r'\converted'
    converted_dir_existes = os.path.isdir(converted_dir)
    if not converted_dir_existes and not this_is_converted_dir:
        os.mkdir(converted_dir)

# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
for subdir, dirs, files in os.walk(rootdir):
    if not subdir.endswith('converted'):
        for file in files:
            if file.endswith((".mp4",".mkv")):
                #add if statemtent here to replace mkv with mp4
                file_path = subdir + '\\' + file
                if file.endswith(".mkv"):
                    file = file.removesuffix(".mkv")+ ".mp4"
                converted_path = subdir + '\\converted\\' + file
                
                #handbrake command
                handbrake_command = [handbrake_dir,
                "-i",f"{file_path}", "-o",f"{converted_path}",
                "--preset" ,f"{preset_720}" ,"--crop-mode" ,"none"]
                subprocess.run(handbrake_command, shell=True)




for subdir, dirs, files in os.walk(rootdir):
    if not subdir.endswith('converted'):
        for file in files:
            if file.endswith((".mp4",".mkv")):
                file_path = subdir + '\\' + file
                os.unlink(file_path)

Move_converted_file_and_delete_converted(rootdir)
