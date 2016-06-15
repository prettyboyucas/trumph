# -*- coding: utf-8 -*-
import os

def findFile(path,key):
    result=[]
    resultFiles=[os.path.join(path,x) for x in os.listdir(path) if os.path.isfile(os.path.join(path,x)) and key in x]
    dictPaths=[os.path.join(path,x) for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))]

    if dictPaths==[]:
        return resultFiles
    else:
        for i in dictPaths:
            result=result+findFile(i,key)
        return resultFiles+result

def saveResult(path,keys,files):
    with open(r'C:\Users\Kenkon\Desktop\findResult.txt','w',encoding='utf-8') as f:
        f.write('Path:' + path + '\t' + 'Key:')
        for key in keys:
            f.write(key+' ')
        f.write('\n')
        f.write('==================  %d   Results found.==================\n' % len(files))
        for i in files:
            f.write(i+'\n')

def main():
    path=input("Please input the path:")
    keys=input("Please input the key:").split(',')
    files=[]
    for key in keys:
        files=files+findFile(path,key)
    saveResult(path,keys,files)

if __name__ == '__main__':
    main()