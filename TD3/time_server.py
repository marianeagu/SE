# -*- coding: utf-8 -*-
import socket, select,sys,time
 
#functie de broadcast mesaje catre toti clientii conectati 
def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:
          # nu trimite catre clientul care a trimis mesajul 
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)       #trimit mesajul
            except :
                #  blocare conexiune socket sau apasare (CTRL+C) 
                socket.close()                #inchid socket-ul
                CONNECTION_LIST.remove(socket)
 
if __name__ == "__main__":
     
    # descriere socket 
    CONNECTION_LIST = []
    RECV_BUFFER = 1024
    PORT = 6666
    
    #creare sochet 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))     #adresa ip si port-ul
    server_socket.listen(10)                  #queue up to 10 requests
 
    # adaugare socket_server in lista de conexiuni 
    CONNECTION_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)         
 
    while True:
        #  lista socket-urilor  
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            # adaugarea unei connexiuni 
            if sock == server_socket:
                # cazul în care există o conexiune nouă prin server_socket
                clientsocket, addr = server_socket.accept()     #stabilire connexiunii
                CONNECTION_LIST.append(clientsocket)            #adaugare in lista
                print "Client (%s, %s) connected" % addr
                currentTime = time.ctime(time.time()) + "\r\n"
                clientsocket.send(currentTime.encode('ascii'))
                 
                broadcast_data(clientsocket, "[%s:%s] entered room\n" % addr)
             
            # mesaje primite de la client
            else:
                # procesare mesaje de la client
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()
