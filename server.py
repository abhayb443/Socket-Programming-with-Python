#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8080

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print('\nWaiting for connections...')
        s.listen()
        connection, address = s.accept()
        with connection:
            print('Connected by', address)
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(data.decode())
                connection.sendall(bytes('Connection Successful, Packet received from server', 'utf-8'))