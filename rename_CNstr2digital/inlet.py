# -*- coding: utf-8 -*-
from rename_CNstr2digital.listOutDirectories import listOutDirsRecur
from rename_CNstr2digital.renameDirctContained import renAllDirectContainedFiles

'''
To replace the Chinese numbers strings in the names of all the sub directories and files, recursively contained in the given path.
'''
path = r'C:\test'
dirList = listOutDirsRecur(path)
for i in range(len(dirList)-1,-1,-1):
    renAllDirectContainedFiles(dirList[i])
    # print(dirList[i])
