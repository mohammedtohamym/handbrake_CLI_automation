import os
import subprocess

rootdir = r'O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64'
handbrake_dir = rootdir+r"\HandBrakeCLI.exe"

for subdir, dirs, files in os.walk(rootdir):
 
    new_dir = os.path.join(subdir,r'\\converted\\')
    os.mkdir(new_dir)
    

    # for file in files:
    #     file_to_be_converted = os.path.join(subdir, file)
    #     if file_to_be_converted.endswith(".mp4"):
    #         new_file = subdir +"\\converted\\"+ file
            
    #         #print to degub
    #         print(new_file)
            


            #handbrake command
            # handbrake_command = [handbrake_dir,
            #                     "-i",f"{file_to_be_converted}", "-o",f"{new_file}",
            #                     "--preset" ,"Very Fast 1080p30" ,"--crop-mode" ,"none"]
            # subprocess.run(handbrake_command, shell=True)
        