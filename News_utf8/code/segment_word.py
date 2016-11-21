
# coding: utf-8

# In[1]:

import os
import jieba
rootDir = '../'
seg_folder = 'segment_word'
content_folder = 'content_only'


# In[2]:

try:
    os.mkdir(rootDir+seg_folder)
    print('Create new folder "%s" '%(seg_folder))
except:
    print('Folder "%s" exist' %(seg_folder))


# In[3]:

badInputFile = open('bad_segment.txt','w')

for dirPath, dirName, fileList in os.walk(rootDir, topdown=False):
    if dirName!=[]:
        continue
    if content_folder not in dirPath:
        continue
    srcDir = ('%s%s%s' %(rootDir,seg_folder,dirPath[3:len(dirPath)].replace(content_folder,'')))
    try:
        os.mkdir(srcDir)
    except:
        pass
    for idx in range(len(fileList)):
        try:
            inputFile = ('%s/%s' %(dirPath, fileList[idx]))
            outputFile = ('%s/%s' %(srcDir, fileList[idx]))
            fp = open(inputFile, 'r').read()
            seg_lst = jieba.cut(fp)
            wp = open(outputFile, 'w').write(' '.join(seg_lst))
        except:
            badInputFile.write(inputFile+'\n')

    


# In[ ]:



