# Projeto de Redes

## Alunos:

 - José Matheus Santana Alves ([Mytheus](https://github.com/Mytheus))
 - Lucas Heron Santos Anchieta ([LukeHer0](https://github.com/LukeHer0))
 - Rafael Luciano Lima da Silva ([rafaellucian0](https://github.com/rafaellucian0))

## Tema
Neste Projeto, optamos por fazer um Jogo da Velha na linguagem de programação Python, utilizando técnicas e ferramentas oriundas dos conceitos de sockets.

## Aplicação

A aplicação permite que múltiplos jogadores se conectem em partidas de Jogo da Velha, criando novos jogos à medida que os usuários conectam-se ao servidor.

## Instruções de uso

Primeiramente, é necessário iniciar a conexão do servidor, executando o arquivo "servidor.py" em um prompt de comando:
***python servidor.py***

Posteriormente, é preciso alterar a variável *"serverAddress"* no arquivo "cliente.py", colocando o endereço correspondente ao ip da máquina do usuário. Para cada usuário que for iniciar uma conexão com o servidor de jogos, é necessário executar o seguinte comando no prompt de comando:
***python cliente.py***

Quando um usuário inicia a conexão, o servidor procurará outra conexão de um cliente para criar a partida, caso não haja uma conexão (quando o número de clientes conectados ao servidor é ímpar), o cliente ficará aguardando a chegada de seu oponente.

Ao encontrar a conexão, o jogo será iniciado. O primeiro cliente a conectar-se ao servidor será definido como o Jogador 1, jogando com o X no tabuleiro, e o segundo cliente será definido como Jogador 2. 

O Jogador 1 sempre iniciará jogando, então em sua tela aparecerá o tabuleiro no estado inicial (vazio) seguido das coordenadas em que as "peças" poderão ser colocadas. 

AGUARDANDO OPONENTE...
Jogo encontrado! Você é o X!
Estado do tabuleiro:
|   | 0 | 1 | 2 |
|---|---|---|---|
| 0 |  |  |  |
| 1 |  |  |  |
| 2 |  |  |  |

Sua vez!
Digite a ação:

O servidor e o Jogador 2 aguardarão a resposta do cliente sobre qual jogada ele irá fazer, e após o Jogador 1 digitar sua jogada, o tabuleiro atualizará de acordo com ela, e a mesma será enviada ao servidor, que a repassará para o Jogador 2.

Digite a ação: 11
Estado do tabuleiro:
|   | 0 | 1 | 2 |
|---|---|---|---|
| 0 |  |  |  |
| 1 |  | X |  |
| 2 |  |  |  |

Vez do oponente...

Ao receber a jogada de seu oponente, o Jogador 2 receberá o tabuleiro atualizado e estará livre para realizar seu lance:

AGUARDANDO OPONENTE...
Jogo encontrado! Você é o O!
Estado do tabuleiro:
|   | 0 | 1 | 2 |
|---|---|---|---|
| 0 |  |  |  |
| 1 |  | X |  |
| 2 |  |  |  |

Sua vez!
Digite a ação:

E assim o jogo continuará até que haja um vencedor ou seja declarado empate. As condições de vitória são analisadas pelo servidor à cada lance jogado.

Estado do tabuleiro:
|   | 0 | 1 | 2 |
|---|---|---|---|
| 0 | X | O |  |
| 1 |  | X | O |
| 2 |  |  | X |

Você Venceu!
