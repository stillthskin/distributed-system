#!/usr/bin/env python3
import socket

class client:
	def __init__(self):
		#print(dir(socket))
		serverip = socket.gethostbyname(socket.gethostname())
		port = 5050
		SIZE = 64
		rank = 1
		client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client.bind((serverip,port))
		client.connect((serverip,port))
		command = input("Please enter command to be sent: ")
		command = command.encode("utf-8")
		command_len = str(len(command)).encode("utf-8")
		command_len += b' ' *(SIZE - len(command))
		client.send(command_len)
		client.send(f"{rank};command".encode("utf-8"))
		client.send("hello world".encode("utf-8"))
		client.listen()
		

c = client()