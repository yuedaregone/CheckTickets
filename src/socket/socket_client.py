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
		self.csocket.settimeout(15)
		error_code = self.csocket.connect_ex((host,port))
		if error_code == 0:
			timer = threading.Timer(self.recv_gap, self.recv)
			timer.start()
		else
			print("connect error!")

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
		print("recv:")
		ret = self.csocket.recv(buff_size)
		print(ret)
		timer = threading.Timer(self.recv_gap, self.recv)
		timer.start()

	def disconnect(self):
		self.csocket.close()
