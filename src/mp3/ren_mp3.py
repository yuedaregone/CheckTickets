#coding:utf-8

import eyed3
import sys
import os

def GetMp3Name(name):
	mp3 = eyed3.load(name)
	return mp3.tag.title

if __name__ == '__main__':
	originName = sys.argv[1].decode("GBK")
	fileName = GetMp3Name(originName)
	if fileName != None:
		print(fileName)
		command = "ren " + originName + " " + fileName + ".mp3"		
		os.system(command.encode("GBK"))
