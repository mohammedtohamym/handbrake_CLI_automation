import os


rootdir = r"U:\Udemy - The Complete Android 14 Developer Course - Java & Kotlin 2024-1"
# make a folder named converted inside all of the folders in root directorey


# perform the conversion on files only in the original folders
# and put them in the respective 'converted' subfolder
for subdir, dirs, files in os.walk(rootdir):
    if subdir.endswith('converted'):
        os.unlink(subdir)

