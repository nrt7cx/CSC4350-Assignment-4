#Nathaniel Tirado
#Server recieves messages from the browser and sends the corresponding message back.
#Python; socket, argparse, pathlib(Path)
#run with command line
from socket import *
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", help="Sets the port for the server", type=int)
args = parser.parse_args()

serverPort = args.port
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive.")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    splitSentence = sentence.split()
    print(splitSentence)

    if splitSentence[0] == "GET":

        if splitSentence[1] == "/":
                f = open('index.html', 'r') 
                file_contents = f.read()
                connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents.encode() + b"\r\n\r\n")
                connectionSocket.close()
    
        elif splitSentence[1] == "/index.html":
                f = open('index.html', 'r') 
                
                file_contents = f.read()
                connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents.encode() + b"\r\n\r\n")
                connectionSocket.close()
        
        elif splitSentence[1] == "/epic.txt":
                f = 'epic.txt'
                path = Path(f)
                if path.is_file():
                        r = open('epic.txt', 'r')
                        file_contents1 = r.read()
                        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents1.encode() + b"\r\n\r\n")
                        connectionSocket.close()
                else:
                        modifiedSentence = "HTTP/1.1 404 Not Found\r\n\r\n"
                        connectionSocket.send(modifiedSentence.encode())
                        connectionSocket.close()
        
        else:
                modifiedSentence = "HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(modifiedSentence.encode())
                connectionSocket.close()
        
    else:
        modifiedSentence = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(modifiedSentence.encode())
        connectionSocket.close()
