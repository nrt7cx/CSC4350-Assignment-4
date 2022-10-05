#Nathaniel Tirado
#Server recieves messages from the browser and sends the corresponding message back.
#Python; socket, argparse, pathlib(Path), logging, time
#run with command line
from socket import *
import argparse
from pathlib import Path
import logging
import time

def my_Index():
        f = open('index.html', 'r') 
        file_contents = f.read()
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents.encode() + b"\r\n\r\n")
        logging.info(splitSentence[4][0:9] + ' - - ' + time.strftime("%m/%d/%Y:%H:%M:%S") + ' ' + splitSentence[0] + ' ' + splitSentence[1] + ' ' + splitSentence[2] + ' 200 ' + splitSentence[6])
        connectionSocket.close()

def file_Found():
        r = open('epic.txt', 'r')
        file_contents1 = r.read()
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" + file_contents1.encode() + b"\r\n\r\n")
        logging.info(splitSentence[4][0:9] + ' - - ' + time.strftime("%m/%d/%Y:%H:%M:%S") + ' ' + splitSentence[0] + ' ' + splitSentence[1] + ' ' + splitSentence[2] + ' 200 ' + splitSentence[6])
        connectionSocket.close()
        
def my_404():
        f = open('404.html', 'r')
        file_contents= f.read()
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n" + file_contents.encode() + b"\r\n\r\n")
        logging.info(splitSentence[4][0:9] + ' - - ' + time.strftime("%m/%d/%Y:%H:%M:%S") + ' ' + splitSentence[0] + ' ' + splitSentence[1] + ' ' + splitSentence[2] + ' 404 ' + splitSentence[6])
        connectionSocket.close()

def my_400():
        f = open('400.html', 'r')
        file_contents= f.read()
        connectionSocket.send(b"HTTP/1.1 400 Bad Request\r\n\r\n" + file_contents.encode() + b"\r\n\r\n")
        logging.warning(str(addr[0]) + ' - - ' + time.strftime("%m/%d/%Y:%H:%M:%S") + ' - '  + splitSentence[0] + ' - 400 -')
        connectionSocket.close()

        


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
    logging.basicConfig(filename='example.log', level=logging.DEBUG)

    if splitSentence[0] == "GET":

        if splitSentence[1] == "/":
                my_Index()
    
        elif splitSentence[1] == "/index.html":
                my_Index()
        
        elif splitSentence[1] == "/epic.txt":
                f = 'epic.txt'
                path = Path(f)
                
                if path.is_file():
                        file_Found()
                else:
                        my_404()
        
        else:
                my_404()
        
    else:
        my_400()
