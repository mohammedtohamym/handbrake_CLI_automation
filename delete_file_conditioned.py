import os


rootdir = r"U:\5TB\Courses\Masterclass"
# make a folder named converted inside all of the folders in root directorey


# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
for subdir, dirs, files in os.walk(rootdir):
    if not subdir.endswith('converted'):
        for file in files:
            if file.endswith(".mp4"):
                file_path = subdir + '\\' + file
                os.unlink(file_path)

