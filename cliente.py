import socket

FT = 4
YT = 0
WIN = 1
LOSE = 2
EMP = 3

symbol = ""

serverAddress = "192.168.0.22"
serverPort = 12000
toconec = (serverAddress, serverPort)


def printTabuleiro():
    print("Estado do tabuleiro:")
    print("   0      1      2")
    count=0
    for i in range(len(matriz)):
        print(count, end="")
        count+=1
        for u in range(len(matriz[i])):
            if u==2:
                print(" ",matriz[i][u], end="")    
            else:
                print(" ",matriz[i][u], " | ", end="")
        print()

def alteraTabuleiro(cmd):
    if (int(cmd[1]) > 2 or int(cmd[1]) < 0) or (int(cmd[2]) > 2 or int(cmd[2]) < 0):
        print("Coordenada inválida!")
        return False

    elif matriz[int(cmd[1])][int(cmd[2])] != " ":
        print("Casa preenchida")
        return False
    
    else:
        matriz[int(cmd[1])][int(cmd[2])] = cmd[0]
        return True
    


matriz = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]



clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(toconec)
print("AGUARDANDO OPONENTE...")
    
msg = clientSocket.recv(1024).decode()
if msg[0]=="1":
    if msg[1] == "1":
        print("Jogo encontrado! Você é o X!")
        symbol = "X"
    elif msg[1] == "2":
        print("Jogo encontrado! Você é o O!")
        symbol = "O"


while True:
    msg = int(clientSocket.recv(1024).decode())
    
    if msg == WIN:
        comando = clientSocket.recv(1024).decode()
        alteraTabuleiro(comando)
        printTabuleiro()
        print("Você venceu!")
        break
        
    elif msg == EMP:
        comando = clientSocket.recv(1024).decode()
        alteraTabuleiro(comando)
        printTabuleiro()
        print("Deu velha!")
        break
        
    elif msg == LOSE:
        comando = clientSocket.recv(1024).decode()
        alteraTabuleiro(comando)
        printTabuleiro()
        print("Você perdeu!")
        break
    
    else:
        if msg == YT:
            comando = clientSocket.recv(1024).decode()
            alteraTabuleiro(comando)
        printTabuleiro()
        print("Sua vez!")
        while True:
            comando = input("Digite a ação: ")
            if (len(comando)!=2 or not comando.isnumeric()):
                print("Entrada inválida!")
                continue
            comando = symbol+comando
            if alteraTabuleiro(comando):
                clientSocket.send(comando.encode())
                break
        printTabuleiro()
        print("Vez do oponente...")