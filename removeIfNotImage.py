import os

def removeExceptImg(path=''):
    '''
    remove files except it is image.
    :param path:
    :return:
    '''
    lst = os.walk(path)
    for i in lst:
        print('###############', i)
        for j in i[2]:

            pathTemp = os.path.join(i[0], j)
            print(pathTemp)
            if os.path.isfile(pathTemp):
                if not (pathTemp[-4:] == '.jpg' or pathTemp[-5:] == '.jpeg'):
                    os.remove(pathTemp)


if __name__ =='__main__':
    path = r'C:\test'
    removeExceptImg(path)

