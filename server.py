#!/usr/bin/env python3


import socket
import threading
class Node:
	def __init__(self, conn, addr,rank):
		self.conn = conn
		self.addr = addr
		self.rank = rank
class Server:
	def __init__(self):
		self.clients[]
		self.N = 20
		self.DISCONNECT = "DISCONNECT"
		self.HEADER = 64
		SERVER = socket.gethostbyname(socket.gethostname())
		print(socket.gethostbyname(socket.gethostname()))
		PORT = 5050
		self.ADDR = (SERVER, PORT)
		self.FORMAT = 'utf-8'
		self.addr = " "
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.lock = threading.Lock()
	def handle_clients(self):
		pass
	def start_server(self):
		self.server.bind(self.ADDR)
		self.server.listen()
		print('server running...')
		while True:
			conn, addr = self.server.accept()
			print('Connection received')
			rank = len(clients)
			n = Node(conn,addr,rank)
			clients.append(n)
			conn.send(f"Assigned rank: {rank}".encode())
			thread = threading.thead(target=self.handle, args(n,))
			print(conn, addr)

			pass

	def broadcast(self, message, sender):
        for client in self.clients:
            if client != sender:
                client.conn.send(message)
    '''
    def handle(self, client):
        while True:
        	data = client.conn.recv(1024)
        	command = data.decode().strip()
            if int(command.split(":")[0]) > client.rank:
               client.conn.send("Rejected: rank is higher".encode())
            else:
            	message = f"Executed: {command}"
                self.broadcast(message.encode(), client)

        client.conn.close()
        self.clients.remove(client)
        self.broadcast(f"{client.addr} disconnected".encode(), client)
        with self.lock:
            for i in range(client.rank+1, N):
                self.clients[i].rank -= 1
    '''

s = Server()
s.start_server()

#print(prompts)
