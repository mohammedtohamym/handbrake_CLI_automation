import os
import subprocess

rootdir = r"D:\UI"
handbrake_dir = r"O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64\folder1\HandBrakeCLI.exe"


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
            file_path = subdir + '\\' + file
            print(file_path)
            converted_path = subdir + '\\converted\\' + file

            #handbrake command
            handbrake_command = [handbrake_dir,
                                "-i",f"{file_path}", "-o",f"{converted_path}",
                                "--preset" ,"Very Fast 1080p30" ,"--crop-mode" ,"none"]
            subprocess.run(handbrake_command, shell=True)
