import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

address = ('127.0.0.1', 20000)

server_socket.bind(address)
server_socket.listen(1)

connection, client_address = server_socket.accept()

buffer_size = 4096
received_message = connection.recv(buffer_size)

print("Client says: {}".format(received_message.decode()))

# Not the best way, eh?
# maybe sending length is better, but this works.
# unless some idiot sends this && it happens to be at the
# end of a 16 byte string being sent... v. unlikely.
end_code = "$MeSSaGeEnD!"

msg = 'message, "{}" received.'.format(received_message.decode()).encode('utf8')
connection.sendall(msg+ end_code.encode('utf8'))

