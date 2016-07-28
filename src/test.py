#-*-coding:utf-8-*- 
s='中文'
print type(s) #查看s的字符类型
print s  

s.decode('utf8') #解码utf8，默认的编码方式是unicode
s.decode('gbk', "ignore") #解码utf8，忽略其中有异常的编码，仅显示有效的编码
s.decode('gbk', 'replace')
print type(s)
print s

s.encode('gb2312') ##编码为utf8
print type(s)
print s
