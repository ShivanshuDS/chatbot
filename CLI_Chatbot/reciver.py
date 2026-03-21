import socket #ye to chich  ko add karta h
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address="192.168.1.206"
port=8888
complete_address=(ip_address,port)
s.bind(complete_address)
while True:
    message=s.recvfrom(1024)
    decoded_msg=message[0].decode("ascii")
    print(decoded_msg)