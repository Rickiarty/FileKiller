#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * 
 *  Coded by Rei-Chi Lin 
 * 
"""

import os
#import shutil # utilities of 'shell'
if __name__ == '__main__':
    from format_number import format_number_kilo_by_kilo
else:
    from remove.format_number import format_number_kilo_by_kilo

__version_code = '1.0.1' # version code

def version():
    return __version_code

def _delete_all_under(parent_path):
    file_system_objects = sorted(os.listdir(parent_path)) # ascendantly list all children
    for obj in file_system_objects:
        obj_path = os.path.join(parent_path, obj)
        if os.path.isdir(obj_path): # is a directory/folder
            _delete_all_under(obj_path)
            os.rmdir(obj_path)
        else: # is a file
            os.remove(obj_path)

def delete_by_name_under_path(path_to_search, name_of_file_or_dir_to_delete, pattern):
    if os.path.exists(path_to_search) and os.path.isdir(path_to_search):
            path_to_search = os.path.abspath(path_to_search)
    else:
        print('\nERROR: \n\n The process can not access the given path !\n Please check whether the path exists and whether the path is to a directory/folder.\n And check if the access to the path is permitted or not.\n')
        return 0, 0
    
    file_count = 0
    folder_count = 0
    
    file_system_objects = sorted(os.listdir(path_to_search)) # ascendantly list all children
    for obj in file_system_objects:
        obj_path = os.path.join(path_to_search, obj)
        if os.path.isdir(obj_path): # is a directory/folder
            folder_c, file_c = delete_by_name_under_path(obj_path, name_of_file_or_dir_to_delete, pattern)
            folder_count += folder_c
            file_count += file_c
    
    obj_path = os.path.join(path_to_search, name_of_file_or_dir_to_delete)
    if os.path.exists(obj_path):
        _is_dir = os.path.isdir(obj_path)
        if _is_dir and (pattern // 2 ) % 2 == 1: # target is a folder/directory AND pattern=1x
            # Recursively delete/remove a specific folder/directory. (method 1)
            _delete_all_under(obj_path) # First, delete/remove all files and sub-folders under a specific sub-folder.
            os.rmdir(obj_path) # Second, delete/remove the specific folder/directory.
            # Recursively delete/remove a specific folder/directory. (method 2)
            #shutil.rmtree(obj_path) # (shell's utilities).(remove a whole tree of files and folders under a specific path on a file system)
            folder_count += 1
        if (not _is_dir) and pattern % 2 == 1: # target is a file AND pattern=x1
            os.remove(obj_path) # Simply delete/remove a specific file.
            file_count += 1
    
    return folder_count, file_count

__author = 'Rei-Chi Lin'
def author():
    return __author

if __name__ == "__main__":
    print("ver. " + version() + " by " + author())
    folder_c, file_c = delete_by_name_under_path(os.getcwd(), '', 0)
    print("\nThe file 'delete_file_dir.py' is a program unit in module 'remove', and it should not be used in this way.")
    print("\n---\nAPI usage:\n")
    print("from remove import delete_file_dir\n")
    print("folder_count, file_count = delete_by_name_under_path(path_to_search, name_of_file_or_dir_to_delete, pattern)\n")
    print("path_to_search :: str")
    print("name_of_file_or_dir_to_delete :: str")
    print("pattern :: int")
    print("folder_count, file_count :: int, int\n---")
