import os


rootdir = r"U:\Udemy - The Complete Android 14 Developer Course - Java & Kotlin 2024-1"
# make a folder named converted inside all of the folders in root directorey



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

