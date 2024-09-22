import Handbrake_CLI_Script_Functions as hpf
import os

# rootdir = r"U:\Sofware Engineering\Flutter\Tharwat samy collection\Master Git & GitHub Essential Skills for Developers[Arabic]"
# rootdir = r"O:\handbrake place holder"
rootdir = input("enter the folder locaiton: ")
handbrake_dir = r"C:\Users\onetw\OneDrive\Desktop\handbrake script\handbrake_CLI_automation\HandBrakeCLI-1.8.2-win-x86_64\HandBrakeCLI.exe"

preset_720 = "Very Fast 720p30"
preset_1080 = "Very Fast 1080p30"

frame_rate_30 = "30"
frame_rate_60 = "60"

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
# user_input_frame_rate_warning = input("this conversion will result in 30fps only\n press 0 to continue or 9 to abort")
# if user_input_frame_rate_warning == '0':
#     print("starting..")
# elif user_input_frame_rate_warning == '9':
#     print("aborting ..")
#     exit()
# else:
#     print("invalid input")
#     exit()
user_input_frame_rate = input("choose the framerate: \n 1 for 30fps\n 2 for 60fps\n or 3 to enter the frame rate: ")
if user_input_frame_rate == '1':
    frame_rate = frame_rate_30
elif user_input_frame_rate == '2':
    frame_rate = frame_rate_60
elif user_input_frame_rate == '3':
    frame_rate = input("enter frame rate (flaot between 1 and 100): ")
    if frame_rate not in range(1,100):
        print("invalid input")
        exit()
else:
    print("invalid input")
    exit()


hpf.Converions_Init(rootdir, preset)
# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
hpf.Convert_with_handbrake_CLI(rootdir, handbrake_dir, preset, frame_rate)
hpf.Delete_original_files(rootdir)
hpf.Move_converted_files_and_delete_converted_dirs(rootdir)
hpf.Mark_as_finished(rootdir)
hpf.Detele_convertsion_history(rootdir)