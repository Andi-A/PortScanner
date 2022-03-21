#If we connect to a port its open
#import socket from IPy import IP


from ctypes.wintypes import tagRECT
from lib2to3.pytree import convert
import socket
from IPy import IP
def scan(target,):
    converted_ip=check_ip(target)
    print('\n'+ '[-_0] Scanning Target '+ str(target))
    for port in  range (1,500):
        scan_port(converted_ip,port)


def check_ip (ip):  #Specifing IP address
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)    #Conv ert hostname to IP-Address
def  get_banner(s):
    return s.recv(1024) #1024 bytes
def scan_port(ipaddress,port): #Function
    try:
        sock=socket.socket() #Socket object
        sock.settimeout(0.5) #Increases scanning  speed but with lower accuracy
        sock.connect((ipaddress,port))
        try:
            banner =get_banner(sock) #Sofware running on port
            print('[+] Open Port '+ str(port) + ' : '+ str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port '+ str(port))
    except:
        pass #Just pass 

if __name__=="__main": #It recognies if the program is running as the main program 
    targets=input('[+] Enter Target/s to scan(split multiple targets with  , ')
   
    if ',' in targets: #Checks , in user input
        for ip_add in targets.split(','): #Split
            scan(ip_add.strip(' ')) #Removes empty spaces

    else:
         scan(targets)



