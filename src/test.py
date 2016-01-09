#coding:utf-8
import urllib2
import urllib

url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&0.07869914087243213'
check_img = urllib2.urlopen(url).read()
fp = file("../img/check.jpg","wb")
fp.write(check_img)
fp.close()


