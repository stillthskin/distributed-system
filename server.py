#!/usr/bin/env python3


import socket
import threading

class clientNode:
	def __init__(self,conn,data,rank):
		self.conn = conn
		self.data = data
		self.rank = rank

class server:
	def __init__(self):
		self.SIZE = 1024
		self.nodes = []
		#print(dir(socket))
		serverip = socket.gethostbyname(socket.gethostname())
		port = 5050
		server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server.bind((serverip,port))
		print(f"Server Running on {serverip}...")
		server.listen()
		while True:
			conn,data = server.accept()
			rank = len(self.nodes) + 1
			n = clientNode(conn,data,rank)
			self.nodes.append(n)
			conn.send(f"Assigned rank: {rank}".encode())
			thread = threading.Thread(target=self.handle_client, args=(n,))
			thread.start()
	
	def broadcast(self, message, sender):
		for client in self.clients:
			if client != sender:
				client.conn.send(message)
	
	def handle_client(self,client):
		connection =True
		while connection:
			msg = client.conn.recv(self.SIZE).decode("utf-8")
			if msg:
				msg_len = int(msg)
				msg = client.conn.recv(msg_len).decode("utf-8")
				command = msg.decode("utf-8").strip()
				if int(command.split(":")[0]) > client.rank:
					client.conn.send("Cannot Excecute Rank Lower: ".encode("utf-8"))
				else:
					message = f"Executed: {command}"
					self.broadcast(message.encode(), client)
				if msg == "DISCONNECT":
					connection = False
		client.conn.close()
		

s = server()
