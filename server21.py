from socket import *
from pathlib import Path
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
    if sentence[0:3] == "GET":
        path_to_file = ''
        path = Path(path_to_file)
        if path_to_file == '':
            modifiedSentence = "HTTP/1.1 200 OK\r\n\r\n" + 'sentence' + "\r\n\r\n"
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()   
        elif path.is_file():
            modifiedSentence = "HTTP/1.1 200 OK\r\n\r\n" + sentence + "\r\n\r\n"
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()     
        else:
            modifiedSentence = "HTTP/1.1 404 Not Found\r\n\r\n" + sentence + "\r\n\r\n"
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()