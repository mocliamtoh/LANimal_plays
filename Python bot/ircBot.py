# twisted imports
from twisted.internet import protocol, reactor
from twisted.internet.task import LoopingCall
from twisted.words.protocols import irc

# system imports
import time, sys

# lanimal plays imports
from botCredentials import botCredentials as bCred
import parseCommand
import sendCmds

# global vars
emuCommand = ''
emuSocket = sendCmds.initSocket()

class IRCBot(irc.IRCClient):
    nickname = bCred.nickname
    
    def signedOn(self):
        #called when the bot has joined the IRC channel
        print "Bot has signed on"
        #repeater.start(0.01)
        self.join(self.factory.channel)
        
    def privmsg(self, user, channel, msg):
        #called when the bot receives a message
        
        print "bot received a message" + msg
        (cmd,cmdType) = parseCommand.parseMessage(msg)

        global emuCommand
        if cmdType == 1:
            sendCmds.sendString(emuSocket,cmd) #emuCommand = emuCommand + ',' + cmd
        elif cmdType == 2:
            pass
        
    def action(self, user, channel, action):
        #called after a /me
        print "bot has detected an action"
        print channel
        

class IRCBotFactory(protocol.ClientFactory):
    def __init__(self, channel):
        self.channel = channel
        
    def buildProtocol(self, address):
        proto = IRCBot()
        proto.factory = self
        return proto
        
    def clientConnectionLost(self, connector, reason):
        #reconnect if disconnected
        print "Disconnected [%s]" %reason
        print "Trying to reconnect"
        connector.connect()
        
    def clientConnectionFailed(self, connector, reason):
        print "fuck"
        reactor.stop()

def sendAndReset():
    global emuCommand
    sendCmds.sendString(emuSocket,emuCommand)
    emuCommand = ''

#repeater = LoopingCall(sendAndReset)

reactor.connectTCP(bCred.address, bCred.port, IRCBotFactory(bCred.channel))
reactor.run()
print "something went wrong in this test - " + bCred.address