#coding:utf-8
import os
import json
import sys

#start_path = 'D:/Downloads/mp3/zjl/'
start_path = 'C:/Users/1849/AppData/Local/Netease/CloudMusic/'
dest_path = 'D:/Downloads/mp3/dest/'

def read_file(name):
	fp = file(name,"r")
	content = fp.read()
	fp.close()
	return content
	
def get_all_file(path):
	file_list = os.listdir(path)
	
	f_dict = {}
	for file_name in file_list:
		f_ex = file_name[file_name.rfind('.'):len(file_name)]		
		if f_ex == ".uc":
			f_id = file_name[0:file_name.find('-')]
			f_dict[f_id] = file_name
	return f_dict

def del_all_file(path):
	file_list = os.listdir(path)
	for file_name in file_list:
		f_ex = file_name[file_name.rfind('.'):len(file_name)]
		if f_ex == ".uc":
			os.rename(path + file_name, dest_path + file_name)
		else:
			os.remove(path + file_name)

	
if __name__ == '__main__':
	file_name = start_path + "webdata/file/history"
	content = read_file(file_name)
	if content == '':
		print("No content of " + file_name)
		sys.exit()
		
	music_path = start_path + "Cache/Cache/"
	file_dict = get_all_file(music_path)	
		
	json_data = json.loads( content )	
	json_file_num = 0
	mv_file_num = 0
	for item in json_data:
		json_file_num = json_file_num + 1
		item_name = item["track"]["name"]
		item_id = item["tid"]
		
		#print(item_id)
		if file_dict.has_key(str(item_id)):
			mv_file_num = mv_file_num + 1			
			os.rename(music_path+file_dict[str(item_id)], dest_path + item_name + ".mp3")
	
	print("find %d file in json file. and move %d file." % (json_file_num, mv_file_num))
	
	if json_file_num == mv_file_num:
		#os.remove(file_name)
		del_all_file(music_path)
	
	
	
	
	
	