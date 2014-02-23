import sys

emuCmds = {'a':'A', 'b':'B','x':'X', 'y':'Y','l':'L', 'r':'R', 'start':'start','select':'select','up':'up','left':'left','down':'down','right':'right'}

botCmds = {'!':'bang'}

def parseMessage(message):
    commandType = 0
    command = ''
    
    if message in emuCmds.keys():
        commandType = 1
        command = emuCmds[message]            
    
    if message in botCmds.keys():
        commandType = 2
        command = botCmds[message]
            
    return (command,commandType)

if __name__ == "__main__":
    while True:
        input = raw_input("test: ")
        print parseMessage(input)
        if input == 'exit':
            break

