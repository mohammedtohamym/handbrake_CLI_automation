import os
import subprocess

rootdir = r'O:\C drive\downloads\Compressed\HandBrakeCLI-1.8.1-win-x86_64'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(file)
## join path just puts \ man XDXDXDXDXDXD