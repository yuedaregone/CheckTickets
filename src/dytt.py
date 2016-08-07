#coding:utf-8
import urllib2
import urllib
import re
import os
import time
import sys
from bs4 import BeautifulSoup

start_url = 'http://www.dytt8.net'
file_uri = './dy.txt'

def read_file():
	fp = file(file_uri,"r")
	content = fp.read()
	fp.close()
	return content

def write_file(content):
    fp = file(file_uri, "w")
    fp.write(content)
    fp.close()

def  get_html_content(url):
	print "fecthing:" + url
	content = ''
	try:
		content = urllib2.urlopen(url).read()
	except:
		print "get html error!"
	return content

def get_now_time_str():
	now = int(time.time())
	time_array = time.localtime(now)
	return time.strftime("%Y-%m-%d", time_array)

def get_local_file_name(uri):
	return file_uri + get_now_time_str() + uri[uri.rfind('.'):len(uri)]

def download_file(uri):
	name = get_local_file_name(uri)

	if os.path.exists(name):
		return

	try:
		f = urllib2.urlopen(uri)
		data = f.read()
		with open(name, "wb") as code:
			code.write(data)
	except Exception, e:
		print e
		print "get error while download!"


#download_file('https:/az/hprichbg/rb/TowerBridgeVideo_ZH-CN9340207782_1920x1080.jpg')

if __name__ == '__main__':
    #html = get_html_content(start_url)
    #write_file(html)
    content = read_file()
    soup = BeautifulSoup(content, "lxml")
    write_file(soup.prettify().encode("utf8"))
    print(soup.div.string)

		
