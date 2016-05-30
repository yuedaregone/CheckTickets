#coding:utf-8
import urllib2
import urllib
import re
import os

start_url = 'http://girl-atlas.com/'

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
	reg = r'(?:\'|\")http[^ ]+?(?:jpg!mid|jpg|png)(?:\'|\")'
	imgrgx = re.compile(reg)
	imglist = re.findall(imgrgx,content)
	return imglist

def get_url_list(content):
	reg = r'(?:\'|\")http[^ ]+?(?:\'|\")'
	imgrgx = re.compile(reg)
	imglist = re.findall(imgrgx,content)
	return imglist

def download_file(uri):	
	l = uri.split('/')
	name = '/home/yue/workspace/python/img/' + l[len(l) - 1]

	if os.path.exists(name):
		return
		
	try:
		f = urllib2.urlopen(uri)
		data = f.read() 
		with open(name, "wb") as code:
			code.write(data)
	except Exception, e:
		print "get error while download!"
	
	

def is_except_str(content):
	if len(content) < 14:
		return False
	reg = r'(?:\'|\")http.+?\.(?:jpg!mid|jpg|png|css|js)(?:\'|\")'
	imgrgx = re.compile(reg)
	imglist = re.match(imgrgx,content)
	if imglist:
		return True	
	return False
	


to_fetch_urls = [start_url]
has_fetch_urls = []

while to_fetch_urls: 
	html = get_html_content(to_fetch_urls[0])	
	
	if len(html) < 5:
		temp_url = to_fetch_urls[0]
		del to_fetch_urls[0]
		to_fetch_urls.append(temp_url)
		continue

	print("fecth url success!")
	has_fetch_urls.append(to_fetch_urls[0])
	del to_fetch_urls[0]
	

	jpg_list = get_jpg_list(html)
	for jpg in jpg_list:
		jpg = jpg.strip('\"')
		jpg = jpg.strip('\'')
		print "downloading:" + jpg
		download_file(jpg)
		print "download ok!"

	
	url_list = get_url_list(html)	
	for url in url_list:		
		if not is_except_str(url):
			if url not in to_fetch_urls and url not in has_fetch_urls:
				url = url.strip('\"')
				url = url.strip('\'')
				to_fetch_urls.append(url)

	#for i in to_fetch_urls:
	#	print(i)
	



