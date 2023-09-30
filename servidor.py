import socket
import threading

#python servidor.py
#python cliente.py

FT = 4
YT = 0
WIN = 1
LOSE = 2
EMP = 3

def jogoDaVelha(conn1, conn2):
    conn1.send("11".encode())
    conn2.send("12".encode())
    continua = True
    pVez = True
    vez = True
    win = False
    while continua:

        if pVez:
            conn1.send(str(FT).encode())
            pVez = False
        if vez:
            comando = conn1.recv(1024)  
        else: 
            comando = conn2.recv(1024)
        # Alterando o estado do jogo de acordo com o comando
        #Verificação de vitória
        if vez:
            conn2.send(str(YT).encode())
            conn2.send(comando)
        else:
            conn1.send(str(YT).encode())
            conn1.send(comando)
        vez = not vez


serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()



print(f"Escutando na porta {serverPort}")



while True:
    print("Esperando o primeiro oponente 1...")
    connectionSocket1, addr1 = serverSocket.accept()
    print("Esperando o primeiro oponente 2...")
    connectionSocket2, addr2 = serverSocket.accept()
    thread = threading.Thread(target=jogoDaVelha, args=[connectionSocket1, connectionSocket2])
    thread.start()
    print(f"Partida inicializada com {addr1} e {addr2}")