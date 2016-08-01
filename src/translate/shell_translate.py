#coding:utf-8
import sys
import json
import urllib2
import urllib

request_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=cmd-translation&key=50036382&type=data&doctype=json&version=1.1&q='

def  get_html_content(url):	
	content = ''
	try:
		content = urllib2.urlopen(url).read()
	except:
		print "get html error!"
	return content


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print("Parameter Error!")
		sys.exit()
	
	json_data = get_html_content(request_url + urllib.quote(sys.argv[1]))
	if json_data == '':
		sys.exit()	
	
	json_data = json.loads(json_data)
	
	if json_data["errorCode"] != 0:
		print("Error!")
		sys.exit()

	print(u"翻译：")	
	for tl in json_data["translation"]:
		print(tl),
		print("\t"),
	print("\n")


	if not json_data.has_key("basic"):
		sys.exit()

	print(u"基本释义：")
	for tl in json_data["basic"]["explains"]:
		print(tl)
	print(" ")

	if not json_data.has_key("web"):
		sys.exit()
	
	print(u"网络释义：")
	for tlist in json_data["web"]:
		print(tlist["key"]),
		print(u"："),
		for tl in tlist["value"]:	
			print(tl)
		print(" ")
		

