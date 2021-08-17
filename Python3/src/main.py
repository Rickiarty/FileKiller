#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 * 
 *  Coded by Rei-Chi Lin 
 * 
"""

import os
import sys
from remove import delete_file_dir as del_f_d
from remove import format_number as format_num

def pattern_parse(short_option):
    if sys.argv[1][0] == '-'[0]:
        if len(sys.argv[1]) == 3:
            if sys.argv[1] == '-df' or sys.argv[1] == '-fd':
                return 3
            else:
                return 0
        elif len(sys.argv[1]) == 2:
            if sys.argv[1][1] == 'f'[0]:
                return 1
            elif sys.argv[1][1] == 'd'[0]:
                return 2
            else:
                return 0
        else:
            return 0
    else:
        return 0

def main():
    start_path = ''
    target_name = ''
    pattern = 0
    try:
        if len(sys.argv) == 4:
            if sys.argv[1][0] == '-':
                start_path = sys.argv[3]
                target_name = sys.argv[2]
                pattern = pattern_parse(sys.argv[1])
            else:
                print("\nERROR: Invalid argument(s) !\n\nType either '--help' or '-h' for more info.\n")
                return -4
        elif len(sys.argv) == 3:
            if sys.argv[1][0] == '-':
                start_path = os.getcwd() # get current working directory
                target_name = sys.argv[2]
                pattern = pattern_parse(sys.argv[1])
            else:
                start_path = sys.argv[2]
                target_name = sys.argv[1]
                pattern = 1
        elif len(sys.argv) == 2:
            if sys.argv[1] == '--help' or sys.argv[1] == '-h':
                help_info = "\nusage:\n\n"
                help_info += "[-(pattern)] name_of_file_or_dir_to_delete [directory_path_to_search]\n"
                help_info += "or\n"
                help_info += "--(option)\n\n"
                help_info += "e.g., -fd test ~/Downloads\n"
                help_info += "\t(to search path '~/Downloads' recursively for all files and folders named 'test' and delete)\n"
                help_info += "or -fd test\n"
                help_info += "\t(to search current working path recursively for all files and folders named 'test' and delete)\n"
                help_info += "or -d test\n"
                help_info += "\t(to search current working path recursively for all folders named 'test' and delete)\n"
                help_info += "or -f test.txt ~/Downloads\n"
                help_info += "\t(to search path '~/Downloads' recursively for all files named 'test' and delete)\n"
                help_info += "or -f test.txt\n"
                help_info += "\t(to search current working path recursively for all files named 'test.txt' and delete)\n"
                help_info += "or test.txt\n"
                help_info += "\t(the same as '-f test.txt')\n"
                help_info += "\nYou have to give the program at least 1 argument. \nIn this case, either the argument is the name of file which you want to delete under your current working folder and its sub-folder(s), or the argument is an option which you want the program to execute.\n"
                print(help_info)
                return 1
            elif sys.argv[1] == '--version':
                print('\n\tversion: ' + del_f_d.version() + '\n\t\tby Rei-Chi Lin\n')
                return 2
            else:
                pattern = 1
                target_name = str(sys.argv[1])
                start_path = os.getcwd() # get current working directory
        elif len(sys.argv) == 1:
            print("\nERROR: you MUST give at least 1 argument!\n\nType either '--help' or '-h' for usage info.\n")
            return -2
        else:
            print("\nERROR: Too many arguments !\n\nType either '--help' or '-h' for usage info.\n")
            return -3
        
        _folder_count, _file_count = del_f_d.delete_by_name_under_path(start_path, target_name, pattern)
        print("\n %s folder(s), %s file(s) were deleted.\n" % (format_num.format_number_kilo_by_kilo(_folder_count), format_num.format_number_kilo_by_kilo(_file_count)))
        return 0
    except Exception as ex:
        print("Unknown error(s) occurred.")
        return -1

if __name__ == '__main__':
    exit_code = main()
    print('(exit code: ' + str(exit_code) + ' )')
