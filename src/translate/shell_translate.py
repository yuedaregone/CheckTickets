#coding:utf-8
import sys
import json
import urllib2
import urllib
import re
import os
import sqlite3

request_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=cmd-translation&key=50036382&type=data&doctype=json&version=1.1&q='
dict_path = "/yhDict.db"

def get_html_content(url):	
	content = ''
	try:
		content = urllib2.urlopen(url).read()
	except:
		print "get html error!"
	return content

def load_local_translate(word):
	conn = sqlite3.connect(dict_path)
	command =  "SELECT explain FROM Words WHERE word='%s'" % word
	cursor = conn.execute(command)
	result = ()
	for cown in cursor:
		result = result + cown		
	conn.close()

	if len(result) == 0:
		return None
	return [(u"本地释义", result)]

def fecth_net_translate(word):
	json_data = get_html_content(request_url + urllib.quote(word))
	if json_data == '':
		return None
	
	json_data = json.loads(json_data)
	
	if json_data["errorCode"] != 0:
		print("Error!")
		return None

	result = []
	if json_data.has_key("translation"):
		result.append((u"翻译", json_data["translation"]))

	if json_data.has_key("basic"):
		result.append((u"基本释义", json_data["basic"]["explains"]))

	if json_data.has_key("web"):
		result.append((u"网络释义", None))
		for tlist in json_data["web"]:
			result.append((tlist["key"], tlist["value"]))		
	return result	

def has_chinese_character(t_str):
	zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
	match = zhPattern.search(t_str)
	if match:
		return True
	else:
		return False


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print("Parameter Error!")
		sys.exit()

	dirname,fileName = os.path.split(os.path.abspath(sys.argv[0]))
	dict_path = dirname + dict_path	

	keyword = sys.argv[1]
	result = None
	if os.path.exists(dict_path) and not has_chinese_character(keyword):
		result = load_local_translate(keyword)

	if result == None:
		result = fecth_net_translate(keyword)

	if result == None:
		print(u"没有找到翻译")
		sys.exit()

	for k in result:
		print("%s:" % k[0])
		if type(k[1]) == list or type(k[1]) == tuple:
			for exp in k[1]:
				print('  '),
				print(exp)
		elif type(k[1]) == type(None):
			continue
		else:
			print(k[1])
		#print("\n")
		

	
		

