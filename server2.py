from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", help="Sets the port for the server", type=int)
#parser.add_argument("-h","--help", help="Prints out message on how to run the server", type=str)
args = parser.parse_args()

socket = socket(AF_INET, SOCK_STREAM)
#print("Please enter a specific page: ")
#website= input()
socket.connect(("www.imdb.com", args.port))
request_Part1 = "GET / HTTP/1.1\r\nHost:"
print("Please enter a specific page: ")
website= input()
request = request_Part1 + website + "\r\n\r\n" 
socket.send(request.encode())

response = socket.recv(10000)
#if response[0:12].decode() == "HTTP/1.1 200":   
    #print("HTTP 200 OK") 
print(response.decode())
socket.close