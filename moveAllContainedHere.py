#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import glob
import shutil
import pprint

def moveAllContainedHere(roott = ''):
    fileObj = open('filepathes','w',encoding='utf8')
    for path, subdirs, files in os.walk(roott):
        for name in files:
            print('reading file %s' % name)
            tempPath = os.path.join(path, name)
            tempPath = tempPath.replace(roott + '\\','')
            fileObj.writelines(tempPath + '\n')
    fileObj.close()

    relativePathes_ori = []
    relativePathes_new = []
    with open('filepathes',encoding='utf8') as fileObj:
        for line in fileObj.readlines():
            if len(line) > 100:
                print('*** The new file name well be longer than about 100 char.***')
                print('*** I recommend to make sure you are going to do that. ***')
                break
            tempRelaPath = line.rstrip('\n')
            print('processing new name of %s' % tempRelaPath)
            relativePathes_ori.append(tempRelaPath)
            relativePathes_new.append(tempRelaPath.replace('\\','_'))

    pair = list(zip(relativePathes_ori, relativePathes_new))
    # pprint.pprint(pair)

    for ii in pair:
        print('applying rename of %s to file system.' % ii[0])
        shutil.move(os.path.join(roott, ii[0]),
                    os.path.join(roott, ii[1]))

    # clean work space
    os.remove('filepathes')
    # the work is done
    print("the work is done successfully.")

if __name__ == '__main__':
    # roott is the path of directory where all file in its subfolder will be put in.
    roott = r'C:\test'
    moveAllContainedHere(roott)