import os
import re

folder_path = '/home/ravikansal/Desktop/learn/Video/Tech/ES6(copy)'
files = os.listdir(folder_path)  # get files from the source folder

prefix_to_remove = r'ES6 and Typescript Tutorial - '

for file in files:
    full_path = os.path.join(folder_path, file)  # getting full path of file
    new_name = re.sub(prefix_to_remove, '', full_path)  # replace the name
    os.rename(full_path, new_name)  # Rename

    print(f'Renamed: {full_path} -> {new_name}')

    # print(f'{file}')
    # print(f'{full_path}')
    # print(f'{new_name}')
    # print('--'*20)

print('Done')
