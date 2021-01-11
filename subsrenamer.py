#!/usr/bin/env python
#@author : mossaybo

from pathlib import Path
import sys
import re
import glob
import argparse

#setting variables
path = Path('.')
"""
take form user:
    video first part
    sub first part

make list of old names
find pattern from user hint
fill a dict with old:new names
rename based on dict
"""
def namecut(name, stpart):

    """
    the cutting function , takes full name and first part
    return a list [stpart, num, ndpart, ext]
    """
    ndhalf = name.split(stpart)[1]
    #get revers index of the final '.' which marks the extention
    dot_rindex = -ndhalf[::-1].index('.')
    #use it to split ndhalf another time (-1 to include the dot with the extention)
    chunk, ext = ndhalf[:dot_rindex-1], ndhalf[dot_rindex-1:]
    #make a list made of our last needed items
    num_ndpar_list = re.split('(\d+)',chunk, 1)
    num,ndpart = num_ndpar_list[1], num_ndpar_list[2]

    return [stpart, num, ndpart, ext]


def filelist(stpart):
    """
    take a beginning of a file
    creat a list of all files in current dir with that beginning
    each file is represented with a list of [stpart, num, ndpart, ext] (returned from namecut)
    """
    #get a list of all files starting with stpart (making this work was a pain)
    #the first glob is a method used in Posix paths to find files in a dir based on pattern
    #second glob is the imported glob to escap [] found in names
    filenames = list(path.glob(glob.escape(stpart)+'*'))
    files_list = []

    for i in filenames:
        files_list.append(namecut(i.name, stpart))

    return files_list

def oldnewdict(pattern_list, files_list):
    """
    take a pattern filename as list and nested lists of files (each file is represented as a list
    make newnames for files based on pattern
    fill a dictionary with old:new names
    """
    oldnew_dict = {}
    for filename in files_list:
        oldname = ''.join(filename)
        newname = pattern_list[0]+filename[1]+pattern_list[2]+filename[3]
        oldnew_dict[oldname] = newname

    return oldnew_dict

def batchrename(dic, dryrun):
    """
    take a dictionary of old / new names and rename files
    if dryrun just print what you want to do
    """
    if dryrun:
        for old, new in dic.items():
            print("renaming "+old+" to "+new)
    else:
        for old, new in dic.items():
            print("renaming "+old+" to "+new)
            Path(old).rename(new)

#handle args
parser = argparse.ArgumentParser()  #make an argument parsing object

reqArgs = parser.add_argument_group('required') #making a group to hold required args, see:stackoverflow.com/a/24181138
reqArgs.add_argument("-s",
        help="video name start string (including spaces)",
        required=True)

reqArgs.add_argument("-v",
        help="subtitle name start string (including spaces)",
        required=True)

parser.add_argument("--dry-run",
        dest='dryrun',      #store value as
        action='store_true',    #it's job is to catch true if passed else it's false by default
        help="Do nothing , print what to do and quit")

if len(sys.argv)==1:        #display full help if no arguments passed
    parser.print_help()
    sys.exit(1)

args = parser.parse_args() 
print(args)
#getting the video name pattern & subfiles list
video_patt = filelist(args.v)[0]    #picking the first result
subfiles = filelist(args.s)
#make a dictionaty
subnames_dict = oldnewdict(video_patt, subfiles)

batchrename(subnames_dict, dryrun=args.dryrun)
