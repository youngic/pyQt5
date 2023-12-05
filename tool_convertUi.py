import os
import os.path

dir = './'

def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        # print(dir + os.sep + filename)
        # print(filename)
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)
    print(list)
    return list

def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'

def runMain():
    list = listUiFile()
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = f'pyuic5 -o {pyfile} {uifile}'
        print(cmd)
        os.system(cmd)

if __name__ =='__main__':
    runMain()
