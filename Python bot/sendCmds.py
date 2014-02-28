import socket

def sendString(emu,msg):
    if msg != '':
        print msg
    if msg.find('\n') == -1:
        msg = msg + '\n'
    emu.send(msg)
    

def initSocket():
    toEmu = socket.socket()
    toEmu.connect(('localhost', 6667))
    return toEmu


"""
i = 0
while True:
    i += 1
    print i
    toEmu.send(str(i) + '\n')

    

toEmu.close()
"""