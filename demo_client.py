import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client_socket.connect(("127.0.0.1", 20000))

my_message = input("> ")
client_socket.sendall(my_message.encode('utf-8'))

end_code = "$MeSSaGeEnD!" # lol.
message_over = False

received_message = ''
while not message_over:
	received_message += client_socket.recv(16).decode()
	# probably not the right answer, but an answer...
	message_over = received_message.endswith(end_code)

#so here's where sending this extra bit of code is wasteful I guess:
print("Server says: {}".format(received_message.strip(end_code))) 

client_socket.close()
