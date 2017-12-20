import os,sys
from rename_CNstr2digital.subLocate import *
from rename_CNstr2digital.cn2digi import *
# print(findSubCnNumStrIndex('五个六十七'))

def name2new(oldNmae = ''):
    newName = oldNmae
    while findSubCnNumStrIndex(newName) != (-1, -1):
        # substituteSub(str,findSubCnNumStrIndex(str))
        CnNumStr = newName[findSubCnNumStrIndex(newName)[0]:findSubCnNumStrIndex(newName)[1]+1]
        newName = newName.replace(CnNumStr,str(cn2digi(CnNumStr)))
    return newName


def renAllDirectContainedFiles(thePath):
    '''
    rename all the files,exclude directories, in subordinated to the given path.
    :param thePath:
    :return:
    '''
    # print(sys._getframe().f_code.co_name)
    for i in os.listdir(thePath):
        # if os.path.isfile(os.path.join(thePath,i)):
        if containChineseNumChar(i):
            os.rename(os.path.join(thePath,i),os.path.join(thePath,name2new(i)))



if __name__ == "__main__":
    '''
    rename all the files,exclude directories, in subordinated to the given path.
    '''
    path = "C:\\test"
    renAllDirectContainedFiles(path)