#!/usr/bin/python3
from lfi import *  # use our lfi module

# create a list of files you want to collect and put into "files"
# Below collects all the files and mirrors the directory structure
for line in open('files'):
    line = line.strip()
    try:
        source = get_source(line)
    except:
        None
    if source:
        save_file(line, source)

