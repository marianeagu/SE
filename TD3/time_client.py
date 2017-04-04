# -*- coding: utf-8 -*-
import socket, select, string, sys
 
def prompt() :
    sys.stdout.write(' <You> ')
    sys.stdout.flush()
 
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python time_client.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    #creare socket object 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # conectare hostname - port
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    prompt()
     
    while True:
        socket_list = [sys.stdin, s]
         
        # lista socket-uri 
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #mesaje primite de la client
            if sock == s:
                data = sock.recv(1024)    #nu primeste mai mult de 1024 bytes
                if not data :
                    print '\nDisconnected from chat server'
                    print("The time got from the server is %s" % data.decode('ascii'))
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    prompt()
             
            #clientul trimite un mesaj in terminal
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
