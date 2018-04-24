#-*-coding:utf-8-*- 
import Image
import os
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList) 
    return fileList

list = GetFileList("./img/", [])
for f in list:
    im = Image.open(f)
    w, h = im.size    
    #im.thumbnail((int(w * 0.8), int(h * 0.8)))
    #im.save(f + ".small", 'png')
    out = im.resize((int(w * 0.8), int(h * 0.8)),Image.ANTIALIAS) 
    out.save("./out/" + f, 'png')
    

#
#w, h = im.size
#im.thumbnail((w//2, h//2))
#im.save('/Users/michael/thumbnail.jpg', 'jpeg')