import Handbrake_CLI_Script_Functions as hpf

rootdir = r"U:\placeholder\Udemy - Python Masterclass Learn Python From Scratch, Build 23 Apps 2024-3"
handbrake_dir = r"O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64\folder1\HandBrakeCLI.exe"

preset_720 = "Very Fast 720p30"
preset_1080 = "Very Fast 1080p30"


hpf.Converions_Init(rootdir, preset_720)
# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
hpf.Convert_with_handbrake_CLI(rootdir, handbrake_dir, preset_720)
hpf.Delete_original_files(rootdir)
hpf.Move_converted_files_and_delete_converted_dirs(rootdir)
hpf.Mark_as_finished(rootdir)
# hpf.Detele_convertsion_history(rootdir)