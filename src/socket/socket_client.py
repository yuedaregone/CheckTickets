import socket
import threading

class NetClient:
	csocket = None
	recv_gap = 1
	buff_size = 1024

	def __init__(self):
		pass

	def connect(self, host, port):
		self.csocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		error_code = self.csocket.connect_ex((host,port))
		self.csocket.setblocking(0)
		if error_code == 0:
			timer = threading.Timer(self.recv_gap, self.recv)
			timer.start()
			return 0
		else:
			print("connect error!")
		return -1

	def send(self, buff):
		size = len(buff)
		if size <= 0:
			print("data is empty!")
			return
		sbuff = buff
		ssize = 0
		while ssize < size:
			send_size = self.csocket.send(sbuff)
			sbuff = sbuff[send_size:len(sbuff)-send_size]
			ssize = ssize + send_size

	def recv(self):
		ret = ""
		try:
			ret = self.csocket.recv(self.buff_size)
		except Exception, e:
			pass
		if ret != "":
			print("recv:")
			print(ret)
		timer = threading.Timer(self.recv_gap, self.recv)
		timer.start()

	def disconnect(self):
		self.csocket.close()

if __name__ == '__main__':
	client = NetClient()
	#addr = socket.getaddrinfo("daregone.f3322.net",20480)
	addr = socket.getaddrinfo("192.168.0.148",20480)
	print(addr[0][4][0])
	error_code = client.connect(addr[0][4][0],20480)

	if error_code == 0:
		while True:
			key = raw_input()
			if key == 'q' or key == '':
				break
			client.send(key)
	client.disconnect()
