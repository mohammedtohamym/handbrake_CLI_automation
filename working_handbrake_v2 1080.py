import os
import subprocess

rootdir = r"U:\Udemy - The Complete Android 14 Developer Course - Java & Kotlin 2024-1 - Copy"
handbrake_dir = r"O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64\folder1\HandBrakeCLI.exe"

preset_720 = "Very Fast 720p30"
preset_1080 = "Very Fast 1080p30"

# make a folder named converted inside all of the folders in root directorey
directories = []
for subdir, dirs, files in os.walk(rootdir):
    directories.append(subdir)
for item in directories:
    converted_dir = item + r'\converted'
    os.mkdir(converted_dir)

# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
for subdir, dirs, files in os.walk(rootdir):
    if not subdir.endswith('converted'):
        for file in files:
            if file.endswith('.mp4'):
                file_path = subdir + '\\' + file
                converted_path = subdir + '\\converted\\' + file
                
                #handbrake command
                handbrake_command = [handbrake_dir,
                "-i",f"{file_path}", "-o",f"{converted_path}",
                "--preset" ,f"{preset_1080}" ,"--crop-mode" ,"none"]
                subprocess.run(handbrake_command, shell=True)




for subdir, dirs, files in os.walk(rootdir):
    if not subdir.endswith('converted'):
        for file in files:
            if file.endswith(".mp4"):
                file_path = subdir + '\\' + file
                os.unlink(file_path)


for subdir, dirs, files in os.walk(rootdir):
    if subdir.endswith('converted'):
        for file in files:
            before_move_path = subdir + '\\' + file
            if file.endswith(".mp4"):
                # print(subdir)
                
                # print(before_move_path)

                after_move_path = subdir.removesuffix('\\converted') + '\\' + file
                # print(after_move_path)
                
                os.rename(before_move_path , after_move_path)
            else:   
                os.unlink(before_move_path)
        os.rmdir(subdir)


