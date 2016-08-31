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
conn_inst = None

def  get_html_content(url):	
	content = ''
	try:
		content = urllib2.urlopen(url).read()
	except:
		print "get html error!"
	return content

def load_local_translate(word, is_ch):
	if conn_inst == None:
		return None	
	command = ""
	if is_ch == True:
		command = "SELECT explain FROM Translate WHERE word='%s'" % word
	else:
		command = "SELECT explain FROM Words WHERE word='%s'" % word
	cursor = conn_inst.execute(command)
	result = ()
	for cown in cursor:
		result = result + cown	

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
	zhPattern = re.compile('[^\u4e00-\u9fa5]+')
	match = zhPattern.search(t_str)
	if match:
		return True
	else:
		return False

def insert_translate(key, fetch_data, is_ch):
	if conn_inst == None:
		return	
	explain = ""
	for item in fetch_data:		
		if item[1] == None:
			break
		if type(item[1]) == list or type(item[1]) == tuple:
			for exp in item[1]:				
				explain = explain + exp + ","
		else:
			explain = explain + item[1] + ","
	if explain == "":
		return
	command = ""	
	if is_ch == True:
		command = "INSERT INTO Translate VALUES ('%s', '%s')" % (key.decode("utf8"), explain)
	else:
		command = "INSERT INTO Words VALUES ('%s', '%s')" % (key.decode("utf8"), explain)	
	conn_inst.execute(command)
	conn_inst.commit()
	
def show_translate(keyword):
	keyword = keyword.decode("GBK")	
	keyword = keyword.encode("utf8")
	isHasChinese = has_chinese_character(keyword)
	result = None
	if conn_inst != None:
		result = load_local_translate(keyword, isHasChinese)

	is_from_net = False
	if result == None:
		result = fecth_net_translate(keyword)
		if len(result) > 1:
			is_from_net = True

	if result == None:
		print(u"没有找到翻译")
		sys.exit()

	for k in result:
		print("%s:" % k[0].encode("GBK", 'ignore'))
		if type(k[1]) == list or type(k[1]) == tuple:
			for exp in k[1]:
				print('  '),
				print(exp.encode("GBK", 'ignore'))
		elif type(k[1]) == type(None):
			continue
		else:
			print(k[1].encode("GBK", 'ignore'))

	if is_from_net == True:
		insert_translate(keyword, result, isHasChinese)
		
def cycle_show_translate():
	while True:
		print(u'请输入关键词(按q退出)：')
		key = raw_input()
		if key == 'q' or key == 'exit' or key == '':
			break
		show_translate(key)
		
if __name__ == '__main__':
	dirname,fileName = os.path.split(os.path.abspath(sys.argv[0]))
	dict_path = dirname + dict_path
	if os.path.exists(dict_path):
		conn_inst = sqlite3.connect(dict_path)
	
	if len(sys.argv) <= 1:
		cycle_show_translate()
	else:
		show_translate(sys.argv[1])

	if conn_inst != None:
		conn_inst.close()	


