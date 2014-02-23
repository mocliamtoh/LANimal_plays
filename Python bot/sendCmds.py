import socket, time

toEmu = socket.socket()
toEmu.connect(('localhost', 6667))
i = 0
while True:
    i += 1
    toEmu.send(str(i))
    time.sleep(1)
    

toEmu.close()
