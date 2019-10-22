#!/usr/bin/env python3

import socket

import numpy as np
import json
import time

import pickle

x = np.arange(0,np.pi*10,0.1).tolist()
y = np.sin(x).tolist()
data_size = len(x)
counter = 0
graph_size = 100

samples = 0
tic = time.time()

HOST = '192.168.11.18'  # Standard loopback interface address (localhost)
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)


def get_graph_data():

    global counter,data_size,graph_size,x,y
    global samples,tic

    #Calculate FPS
    samples += 1
    if (time.time() - tic) > 2:
        print("FPS is : ",samples /(time.time() - tic))
        samples = 0
        tic = time.time()
    
    counter += 1
    if counter > (data_size - graph_size):
        counter = 0

    graph_to_send = json.dumps({
        'x':x[counter:counter+graph_size],
        'y':y[counter:counter+graph_size]
    })
    return graph_to_send


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            conn.sendall(get_graph_data().encode('utf-8'))


