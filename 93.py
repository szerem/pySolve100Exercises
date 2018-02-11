import os, glob


file_list = len(glob.glob("subdirs/**/*.py", recursive=True))
print(file_list)
