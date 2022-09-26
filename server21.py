from email import message
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", help="Sets the port for the server", type=int)
#parser.add_argument("-h","--help", help="Prints out message on how to run the server", type=str)
args = parser.parse_args()

serverPort = args.port
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print ("The server is ready to receive.")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message)
    #if message.decode() == 