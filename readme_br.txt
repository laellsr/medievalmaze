# Medieval Maze v1

## Requerimentos

#### Python 3.x

Para rodar a aplicação é necessário poder executar Python 3 em seu sistema operacional.

#### Pygame

Pygame é uma aplicação Python que facilita a construção de jogos. Para obtê-la é nessário instalar gerenciador de pacotes **pip**. Geralmente, ele já está na instação com python.

Para Ubuntu e derivados
> apt-get install python-pip

Para Unix/macOS
> python get-pip.py

Para Windows
> py get-pip.py --no-index --find-links=/local/copies


No caso de dúvidas acesse a documentação pip
https://pip.pypa.io/en/stable/installing/


Para instalar o Pygame use
> python -m pip install -U pygame

Em caso de dúvidas
https://www.pygame.org/wiki/GettingStarted


## O jogo

Para rodar o jogo e testar o multiplayer, é necessário abrir 5 terminais.

Inicialize o servidor no primeiro terminal com
> python server.py

No restante use
> python client.py

Atenção: aguarde o cliente ser carregado para executar o próximo. Pode ocorrer travamento caso execute todos de uma vez.

Este processo precisa ser reiniciado a cada final de partida ou a cada desconexão do cliente. Ao final da partida, o servidor precisa obrigatoriamente ser reiniciado.