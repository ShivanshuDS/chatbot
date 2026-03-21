import socket #ye to chich  ko add karta h
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address="192.168.1.227"
port=2222
complete_address=(ip_address,port)
message=input("Enter your message:-")
encode_msg=message.encode("ascii")
s.sendto(encode_msg,complete_address)
