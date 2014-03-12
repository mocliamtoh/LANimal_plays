import sys

emuCmds = {'ba':'A', 'bb':'B','bx':'X', 'by':'Y','bl':'L', 'br':'R', 'bst':'start',
    'bsl':'select','du':'up','dl':'left','dd':'down','dr':'right',
    'a':'A', 'b':'B','x':'X', 'y':'Y','l':'L', 'r':'R', 'start':'start',
    'select':'select','up':'up','left':'left','down':'down','right':'right'}

holdCmds = {'duh': 'uph', 'bbh': 'Bh', 'drh': 'righth', 'dlh': 'lefth', 
    'bsth': 'starth', 'bxh': 'Xh', 'ddh': 'downh', 'bslh': 'selecth', 'byh': 'Yh', 
    'brh': 'Rh', 'bah':'Ah', 'blh': 'Lh',
    'uph': 'uph', 'bh': 'Bh', 'righth': 'righth', 'lefth': 'lefth', 
    'starth': 'starth', 'xh': 'Xh', 'downh': 'downh', 'selecth': 'selecth', 'yh': 'Yh', 
    'rh': 'Rh', 'ah':'Ah', 'lh': 'Lh'}

botCmds = {'!':'bang'}

def parseMessage(message):
    commandType = 0
    command = ''
    
    print message

    if message in emuCmds.keys():
        commandType = 1
        command = emuCmds[message]

    if message in holdCmds.keys():
        commandType = 1
        command = holdCmds[message]         
    
    if message in botCmds.keys():
        commandType = 2
        command = botCmds[message]
            
    return (command,commandType)


# Used for testing command parsing
if __name__ == "__main__":
    while True:
        input = raw_input("test: ")
        print parseMessage(input)
        if input == 'exit':
            break

