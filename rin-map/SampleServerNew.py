from __future__ import print_function
import socket, ssl, sslpsk2, sys
from concurrent.futures import thread

PSKS = {b'client1' : b'abcdef',
        b'client2' : b'123456'}

#********* CONSTANT VARIABLES *********
BACKLOG = 50            # how many pending connections queue will hold
MAX_DATA_RECV = 999999  # max number of bytes we receive at once
DEBUG = True            # set to True to see the debug msgs
BLOCKED = []            # just an example. Remove with [""] for no blocking at all.

def server(host, port):

    try:
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_sock.bind((host, port))
        tcp_sock.listen(BACKLOG)

    except socket.error as e:
        if tcp_sock:
            tcp_sock.close()
        print("Could not open socket:", e)
        sys.exit(1)


    while 1:

        sock, client_addr = tcp_sock.accept()
        ssl_sock = sslpsk2.wrap_socket(sock,
                                      server_side = True,
                                      ssl_version=ssl.PROTOCOL_TLSv1,
                                      ciphers='ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH',
                                      psk=lambda identity: PSKS[identity],
                                      hint=b'server1')
        thread.start_new_thread(server_thread, (ssl_sock, client_addr))



def server_thread(ssl_sock, client_addr):
    msg = ssl_sock.recv(4).decode()
    print('Server received: %s'%(msg))
    msg = "pong"
    ssl_sock.sendall(msg.encode())

    ssl_sock.shutdown(socket.SHUT_RDWR)
    ssl_sock.close()

def main():
    host = '127.0.0.1'
    port = 6000
    server(host, port)

if __name__ == '__main__':

    main()
