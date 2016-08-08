#coding:utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
import webbrowser

start_url = 'http://www.dytt8.net'

def  get_html_content(url):	
	content = ''
	try:
		content = urllib2.urlopen(url).read()
	except:
		print "get html error!"
	return content

if __name__ == '__main__':
	content = get_html_content(start_url)
	#write_file(html)
	#content = read_file()		
	
	soup = BeautifulSoup(content.decode("GBK"), "html.parser")
	target_tag = soup.find("strong", text = u"2016新片精品")
	target_table = target_tag.find_next("table")
	tr_list = target_table.find_all("tr")
	index = 1
	url_list = []
	for tr_item in tr_list:
		a_list = tr_item.find_all("a")	
		print("%2d." % index),		
		print(a_list[1].string)
		index = index + 1
		url_list.append(a_list[1].attrs["href"])
	
	print(u"输入序号，跳转到网址：")
	target = raw_input()
	target_index = -1
	while (True):
		try:
			target_index = int(target)
			if (target_index > 0 and target_index <= len(url_list)):
				break
			else:
				print(u"请输入数字1 ~ %d" % len(url_list))
				target = raw_input()
		except Exception, e:		
			print(u"请输入数字1 ~ %d" % len(url_list))
			target = raw_input()
	
	target_url = start_url + "/" + url_list[target_index - 1] 	
	print(target_url)
	webbrowser.open(target_url)
