import Handbrake_CLI_Script_Functions as hpf

rootdir = input("enter the folder locaiton: ")

hpf.Move_converted_files_and_delete_converted_dirs(rootdir)