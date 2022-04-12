import socket                

class BluetoothData:
    def __init__(self, )


def server(data, port):
    s = socket.socket()         
    host = socket.gethostname()  
    port = 12345                
    s.bind((host, port))        
    s.listen(5)                
    while True:
        conn, addr = s.accept()     
        print('连接地址:', addr)
        conn.send(str(len(data)).encode('utf-8'))
        conn.send(data)
        conn.close()                

