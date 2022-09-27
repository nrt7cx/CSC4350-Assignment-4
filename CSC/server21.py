from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", help="Sets the port for the server", type=int)
#parser.add_argument("-h","--help", help="Prints out message on how to run the server", type=str)
args = parser.parse_args()

serverPort = args.port
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive.")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    
    if sentence[0:14] == "GET / HTTP/1.1":
            f = open('index.html', 'r') 
            file_contents = f.read()
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents.encode())
            connectionSocket.close()
        
    if sentence[0:22] == "GET /epic.txt HTTP/1.1":
            f = open('epic.txt', 'r')
            file_contents = f.read()
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents.encode() + b"\r\n\r\n")
              
    else:
        modifiedSentence = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(modifiedSentence.encode())
    
    connectionSocket.close()