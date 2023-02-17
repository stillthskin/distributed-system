#!/usr/bin/env python3
import socket

class client:
	def __init__(self):
		#print(dir(socket))
		rendezvous = "192.168.0.3"
		clientip = socket.gethostbyname(socket.gethostname())
		knownport = 5050
		port = 5000
		SIZE = 64
		self.rank = 1
		client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client.bind((clientip,port))
		client.connect((rendezvous,knownport))
		client.listen()
		while True:
			conn,data = client.accept()
			responce = conn.recv(self.SIZE).decode("utf-8")
			self.rank = int(responce.split(";")[1])
		command = input("Please enter command to be sent: ")
		command = command.encode("utf-8")
		command_len = str(len(command)).encode("utf-8")
		command_len += b' ' *(SIZE - len(command))
		client.send(command_len)
		client.send(f"{self.rank};command".encode("utf-8"))
		client.send("hello world".encode("utf-8"))
	
		
		

c = client()