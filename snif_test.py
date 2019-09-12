import time
import socket
 
#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

txt = "ip_listen.txt"
fb = '157.240.7.35'

def ada(kata):
    with open(txt) as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if kata in line:
            return True
    return False



def write_file(key_arr):
    with open(txt, "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")
            if ke.find("space") > 0:
                f.write('\n')
            # Finding other Keys
            if ke.find("Key") == -1:
                f.write(ke)


# receive a packet
while True:

   # print output on terminal
   ip_listen = s.recvfrom(65565)[1][0]
   if str(ip_listen) == fb:
       print("Kau sedang mengakses facebook")
   if ada(ip_listen):
       pass
   else:
       print(ip_listen)
       write_file(ip_listen + "\n")
