import Handbrake_CLI_Script_Functions as hpf
import os

rootdir = r"U:\placeholder\Udemy - 50 Projects In 50 Days - HTML, CSS & JavaScript 2020-11"
handbrake_dir = r"O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64\folder1\HandBrakeCLI.exe"

preset_720 = "Very Fast 720p30"
preset_1080 = "Very Fast 1080p30"

if os.path.isfile(rootdir+r'\handbrake done.txt'):
    print("Folder aleady Converted,\ndelete 'handbrake done.txt' if you wish to reconvert")
    exit()

user_input_preset = input("choos 1 for 720,\n 2 for 1080: ")
if user_input_preset == '1':
    preset = preset_720
elif user_input_preset == '2':
    preset = preset_1080
else:
    print("invalid input")
    exit()
    
hpf.Converions_Init(rootdir, preset)
# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
hpf.Convert_with_handbrake_CLI(rootdir, handbrake_dir, preset)
hpf.Delete_original_files(rootdir)
hpf.Move_converted_files_and_delete_converted_dirs(rootdir)
hpf.Mark_as_finished(rootdir)
hpf.Detele_convertsion_history(rootdir)