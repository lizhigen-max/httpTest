import socket
 
HOST,PORT = '192.168.127.101',8080
# HOST,PORT = '10.55.18.43',8000
 
listen_socket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,
socket.SO_REUSEADDR,1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
	client_connection,client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print(request)
	
	http_response = b"""HTTP/1.1 200 OK\r\n\r\nHello,world!"""
	client_connection.send(http_response)
