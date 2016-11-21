# coding: utf-8
from bs4 import BeautifulSoup
import os
import subprocess

rootDir = '../'
try:
    os.mkdir(rootDir+'content_only')
    print('Create new folder "content_only" ')
except:
    print('Folder is exist.')


badFile = open('bad_file.txt','w')

for dirPath, dirName, fileList in os.walk(rootDir, topdown=False):
    if dirName != []:
        continue
    if len(dirPath)>11:
        continue
    srcDir =  ('../content_only%s' %dirPath[2:len(dirPath)])
    try:
        os.mkdir(srcDir)
    except:
        pass
    for idx in range(len(fileList)):
        try:
            inputFile = ('%s/%s' %(dirPath, fileList[idx]))
            soup = BeautifulSoup(open(inputFile))
            outputFile = ('%s/%s.txt' %(srcDir, fileList[idx]))
            wp = open(outputFile, 'w', encoding='UTF-8')
            for pTxt in soup.find_all('p'):
                res = ''
                for tag_c in pTxt.contents:
                    try:
                        if tag_c.get('class')==1:
                            res = res+tag_c.string
                    except:
                        res = res + tag_c
                res = res.strip('.\f\n\r\t\v')
                if len(res)==0:
                    continue
                wp.write(str(res+'\n'))
            wp.close() 
        except:
            badFile.write(inputFile+'\n')

badFile.close()

        

# print(soup.prettify())

