#coding:utf-8
import urllib2
import urllib
import re
import os
import time
import sys
from HTMLParser import HTMLParser
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

start_url = 'https://cn.bing.com'
file_uri = 'D:\\Downloads\\wallpaper\\'
error_file = 'D:\\Downloads\\wallpaper\\error.log'

def read_file():
	fp = file("../img/html.txt","r")
	content = fp.read()
	fp.close()
	return content

def  get_html_content(url):
	print "fecthing:" + url
	content = ''
	try:
		content = urllib2.urlopen(url).read()
	except:
		print "get html error!"
	return content

def get_jpg_list(content):
	#reg = r'(?:\'|\")http[^ ]+?(?:jpg!mid|jpg|png)(?:\'|\")'
	reg = r'g_img={url\:[^,]+(?:\'|\")'
	imgrgx = re.compile(reg)
	imglist = re.findall(imgrgx,content)
	return imglist

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

def schedule_file(a, b, c):
	per = 100.0 * a * b / c
	if per > 100.0 :
		per = 100
	print '%.2f%%' % per

def download_file_re(uri):
	name = file_uri + get_now_time_str() + uri[uri.rfind('.'):len(uri)]

	if os.path.exists(name):
		return

	try:
		urllib.urlretrieve(uri, name, schedule_file)
	except Exception, e:
		print e
		print "get error while download!"

'''
class Render(QWebPage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self._loadFinished)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def _loadFinished(self, result):
		print("rend over")
		self.frame = self.mainFrame()
		self.app.quit()
'''

#download_file('https:/az/hprichbg/rb/TowerBridgeVideo_ZH-CN9340207782_1920x1080.jpg')

if __name__ == '__main__':
	error_fp = file(error_file, "a+")
	error_fp.write("\n")
	error_fp.write(get_now_time_str())
	error_fp.write("\n")

	html_content = get_html_content(start_url)
	#rd = Render(start_url)
	#html_content = rd.frame.toHtml().toUtf8()

	jpg_list = get_jpg_list(html_content)
	for jpg_url in jpg_list:
		error_fp.write(jpg_url)
		error_fp.write("\n")

		tag = '"'
		start = jpg_url.find(tag)
		if start == -1:
			tag = '\''
			start = jpg_url.find(tag)

		end = jpg_url.rfind(tag)
		jpg_url = jpg_url[start+1:end]
		jpg_url = start_url + jpg_url
		error_fp.write(jpg_url)
		error_fp.write("\n")

		download_file(jpg_url)
		command_str = 'SetBackgroud.exe ' + get_local_file_name(jpg_url)
		
		os.system(command_str)
	error_fp.close()

'''
	image_url = jpg_list[0]

	tag = '"'
	start = image_url.find(tag)
	if start == -1:
		tag = '\''
		start = image_url.find(tag)

	end = image_url.rfind(tag)
	image_url = image_url[start+1:end]
	image_url = "https:" + image_url
	error_fp.write(image_url)
	error_fp.write("\n")
	download_file(image_url)
	error_fp.close()
'''
