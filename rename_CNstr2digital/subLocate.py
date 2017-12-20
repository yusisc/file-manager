# -*- coding: utf-8 -*-
import sys


CN_NUMbegin = {

    u'一': 1,
    u'二': 2,
    u'三': 3,
    u'四': 4,
    u'五': 5,
    u'六': 6,
    u'七': 7,
    u'八': 8,
    u'九': 9,


    u'壹': 1,
    u'贰': 2,
    u'叁': 3,
    u'肆': 4,
    u'伍': 5,
    u'陆': 6,
    u'柒': 7,
    u'捌': 8,
    u'玖': 9,

    # u'貮': 2,
    # u'两': 2,
    u'十': 10,
    u'拾': 10,
}
CN_other = {
    u'百': 100,
    u'佰': 100,
    u'千': 1000,
    u'仟': 1000,
    u'万': 10000,
    u'萬': 10000,
    u'亿': 100000000,
    u'億': 100000000,
    u'兆': 1000000000000,

    u'〇': 0,
    u'零': 0,
}

CN_NUM_char = CN_NUMbegin.copy()
CN_NUM_char.update(CN_other)

def containChineseNumChar(str):
    # print(sys._getframe().f_code.co_name)
    for i in CN_NUMbegin:
        if str.find(i) != -1:
            return True

def findSubCnNumStrIndex(str = ''):
    # str = "abcd"
    print(sys._getframe().f_code.co_name)
    print(str)
    subCnNumHeadIndex = -1
    subCnNumTailIndex = -1
    for i in str:
        if i in CN_NUMbegin:
            subCnNumHeadIndex = str.find(i)
            break
    if subCnNumHeadIndex != -1:
        subCnNumTailIndex = subCnNumHeadIndex
    point = subCnNumHeadIndex
    # print("flag1")

    try:
        while str[point + 1] in CN_NUM_char:
            subCnNumTailIndex += 1
            point += 1
        print("flag2",subCnNumHeadIndex,subCnNumTailIndex)
    except:
        pass
    return subCnNumHeadIndex,subCnNumTailIndex

