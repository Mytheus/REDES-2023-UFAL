import socket
import threading

#python servidor.py
#python cliente.py

FT = 4
YT = 0
WIN = 1
LOSE = 2
EMP = 3

def verifyLines(matriz):
    for i in range(len(matriz)):
        if matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2] and matriz[i][0]!=0:
            return True
    return False

def verifyColumns(matriz):
    for i in range(len(matriz)):
        if matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[0][i]!=0:
            return True
    return False

def verifyDiagonal(matriz):
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[1][1]!=0:
        return True
    if matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[1][1]!=0:
        return True
    return False

def verifyWin(matriz):
    return verifyLines(matriz) or verifyColumns(matriz) or verifyDiagonal(matriz)

def verifyVelha(matriz):
    for i in matriz:
        for u in i:
            if u==0:
                return False
    return True

def initializeMatrix(matriz):
    for i in range(3):
        lista = [0,0,0]
        matriz.append(lista)
    return matriz

def alteraTabuleiro(cmd, jogador, matriz):
    matriz[int(cmd[0])][int(cmd[1])] = jogador
    return matriz



def jogoDaVelha(conn1, conn2):
    matriz = []
    matriz = initializeMatrix(matriz)
    conn1.send("11".encode())
    conn2.send("12".encode())
    continua = True
    pVez = True
    vez = True
    win = False
    jogador = 1
    while continua:

        if pVez:
            conn1.send(str(FT).encode())
            pVez = False
        if vez:
            comando = conn1.recv(2048)
            jogador = 1  
        else: 
            comando = conn2.recv(2048)
            jogador = 2
        # Alterando o estado do jogo de acordo com o comando
        matriz = alteraTabuleiro(comando.decode()[1:3], jogador, matriz)
        #Verificação de vitória
        if vez:
            if verifyWin(matriz):
                conn2.send(str(LOSE).encode())
                conn2.send(comando)
                conn1.send(str(WIN).encode())
                conn2.close()
                conn1.close()
                print("Jogo finalizado!")
                break
            elif verifyVelha(matriz):
                conn2.send(str(EMP).encode())
                conn1.send(str(EMP).encode())
                conn2.close()
                conn1.close()
                print("Jogo empatado!")
                break
            else:
                conn2.send(str(YT).encode())
                conn2.send(comando)
        else:
            if verifyWin(matriz):
                conn1.send(str(LOSE).encode())
                conn1.send(comando)
                conn2.send(str(WIN).encode())
                conn2.close()
                conn1.close()
                print("Jogo finalizado!")
                break
            elif verifyVelha(matriz):
                conn1.send(str(EMP).encode())
                conn2.send(str(EMP).encode())
                conn2.close()
                conn1.close()
                print("Jogo empatado!")
                break
            else:
                conn1.send(str(YT).encode())
                conn1.send(comando)
        vez = not vez


serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
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
