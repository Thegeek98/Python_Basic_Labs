import socket
print(socket.gethostname())
print(socket.gethostbyname("www.google.com"))

hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname_ex(hostname)
    print(ip_address)
except:
    print("error")