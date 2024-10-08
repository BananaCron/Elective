try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network
import esp
import gc


esp.osdebug(None)
gc.collect()


ssid = 'GROUP_8-AP'        
password = '123456789'     


ap = network.WLAN(network.AP_IF)
ap.active(True)      
ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=password) 


while not ap.active():
    pass

print('Access Point active')
print(ap.ifconfig())  


led = Pin(2, Pin.OUT)
