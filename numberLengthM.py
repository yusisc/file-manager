#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
This makes the length of numbers contented in file names of the same foloder equal. For example there are files
"a9.mp3" and "b10.mp3" in the same folder. This python script going to make these files be "a09.mp3" and "b10.mp3",
 respectly.
'''
import re
import os
import shutil

def strPattern(str='abc1234abc123.mp44'):
    '''
    :param str:
    :return: a triple. First element flag the string start with number or other character. if flag == 0 string start with
    number.
    '''
    strPat = []
    subListed = re.findall('(\d+|[^\d]+)',str)
    for ii in subListed:
        strPat.append(len(ii))
    if re.match('\d',str):
        flag = 0
    else:
        flag = 1
    return (flag, strPat)

def findGeneralPattern(flag_and_strPat0, flag_and_strPat1):
    if flag_and_strPat0[0] != flag_and_strPat1[0]:
        print('***different pattern!!!')
        print('***', flag_and_strPat0)
        print('***', flag_and_strPat1)
        # input('ctrl + c to break')
        return -1
    else:
        if len(flag_and_strPat0[1]) > len(flag_and_strPat1[1]):
            (flag_and_strPat0, flag_and_strPat1) = (flag_and_strPat1, flag_and_strPat0)
        for ii in range(len(flag_and_strPat0[1])):
            if flag_and_strPat0[1][ii] < flag_and_strPat1[1][ii]:
                flag_and_strPat0[1][ii] = flag_and_strPat1[1][ii]
    return flag_and_strPat0

path = r'c:\test'
for pa,dirs,files in os.walk(path):
    if len(files) == 0:
        continue
    patternGeneral = ''
    for file in files:
        # find the location of the dot in file name
        for dot in re.finditer('\.',file):
            dotLocate = dot.start()
        fileFore = file[:dotLocate]
        fileAft = file[dotLocate:]
        # file name was splited
        pattern = strPattern(fileFore)
        if patternGeneral == '':
            patternGeneral = pattern
        else:
            patternGeneral = findGeneralPattern(pattern,patternGeneral)
            if patternGeneral == -1:
                break
    if patternGeneral == -1:
        continue
    #     print(patternGeneral)
    # print('********************************************************')
    if patternGeneral[0] == 0:
        expectLenLoc = 0
    else:
        expectLenLoc = 1
    for file in files:
        numbLenLoc = expectLenLoc
        for dot in re.finditer('\.',file):
            dotLocate = dot.start()
        fileFore = file[:dotLocate]
        fileAft = file[dotLocate:]
        fileForeSeped = re.findall('(\d+|[^\d]+)',fileFore)
        while numbLenLoc < len(patternGeneral[1]):
            fileForeSeped[numbLenLoc] = fileForeSeped[numbLenLoc].zfill(patternGeneral[1][numbLenLoc])
            numbLenLoc += 2
        fileForeNew = ''.join(fileForeSeped)
        fileNew = fileForeNew + fileAft
        if fileNew != file:
            print(file, ' -> ', fileNew)
            print('going to apply to file system ...')
            shutil.move(os.path.join(pa,file),
                        os.path.join(pa,fileNew))
        else:
            print('nothing to do.')
    print('done for folder %s' % pa)

