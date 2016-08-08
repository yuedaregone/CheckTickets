#coding:utf-8
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
	while True:
		print(u'请输入关键词(按q退出)：')
		key = raw_input()
		if key == 'q' or key == 'exit':
			break

		key = key.decode("GBK")	
		key = key.encode("utf8")	
		
		json_data = get_html_content(request_url + urllib.quote(key))
		if json_data == '':
			print(u'没有发现这个词的翻译，请检查输入是否有误！')
			continue	
		
		json_data = json.loads(json_data)
		
		if json_data["errorCode"] != 0:
			print("Error!")
			continue

		print(u"翻译：")	
		for tl in json_data["translation"]:
			print(tl),
			print("\t"),
		print("\n")

		if not json_data.has_key("basic"):
			continue

		print(u"基本释义：")
		for tl in json_data["basic"]["explains"]:
			print(tl)
		print(" ")

		if not json_data.has_key("web"):
			continue
		
		print(u"网络释义：")
		for tlist in json_data["web"]:
			print(tlist["key"]),
			print(u"："),
			for tl in tlist["value"]:	
				print(tl.encode("GBK", 'ignore')),
				#tl.decode('gbk', "ignore")
			print(" ")
		print(" ")
		

