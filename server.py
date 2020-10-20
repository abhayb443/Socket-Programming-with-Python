#!/usr/bin/env python3

import socket
import json
import requests

HOST = '52.172.195.80'
PORT = 80

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
                resp = requests.post('https://samtrackapi.azurewebsites.net/api/Device/GetDevicData?DeviceData={}'.format(data.decode()))
                print(resp)
                connection.sendall(bytes('Connection Successful, Packet received from server', 'utf-8'))