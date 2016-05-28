import urllib2
import urllib
import re

url = 'http://girl-atlas.com/'


'''
check_img = urllib2.urlopen(url).read()
fp = file("../img/html.txt","wb")
fp.write(check_img)
fp.close()
'''


def get_jpg_list(content):
	reg = r'(?:\'|\")http[^ ]+?(?:jpg!mid|jpg|png)(?:\'|\")'
	imgrgx = re.compile(reg)
	imglist = re.findall(imgrgx,content)
	return imglist


def is_except_str(content):
	if len(content) < 14:
		return False
	reg = r'(?:\'|")http.+?\.(?:jpg!mid|jpg|png|css|js)(?:\'|")'
	imgrgx = re.compile(reg)
	imglist = re.match(imgrgx,content)
	if imglist:
		return True	
	return False

rgx = re.compile(r'(?:\'|\")http[^ ]+?(?:\'|\")')
print re.findall(rgx,'<a href=\'http://girl-atlas.com/a/10160528100000000602\' class="image" photo="http://girlatlas.b0.upaiyun.com/7920/20160528/1001sk4v3dpssj6wnqfs.jpg!mid" target="_blank"></a>')



fp = file("../img/html.txt","rb")
content = fp.read()
fp.close()

list1 = get_jpg_list(content)

for i in list1:	
	print(i)
	print is_except_str(i)

print(len(list1))
