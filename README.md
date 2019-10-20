# Real-time Data Visualization
## IP
192.168.11.85 (Web Server)
192.168.11.18 (Sensor)

**You need change ip address(in source code) dependent on your "network environment"**

## Web server side
```
$ pip3 install websockets
$ sudo apt-get update
$ sudo apt-get install apache2
```

move "plot_graphs_from_websocket.html" to "/var/www/html/"

```
$ python3 ws_server.py
```

## Sensor side
```
$ python3 socket_server.py
```

## PPT
* https://docs.google.com/presentation/d/17gcLdMVilcXN4QGtei15g-6nFRCPQJV9zVY96pl77yE/edit?usp=sharing


### reference
* http://www.whatimade.today/realtime-graphs-using-ploty-and-websockets/
* https://github.com/dannyvai/plotly_websocket_example
* https://github.com/google/pywebsocket
* https://websockets.readthedocs.io/en/stable/intro.html
* https://realpython.com/python-sockets/





