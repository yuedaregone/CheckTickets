 #!/usr/bin/python
import socket
import commands
import select
import threading

class NetServer:
	host = "127.0.0.1"
	port = 2048
	ssocket = None
	cconns = []

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.InitSocket()

	def InitSocket(self):
		self.ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.ssocket.bind((self.host, self.port))
		self.ssocket.listen(5)
		self.ssocket.setblocking(0)
		timer = threading.Timer(1, self.loop)
		timer.start()

	def SocketAccept(self):
		dirty = []
		while True:
			words = raw_input()
			for co in self.cconns:
				try:
					co.sendall(words)
				except Exception, e:
					print("close connet")
					dirty.append(co)
			for dc in dirty:
				self.cconns.remove(dc)
			dirty = []

	def accept(self):
		try:
			conn,addr=self.ssocket.accept()
			print("Connected:")
			print(addr)
			self.cconns.append(conn)
		except Exception, e:
			pass

	def recv(self):
		for co in self.cconns:
			ret = ""
			try:
				ret = co.recv(1024)
			except Exception, e:
				pass
			if ret != "":
				print(co.getpeername()),
				print(ret)

	def loop(self):
		self.accept()
		self.recv()

		timer = threading.Timer(1, self.loop)
		timer.start()


if __name__ == '__main__':
	server = NetServer("127.0.0.1", 20480)
	server.SocketAccept()





