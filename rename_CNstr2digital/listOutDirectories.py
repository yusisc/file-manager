# -*- coding: utf-8 -*-
import os

def dir1dir(thePath):
    lst = []
    for i in os.listdir(thePath):
        if not os.path.isfile(os.path.join(thePath,i)):
            lst.append(os.path.join(thePath,i))
    return lst

def dir1GroupOfDir(lst):
    nextLevelDirList = []
    for i in lst:
        for j in dir1dir(i):
            nextLevelDirList.append(j)
    return nextLevelDirList

def listOutDirsRecur(path =''):
    dirListAll = []
    dirList2dir = [path]
    dirListGot = []

    while dirList2dir:
        for i in dirList2dir:
            dirListAll.append(i)
        dirListGot = dir1GroupOfDir(dirList2dir)
        dirList2dir = dirListGot
        # for i in dirListGot:
        #     dirListAll.append(i)
    return dirListAll

if __name__ == '__main__':
    path = 'C:\\test'
    print(listOutDirsRecur(path))