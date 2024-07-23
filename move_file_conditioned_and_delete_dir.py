import os


rootdir = r"U:\Udemy - The Web Developer Bootcamp 2023 2023-9"
# make a folder named converted inside all of the folders in root directorey




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

