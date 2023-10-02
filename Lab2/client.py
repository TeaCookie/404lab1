import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # opened up a socket , AF_INET uses IPv4 AF_INET6 uses IPv6
    s.connect((host, port)) # connect to google
    s.send(request) # send request
    s.shutdown(socket.SHUT_WR) # Done sending
    result = s.recv(BYTES_TO_READ) # keep reading incoming data
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close() # this .close can be done automatically with the with syntax on python which auto closes when the connection is done.


get("www.google.com", 80)
# get("localhost", 8080)