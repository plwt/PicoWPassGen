# modules
import network
import socket
from time import sleep
import secrets

# connection details
ssid = "??????"
password = "??????"


# List of characters for password
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9', '!','@','#','$','£','%','^','&','*','(',')','_','+','=','{','}','[',']','|',':',';','"','<','>','?','~','`','.','/']

def connect():
    """This function facilitates connection of Raspberry Pi Pico W to the Internet using WiFi."""
    
    # connecting to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # performing handshake
    # continuously wait for connection
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
    # displaying to the console the IP address that the Raspberry Pi Pico is assigned to
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    
    return ip

def open_socket(ip):
    """
    This function opens a socket in order for the server (Raspberry Pi Pico W)
    to be able to listen to a client (any web browser accessing the IP address
    of the Raspberry Pi Pico W).
    """
    
    # opening a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    
    return connection

def webpage(Password):
    """This function contains the HTML string containing elements that would be displayed in the webpage."""
    
    
    html = f"""
            <!DOCTYPE html>
            <html>
            <body style="background-color:#000000">
            <p> </p>
            <p style="color:#00ff41; font-size:50px">Password is {Password} *C</p>
            <p> </p>
            </body>
            </html>
            """
    
    return str(html)

def serve(connection):
    """This function starts the web server and serves the webpage."""
    
    # starting the web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        # generates password from list
        Password = []
        for n in range(10):
            Password.append(secrets.choice(characters))
                
        html = webpage(Password)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)

except KeyboardInterrupt:
    machine.reset()