#coding:utf-8
import urllib2
import urllib
import json
import Tkinter
import tkMessageBox
import time

def show(msg):
    tkMessageBox.showinfo(title='tickets', message=msg)

def isHasTicks(str):
	try:
		num = int(str)
		if num > 2:
			return True
	except ValueError:
		return False
	return False

def getTicketInfo():
	url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-02-13&from_station=PEN&to_station=SHH'
	data = urllib2.urlopen(url).read()
	json_data = json.loads(data)
	list_data = json_data["data"]["datas"]

	for item in list_data:
		print(item["from_station_name"] + ':' + item["yw_num"])
		if isHasTicks(item["yw_num"]):
			show(item["from_station_name"] + ':' + item["yw_num"])

while 1:
	getTicketInfo()
	time.sleep(2)

