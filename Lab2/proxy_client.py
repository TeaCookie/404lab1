import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    chunk = s.recv(BYTES_TO_READ)
    result = b'' + chunk

    while(len(chunk) > 0):
        chunk = s.recv(BYTES_TO_READ)
        result += chunk
    
    s.close()
    return result

# print(get("127.0.0.1", 8080))
print(get("www.google.com", 80))