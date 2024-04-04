#!/usr/bin/env python3
'''Code snippet adding regular expressions to renaming exercise'''

import os
import re

'''NB Mac OS style filepath used here'''
source_path = "/Users/username/Downloads"
file_list = os.listdir(source_path)
##print(file_list)

for file in file_list:
    if file.endswith('.zip'):
        '''find zip file names with one or more digits'''
        if re.search('\d+',file):
            '''replace digit(s) instances with the string 'digit(s)''''
            new_name = re.sub('\d+','digit(s)',file)
            os.rename(os.path.join(source_path, file), os.path.join(source_path, new_name))
            print(f"Renamed {file} to {new_name}")
