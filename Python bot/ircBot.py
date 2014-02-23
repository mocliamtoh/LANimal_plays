# twisted imports
from twisted.internet import protocol, reactor
from twisted.words.protocols import irc

# system imports
import time, sys
from botCredentials import botCredentials as bCred

class IRCBot(irc.IRCClient):
    nickname = bCred.nickname
    
    def signedOn(self):
        #called when the bot has joined the IRC channel
        print "Bot has signed on"
        self.join(self.factory.channel)
        
    def privmsg(self, user, channel, msg):
        print "bot received a message"
        print msg

        #called when the bot receives a message
        #
        
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
        
        
reactor.connectTCP(bCred.address, bCred.port, IRCBotFactory(bCred.channel))
reactor.run()
print "something went wrong in this test - " + bCred.address