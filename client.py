#!/usr/bin/env python3
import socket
import os
class Client:
	def __init__(self, rank):
		self.rendevour = '127.0.0.1'
		self.clientip = socket.gethostbyname(socket.gethostname())
		self.port = 5000
		self.ADDR = (self.clientip,self.port)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.bind(self.ADDR)
		self.FORMAT = 'utf-8'
		self.initmesage = 'b'
		#self.client.sendto(self.initmesage.encode(self.FORMAT),(self.rendevour,5050))
		print(dir(os))

		

	def initiate_com(self):
		command = input('Type command to be broadcast: ')
		while True:
			#self.client.sendto(command.encode(self.FORMAT),(self.rendevour,5050))
			pass



c = Client(1)
print(c.clientip)