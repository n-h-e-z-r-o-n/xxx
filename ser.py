import socket
import cv2
import numpy as np
import ast


def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname(socket.gethostname()) #"127.0.0.1"
    print(server_ip)
    #server_ip = "41.90.187.99"
    port = 8000

    # bind the socket to a specific address and port
    server.bind((server_ip, port))
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip} :{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # receive data from the client
    count = 1
    hold: int = 0
    hold2: tuple = (0, 0, 0)
    while True:

        frame_byte_length = client_socket.recv(1024).decode("utf-8", errors="ignore")
        client_socket.send(f"recived : {frame_byte_length}")


    # close connection socket with the client
    client_socket.close()
    print("Connection to client closed")
    # close server socket
    server.close()


run_server()
