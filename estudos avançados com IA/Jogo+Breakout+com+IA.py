# Importa a biblioteca turtle para criar gráficos e interfaces gráficas.
import turtle

# Importa a biblioteca random para gerar números aleatórios,
        # útil para adicionar elementos aleatórios no jogo.
import random

# Importa a biblioteca math para usar funções matemáticas avançadas.
import math

# Importa o módulo time para usar funcionalidades de
        # controle de tempo, como pausas.
import time

# Cria uma nova janela para o jogo utilizando a biblioteca turtle.
janela = turtle.Screen()

# Define o título da janela como "Jogo Breakout".
janela.title("Jogo Breakout")

# Define a cor de fundo da janela para preto.
janela.bgcolor("black")

# Configura as dimensões da janela para 800 pixels de
        # largura e 600 pixels de altura.
janela.setup(width=800, height=600)

# Desativa a atualização automática da tela para
        # otimizar o desempenho.
janela.tracer(0)

# Cria a raquete do jogador como um objeto Turtle.
raquete = turtle.Turtle()

# Define a velocidade da animação da raquete para o máximo possível.
raquete.speed(0)

# Define a forma da raquete como um quadrado.
raquete.shape("square")

# Define a cor da raquete para branco.
raquete.color("white")

# Ajusta o tamanho da raquete, esticando-a para 5 vezes o seu
        # tamanho original em comprimento e mantendo a altura padrão.
raquete.shapesize(stretch_wid=1, stretch_len=5)

# Levanta a caneta da raquete, para que ela não
        # desenhe enquanto se move.
raquete.penup()

# Move a raquete para a posição inicial no centro da
        # tela na parte inferior.
raquete.goto(0, -250)

# Cria a bola como um objeto Turtle para ser usada no jogo.
bola = turtle.Turtle()

# Define a velocidade da animação da bola para o máximo
        # possível, 0 indica "sem atraso".
bola.speed(0)

# Define a forma da bola como um quadrado.
bola.shape("square")

# Define a cor da bola para branco.
bola.color("white")

# Levanta a caneta da bola para evitar que ela desenhe
        # uma linha enquanto se move.
bola.penup()

# Posiciona a bola acima da raquete no início do jogo.
bola.goto(0, -200)

# Define a velocidade horizontal inicial da bola.
velocidade_inicial_dx = 3

# Define a velocidade vertical inicial da bola.
velocidade_inicial_dy = -3

# Atribui as velocidades inicial dx e dy à bola para
        # controle de movimento.
bola.dx = velocidade_inicial_dx
bola.dy = velocidade_inicial_dy

# Calcula a velocidade total inicial da bola usando o teorema de
        # Pitágoras para obter a hipotenusa (velocidade na diagonal).
velocidade_inicial_bola = math.hypot(velocidade_inicial_dx, velocidade_inicial_dy)

# Armazena a velocidade calculada como a velocidade atual da bola.
velocidade_bola = velocidade_inicial_bola

# Cria uma lista vazia para armazenar os blocos que
        # serão destruídos pela bola.
blocos = []

# Define uma lista de cores para os blocos que aparecerão no jogo.
cores = ["red", "orange", "yellow", "green", "blue"]


# Define uma função chamada 'criar_blocos' para criar os
# blocos que a bola pode destruir.
def criar_blocos():

    # Loop para criar 5 filas de blocos (cada fila é um nível diferente).
    for y in range(5):

        # Loop para criar blocos em uma fila. Distribui os blocos horizontalmente
        # de -350 a 350, com um espaçamento de 100 pixels entre cada bloco.
        for x in range(-350, 400, 100):

            # Cria um objeto Turtle para cada bloco.
            bloco = turtle.Turtle()

            # Define a velocidade da animação do bloco para o máximo possível,
            # para que os blocos sejam criados instantaneamente.
            bloco.speed(0)

            # Define a forma do bloco como um quadrado.
            bloco.shape("square")

            # Define a cor do bloco. A cor muda com cada fila usando a lista 'cores'.
            bloco.color(cores[y])

            # Ajusta o tamanho do bloco para ser maior em largura
            # para formar um retângulo.
            bloco.shapesize(stretch_wid=1, stretch_len=5)

            # Levanta a caneta do bloco para evitar desenhar enquanto o
            # bloco é posicionado.
            bloco.penup()

            # Posiciona o bloco na tela. A posição x é definida pelo loop, e
            # a posição y começa em 250 e diminui por 30 para cada nova fila.
            bloco.goto(x, 250 - y * 30)

            # Adiciona o bloco criado à lista 'blocos' para manter o
            # controle de todos os blocos na tela.
            blocos.append(bloco)


# Chama a função criar_blocos para posicionar os blocos no jogo.
criar_blocos()

# Inicializa a variável pontuacao com 0, que irá acompanhar a
        # pontuação do jogador ao longo do jogo.
pontuacao = 0

# Inicializa a variável nivel com 1, que irá controlar o nível
        # de dificuldade atual do jogo.
nivel = 1

# Cria um objeto Turtle para exibir a pontuação e o nível do jogo.
exibir_pontuacao = turtle.Turtle()

# Define a velocidade da animação do texto de pontuação para o máximo
        # possível, para que o texto apareça instantaneamente.
exibir_pontuacao.speed(0)

# Define a cor do texto para branco, garantindo visibilidade
        # contra o fundo preto.
exibir_pontuacao.color("white")

# Levanta a caneta para evitar que o texto desenhe uma linha ao ser movido.
exibir_pontuacao.penup()

# Torna o objeto do texto invisível como cursor, deixando
        # apenas o texto visível.
exibir_pontuacao.hideturtle()

# Posiciona o objeto de texto na parte superior da tela para
        # não interferir com a jogabilidade.
exibir_pontuacao.goto(0, 260)

# Escreve a pontuação inicial e o nível na tela, alinhando ao
        # centro com a fonte Courier de tamanho 24.
exibir_pontuacao.write("Pontuação: 0  Nível: 1",
                       align="center",
                       font=("Courier", 24, "normal"))

# Inicializa uma variável booleana para controlar se a
        # velocidade da bola foi aumentada.
velocidade_aumentada = False


# Define uma função chamada 'fim_jogo' que é chamada quando o jogador
# perde ou o jogo precisa ser encerrado.
def fim_jogo():

    # Limpa o texto de pontuação e nível anterior da tela para preparar
    # para a mensagem de fim de jogo.
    exibir_pontuacao.clear()

    # Escreve a mensagem de 'Fim de Jogo' na tela, informando ao jogador
    # que o jogo terminou e oferecendo uma opção para reiniciar.
    exibir_pontuacao.write("Fim de Jogo. Escolha uma opção para reiniciar",
                           align="center",
                           font=("Courier", 24, "normal"))

    # Cria um objeto Turtle para atuar como botão de 'Recomeçar'.
    botao_recomecar = turtle.Turtle()

    # Define a velocidade da animação do botão para o máximo
    # possível, para que o botão apareça instantaneamente.
    botao_recomecar.speed(0)

    # Define a forma do botão como um quadrado.
    botao_recomecar.shape("square")

    # Define a cor do botão como cinza.
    botao_recomecar.color("grey")

    # Ajusta o tamanho do botão para ser visualmente maior e
    # mais proeminente na tela.
    botao_recomecar.shapesize(stretch_wid=2, stretch_len=10)

    # Levanta a caneta do botão para evitar que ele desenhe
    # uma linha ao ser movido.
    botao_recomecar.penup()

    # Posiciona o botão na tela na posição horizontal -150 e
    # vertical 0, facilitando o acesso pelo jogador.
    botao_recomecar.goto(-150, 0)

    # Cria um objeto Turtle para o texto que será exibido junto
    # com o botão 'Recomeçar'.
    texto_recomecar = turtle.Turtle()

    # Define a velocidade da animação do texto para o máximo possível,
    # para que o texto apareça instantaneamente.
    texto_recomecar.speed(0)

    # Define a cor do texto para branco, garantindo que seja visível
    # contra o fundo e a cor do botão.
    texto_recomecar.color("white")

    # Levanta a caneta do objeto de texto para evitar que desenhe uma
    # linha enquanto está sendo posicionado.
    texto_recomecar.penup()

    # Torna o cursor do objeto de texto invisível, deixando
    # apenas o texto visível.
    texto_recomecar.hideturtle()

    # Posiciona o texto logo abaixo do botão 'Recomeçar' na tela
    # para associá-lo visualmente ao botão.
    texto_recomecar.goto(-150, -10)

    # Escreve o texto "Recomeçar" na tela, alinhado ao centro com a
    # fonte Courier de tamanho 24, claramente indicando a ação que o botão representa.
    texto_recomecar.write("Recomeçar",
                          align="center",
                          font=("Courier", 24, "normal"))

    # Cria um objeto Turtle para o botão 'Jogar IA', que permitirá
    # aos jogadores ativar o modo de inteligência artificial.
    botao_jogar_ia = turtle.Turtle()

    # Define a velocidade da animação do botão para o máximo possível,
    # para que o botão apareça instantaneamente.
    botao_jogar_ia.speed(0)

    # Define a forma do botão como um quadrado, mantendo a consistência
    # visual com o botão 'Recomeçar'.
    botao_jogar_ia.shape("square")

    # Define a cor do botão como cinza, a mesma cor usada no
    # botão 'Recomeçar' para uniformidade.
    botao_jogar_ia.color("grey")

    # Ajusta o tamanho do botão para ser visualmente grande e proeminente,
    # facilitando a identificação e interação por parte do jogador.
    botao_jogar_ia.shapesize(stretch_wid=2, stretch_len=10)

    # Levanta a caneta do botão para evitar que ele desenhe uma
    # linha enquanto está sendo movido.
    botao_jogar_ia.penup()

    # Posiciona o botão na tela na posição horizontal 150 e vertical 0,
    # colocando-o à direita do botão 'Recomeçar' para fácil acesso.
    botao_jogar_ia.goto(150, 0)

    # Cria um objeto Turtle para exibir o texto associado ao botão 'Jogar IA'.
    texto_jogar_ia = turtle.Turtle()

    # Define a velocidade da animação do texto para o máximo possível,
    # assegurando que o texto apareça instantaneamente quando o jogo termina.
    texto_jogar_ia.speed(0)

    # Define a cor do texto para branco, garantindo alto contraste com o
    # botão cinza e fácil leitura contra o fundo escuro.
    texto_jogar_ia.color("white")

    # Levanta a caneta do objeto de texto para prevenir que desenhe
    # linhas indesejadas ao ser movido ou posicionado.
    texto_jogar_ia.penup()

    # Torna o cursor do objeto de texto invisível, deixando
    # visível apenas o texto que ele exibe.
    texto_jogar_ia.hideturtle()

    # Posiciona o texto do botão 'Jogar IA' ligeiramente abaixo do botão
    # na tela para facilitar a associação visual entre o texto e
    # o botão correspondente.
    texto_jogar_ia.goto(150, -10)

    # Escreve o texto "Jogar IA" na tela, alinhado ao centro com a
    # fonte Courier de tamanho 24. O texto serve como rótulo para o
    # botão, indicando claramente a ação que será tomada ao clicar.
    texto_jogar_ia.write("Jogar IA",
                         align="center",
                         font=("Courier", 24, "normal"))

    # Define a função 'ao_clicar', que será chamada sempre que o
    # usuário clicar na janela do jogo.
    def ao_clicar(x, y):

        # Usa a palavra-chave 'global' para permitir que esta função
        # modifique a variável 'modo_IA' que é global.
        global modo_IA

        # A primeira condição verifica se o clique foi dentro dos
        # limites do botão 'Recomeçar'.
        # Isso é feito verificando se a posição x do clique está
        # entre -200 e -100, e a posição y entre -20 e 20.
        if -200 < x < -100 and -20 < y < 20:

            # Se o clique foi dentro desses limites, a tartaruga que
            # representa o botão 'Recomeçar' é escondida.
            botao_recomecar.hideturtle()

            # Limpa qualquer texto que esteja sendo exibido pelo
            # objeto 'texto_recomecar'.
            texto_recomecar.clear()

            # Esconde também o botão 'Jogar IA', para garantir que a
            # tela seja limpa corretamente.
            botao_jogar_ia.hideturtle()

            # Limpa o texto associado ao botão 'Jogar IA'.
            texto_jogar_ia.clear()

            # Define a variável 'modo_IA' como False, indicando que o
            # jogo será reiniciado sem o modo de inteligência artificial.
            modo_IA = False

            # Chama a função 'reiniciar_jogo' para começar o jogo
            # de novo no modo normal.
            reiniciar_jogo()

        # A segunda condição verifica se o clique foi dentro dos
        # limites do botão 'Jogar IA'.
        # Checa se a posição x está entre 100 e 200, e a posição y entre -20 e 20.
        elif 100 < x < 200 and -20 < y < 20:

            # Se o clique foi dentro desses limites, a tartaruga
            # que representa o botão 'Recomeçar' é escondida.
            botao_recomecar.hideturtle()

            # Limpa qualquer texto que esteja sendo exibido pelo
            # objeto 'texto_recomecar'.
            texto_recomecar.clear()

            # Esconde também o botão 'Jogar IA', para garantir que a
            # tela seja limpa corretamente.
            botao_jogar_ia.hideturtle()

            # Limpa o texto associado ao botão 'Jogar IA'.
            texto_jogar_ia.clear()

            # Define a variável 'modo_IA' como True, indicando que o jogo
            # será reiniciado no modo de inteligência artificial.
            modo_IA = True

            # Reinicia o jogo, agora configurado para utilizar a inteligência
            # artificial para controlar a raquete.
            reiniciar_jogo()

    # Configura a janela do jogo para chamar a função 'ao_clicar' sempre que o
    # mouse for clicado dentro da área da janela.
    janela.onclick(ao_clicar)


# Define uma função para reiniciar o jogo, redefinindo a pontuação, a
# posição da bola, da raquete, a velocidade e os blocos.
def reiniciar_jogo():

    # Declara que as variáveis listadas serão usadas em um contexto global,
    # permitindo sua modificação dentro desta função.
    global pontuacao, nivel, bola, blocos, modo_IA, velocidade_bola

    # Move a bola para o centro acima da raquete, preparando para o reinício do jogo.
    bola.goto(0, raquete.ycor() + 20)  # Posicionar a bola acima da raquete

    # Redefine o nível do jogo para 1, reiniciando a progressão de dificuldade.
    nivel = 1

    # Chama a função para ajustar a velocidade da bola de
    # acordo com o novo nível.
    ajustar_velocidade_bola(nivel)

    # Posiciona a raquete no meio da tela na parte inferior,
    # centralizando-a para o reinício.
    raquete.goto(0, -250)  # Posicionar a raquete no meio

    # Zera a pontuação, uma vez que o jogo está sendo reiniciado.
    pontuacao = 0

    # Limpa o texto de pontuação anterior na tela.
    exibir_pontuacao.clear()

    # Escreve a nova pontuação e nível na tela, iniciando de novo.
    exibir_pontuacao.write("Pontuação: 0  Nível: 1", align="center", font=("Courier", 24, "normal"))

    # Loop para esconder todos os blocos existentes na tela.
    for bloco in blocos:
        bloco.hideturtle()

    # Limpa a lista de blocos, removendo todos os blocos
    # antigos para serem recriados.
    blocos.clear()

    # Chama a função para criar blocos novamente, redefinindo o layout dos blocos.
    criar_blocos()

    # Força a atualização da janela do jogo para refletir todas
    # as mudanças feitas.
    janela.update()

    # Pausa o jogo por 2 segundos antes de começar novamente, dando um
    # breve intervalo antes de reiniciar.
    time.sleep(2)  # Pausa de 2 segundos

    # Chama a função principal do loop de jogo para continuar
    # jogando após o reinício.
    loop_jogo()


# Define a função 'prever_posicao_bola', que calcula onde a bola estará
# horizontalmente (em x) no futuro, com base em sua velocidade e direção atuais.
def prever_posicao_bola():

    # Primeiro, verifica se a componente vertical da velocidade
    # da bola (dy) é zero.
    # dy = 0 significaria que a bola está se movendo horizontalmente
    # sem subir ou descer.
    if bola.dy == 0:

        # Se dy é zero, a bola continuará no mesmo y (altura) e
        # apenas o x (lateral) mudará.
        # Portanto, retorna a posição x atual da bola porque ela
        # não mudará de altura.
        return bola.xcor()

    # Calcula o tempo que levará até a bola chegar na mesma
    # altura vertical (y) que a raquete.
    # Isso é feito subtraindo a posição y da raquete pela posição y
    # da bola e dividindo pelo dy da bola.
    # O resultado é o número de "ticks" ou atualizações até que a bola
    # esteja na altura da raquete.
    tempo = (raquete.ycor() - bola.ycor()) / bola.dy

    # Calcula a futura posição x da bola com base em sua velocidade
    # horizontal dx e o tempo calculado.
    # Multiplica dx pelo tempo para encontrar quantos pixels a bola se
    # moverá horizontalmente nesse intervalo.
    posicao_futura = bola.xcor() + bola.dx * tempo

    # Usa um laço 'while' para ajustar a posição futura caso ela ultrapasse as
    # bordas do campo de jogo, que são definidas por x = 390 e x = -390.
    while posicao_futura > 390 or posicao_futura < -390:

        # Se a posição futura calculada for maior que 390 (borda
        # direita do campo de jogo),
        # calcula a posição como se a bola quicasse na parede e
        # voltasse para o campo.
        if posicao_futura > 390:

            # Subtrai a posição que excedeu de 780, o dobro do
            # limite, simulando um quique.
            posicao_futura = 780 - posicao_futura

            # Similarmente, se a posição futura for menor que -390 (borda
            # esquerda do campo de jogo),
        # ajusta a posição como se a bola tivesse quicado na parede
        # esquerda e voltasse para o campo.
        elif posicao_futura < -390:

            # Adiciona a posição que excedeu a -780, também simulando um quique.
            posicao_futura = -780 - posicao_futura

            # Retorna a posição x futura ajustada, que agora considera a
            # possibilidade da bola quicar nas paredes laterais.
    return posicao_futura


# Define uma função para detectar colisão entre dois objetos no jogo,
# como a bola e a raquete ou a bola e os blocos.
def detectar_colisao(objeto1, objeto2):

    # Retorna True se a distância entre objeto1 e objeto2 for
    # menor que 50 pixels, indicando uma colisão.
    return objeto1.distance(objeto2) < 50


# Define uma função para ajustar a velocidade da bola com
# base no nível atual do jogo.
def ajustar_velocidade_bola(nivel):

    # Permite modificar a variável global 'velocidade_bola' dentro desta função.
    global velocidade_bola

    # Calcula o novo multiplicador de velocidade baseado no nível atual.
    # A cada nível acima do primeiro, a velocidade aumenta em 50%.
    multiplicador_velocidade = 1 + (nivel - 1) * 0.5 # Aumenta a velocidade a cada nível

    # Atualiza a velocidade da bola multiplicando a velocidade inicial
    # pela taxa de multiplicador de velocidade calculada.
    velocidade_bola = velocidade_inicial_bola * multiplicador_velocidade

    # Calcula a direção atual da bola usando a função atan2, que retorna o
    # ângulo em radianos entre o eixo x e o vetor formado pelas
    # velocidades dx e dy.
    direcao = math.atan2(bola.dy, bola.dx)

    # Atualiza a velocidade horizontal (dx) da bola multiplicando a nova
    # velocidade total pela função cosseno do ângulo de direção,
    # garantindo que a bola mantenha sua direção ao longo do movimento horizontal.
    bola.dx = velocidade_bola * math.cos(direcao)

    # Atualiza a velocidade vertical (dy) da bola multiplicando a nova
    # velocidade total pela função seno do ângulo de direção,
    # garantindo que a bola mantenha sua direção ao longo do movimento vertical.
    bola.dy = velocidade_bola * math.sin(direcao)


# Define a função 'aumentar_velocidade' que é responsável por
# dobrar a velocidade da bola.
def aumentar_velocidade():

    # A palavra-chave 'global' é usada para indicar que a função
    # modificará a variável global 'velocidade_aumentada'.
    global velocidade_aumentada

    # Verifica se a velocidade já foi aumentada. Se não, o código
    # dentro do bloco if será executado.
    if not velocidade_aumentada:

        # Dobra a componente horizontal da velocidade da bola. 'bola.dx'
        # representa o deslocamento horizontal por atualização de quadro.
        bola.dx *= 2

        # Dobra a componente vertical da velocidade da bola. 'bola.dy' representa o
        # deslocamento vertical por atualização de quadro.
        bola.dy *= 2

        # Atualiza a variável 'velocidade_aumentada' para True, indicando
        # que a velocidade já foi aumentada.
        velocidade_aumentada = True


# Define a função 'velocidade_normal', que reverte a velocidade da bola ao
# seu estado anterior após ter sido aumentada.
def velocidade_normal():

    # A palavra-chave 'global' é utilizada para permitir acesso e modificação
    # da variável global 'velocidade_aumentada' dentro desta função.
    global velocidade_aumentada

    # Verifica se a velocidade da bola foi previamente aumentada.
    if velocidade_aumentada:

        # Divide a componente horizontal da velocidade da bola por 2,
        # retornando à velocidade anterior.
        bola.dx /= 2

        # Divide a componente vertical da velocidade da bola por 2,
        # retornando à velocidade anterior.
        bola.dy /= 2

        # Atualiza a variável 'velocidade_aumentada' para False, indicando
        # que a velocidade da bola voltou ao normal.
        velocidade_aumentada = False


# Configura um evento para capturar quando a tecla 'Shift_L' (Shift esquerdo) é
# pressionada, chamando a função 'aumentar_velocidade'.
janela.onkeypress(aumentar_velocidade, "Shift_L")

# Configura um evento para capturar quando a tecla 'Shift_L' (Shift esquerdo) é
# liberada, chamando a função 'velocidade_normal'.
janela.onkeyrelease(velocidade_normal, "Shift_L")


# Define uma função para mover a raquete para a direita.
def mover_raquete_direita():

    # Obtém a posição horizontal atual (coordenada x) da raquete.
    x = raquete.xcor()

    # Verifica se a raquete está dentro dos limites da tela à direita. 350 é o
    # limite antes da borda direita.
    if x < 350:

        # Incrementa a posição horizontal da raquete em 40 unidades,
        # movendo-a para a direita.
        x += 40

    # Define a nova posição horizontal da raquete.
    raquete.setx(x)


# Define uma função para mover a raquete para a esquerda.
def mover_raquete_esquerda():

    # Obtém a posição horizontal atual (coordenada x) da raquete.
    x = raquete.xcor()

    # Verifica se a raquete está dentro dos limites da tela à
    # esquerda. -350 é o limite antes da borda esquerda.
    if x > -350:

        # Decrementa a posição horizontal da raquete em 40 unidades,
        # movendo-a para a esquerda.
        x -= 40

    # Define a nova posição horizontal da raquete.
    raquete.setx(x)


# Configura a janela para escutar eventos de teclado.
janela.listen()

# Associa a tecla de seta para a direita ("Right") com a função
# 'mover_raquete_direita', permitindo mover a raquete para a
# direita quando a tecla é pressionada.
janela.onkeypress(mover_raquete_direita, "Right")

# Associa a tecla de seta para a esquerda ("Left") com a função
# 'mover_raquete_esquerda', permitindo mover a raquete para a
# esquerda quando a tecla é pressionada.
janela.onkeypress(mover_raquete_esquerda, "Left")

# Define uma variável 'modo_IA' e a inicializa como False. Essa variável
# pode ser usada para ativar um modo de jogo onde a raquete é
# controlada por um algoritmo de IA ao invés de interação humana.
modo_IA = False


# Define a função principal do loop do jogo, que é chamada repetidamente
# para atualizar o estado do jogo.
def loop_jogo():

    # Declara que as variáveis listadas serão utilizadas globalmente,
    # permitindo que esta função modifique seus valores.
    global pontuacao, nivel, blocos, modo_IA

    # Checa se a posição vertical (y) da bola é menor que -290, o que indica
    # que a bola passou da raquete (considerando a altura da tela).
    if bola.ycor() < -290:

        # Chama a função fim_jogo() para tratar o fim do jogo, mostrando a
        # tela de fim de jogo e parando o loop.
        fim_jogo()

        # Interrompe a execução adicional deste loop, não permitindo que
        # as próximas linhas sejam executadas.
        return

    # Atualiza a posição horizontal (x) da bola, adicionando a
    # velocidade horizontal (dx) à posição x atual.
    bola.setx(bola.xcor() + bola.dx)

    # Atualiza a posição vertical (y) da bola, adicionando a
    # velocidade vertical (dy) à posição y atual.
    bola.sety(bola.ycor() + bola.dy)

    # Verifica colisões da bola com as bordas superior e lateral da
    # janela do jogo e ajusta a trajetória da bola se necessário.

    # Se a bola atinge a borda superior da tela (y maior que 290),
    if bola.ycor() > 290:

        # Define a posição y da bola como 290 para mantê-la
        # dentro dos limites visíveis.
        bola.sety(290)

        # Inverte a direção vertical da bola (dy), fazendo-a quicar para baixo.
        bola.dy *= -1

    # Se a bola atinge a borda direita da tela (x maior que 390),
    if bola.xcor() > 390:

        # Define a posição x da bola como 390 para mantê-la dentro
        # dos limites visíveis.
        bola.setx(390)

        # Inverte a direção horizontal da bola (dx), fazendo-a
        # quicar para a esquerda.
        bola.dx *= -1

    # Se a bola atinge a borda esquerda da tela (x menor que -390),
    if bola.xcor() < -390:

        # Define a posição x da bola como -390 para mantê-la dentro dos limites visíveis.
        bola.setx(-390)

        # Inverte a direção horizontal da bola (dx), fazendo-a quicar para a direita.
        bola.dx *= -1

    # Verifica se o modo IA está ativado.
    if modo_IA:

        # Chama a função 'prever_posicao_bola' para calcular onde a bola
        # estará horizontalmente no futuro com base em sua trajetória atual.
        posicao_desejada = prever_posicao_bola()

        # Obtém a posição atual da raquete no eixo x.
        x_raquete = raquete.xcor()

        # Calcula a distância entre a posição futura prevista da bola e
        # a posição atual da raquete.
        distancia = posicao_desejada - x_raquete

        # Define a velocidade com que a raquete deve se mover. Essa velocidade é
        # calculada com base na velocidade horizontal da bola,
        # adicionando 10 unidades básicas e aumentando com base no
        # nível atual do jogo para tornar a IA mais desafiadora à
        # medida que o jogador avança.
        velocidade_raquete = abs(bola.dx) + 10 + (nivel - 1) * 2

        # Se a distância calculada é positiva, a bola está à direita da raquete.
        if distancia > 0:

            # Move a raquete para a direita. A função 'min' garante que a
            # raquete não se mova além da posição desejada, evitando
            # movimentos excessivos.
            x_raquete += min(velocidade_raquete, distancia)

        # Se a distância é negativa, a bola está à esquerda da raquete.
        elif distancia < 0:

            # Move a raquete para a esquerda. A função 'max' é usada para
            # garantir que a raquete não se mova além da posição desejada.
            x_raquete += max(-velocidade_raquete, distancia)

        # Verifica se a nova posição da raquete excede o limite
        # direito do campo de jogo.
        if x_raquete > 350:

            # Se exceder, ajusta a posição para o máximo permitido (350).
            x_raquete = 350

        # Verifica se a nova posição da raquete excede o limite
        # esquerdo do campo de jogo.
        if x_raquete < -350:

            # Se exceder, ajusta a posição para o mínimo permitido (-350).
            x_raquete = -350

        # Atualiza a posição da raquete no jogo para a nova posição calculada.
        raquete.setx(x_raquete)

    # Colisão com a raquete
    # Verifica se a bola está se movendo para baixo (dy < 0) e se a bola
    # está na mesma altura que a raquete dentro de uma
    # tolerância de 10 pixels.
    if (bola.dy < 0) and (bola.ycor() > raquete.ycor() - 10 and bola.ycor() < raquete.ycor() + 10) and (
            bola.xcor() > raquete.xcor() - 50 and bola.xcor() < raquete.xcor() + 50):

        # Se a colisão for detectada, ajusta a posição y da bola para ficar
        # logo acima da raquete, evitando que ela "entre" na raquete.
        bola.sety(raquete.ycor() + 10)

        # Verifica se ainda existem blocos no jogo.
        if blocos:

            # Encontra o bloco mais próximo da bola usando uma função lambda
            # para calcular a distância de cada bloco até a bola e pegar o mínimo.
            bloco_alvo = min(blocos, key=lambda bloco: bloco.distance(bola))

            # Calcula a diferença nas coordenadas x e y entre a bola e o bloco alvo.
            delta_x = bloco_alvo.xcor() - bola.xcor()
            delta_y = bloco_alvo.ycor() - bola.ycor()

            # Se a diferença em y for zero ou negativa (o que não deveria
            # acontecer normalmente), ajusta para um valor pequeno
            # positivo para evitar divisão por zero ou direção errada.
            if delta_y <= 0:
                delta_y = abs(delta_y) + 0.1

            # Calcula a distância euclidiana entre a bola e o bloco alvo.
            distancia = math.hypot(delta_x, delta_y)

            # Normaliza os componentes de deslocamento para criar um vetor
            # unitário (magnitude = 1) que aponte do bloco para a bola.
            dx_normalizado = delta_x / distancia
            dy_normalizado = delta_y / distancia

            # Ajusta a velocidade da bola usando o vetor normalizado,
            # multiplicado pela velocidade atual da bola.
            bola.dx = dx_normalizado * velocidade_bola
            bola.dy = dy_normalizado * velocidade_bola

        else:

            # Se não houver blocos, simplesmente inverte a direção vertical da
            # bola, fazendo-a quicar para cima quando atinge a raquete.
            bola.dy *= -1

    # Colisão com blocos
    # Itera sobre cada bloco na lista de blocos para verificar se
    # ocorreu uma colisão com a bola.
    for bloco in blocos:

        # Chama a função 'detectar_colisao' para verificar se a bola
        # colidiu com o bloco atual.
        if detectar_colisao(bola, bloco):

            # Se houve colisão, inverte a direção vertical da bola (dy),
            # fazendo-a quicar na direção oposta.
            bola.dy *= -1

            # Esconde o bloco com o qual a bola colidiu, usando a função
            # 'hideturtle', que torna o bloco invisível na tela.
            bloco.hideturtle()

            # Remove o bloco da lista de blocos, pois ele foi destruído pela colisão.
            blocos.remove(bloco)

            # Incrementa a pontuação do jogador em 10 pontos por cada bloco destruído.
            pontuacao += 10

            # Limpa o texto de pontuação anterior para atualizar com a nova pontuação.
            exibir_pontuacao.clear()

            # Escreve a nova pontuação e o nível atual na tela, garantindo
            # que o jogador seja informado do seu progresso.
            exibir_pontuacao.write(f"Pontuação: {pontuacao}  Nível: {nivel}",
                                   align="center",
                                   font=("Courier", 24, "normal"))

            # Sai do loop após a colisão para evitar alterações múltiplas em
            # um único quadro, especialmente em cenários de múltiplas colisões.
            break

    # Próximo nível
    # Verifica se a lista de blocos está vazia, indicando que
    # todos foram destruídos.
    if not blocos:

        # Incrementa o nível do jogo, aumentando a dificuldade.
        nivel += 1

        # Reposiciona a bola acima da raquete, preparando para o
        # reinício do jogo no novo nível.
        bola.goto(0, raquete.ycor() + 20)

        # Posiciona a raquete de volta ao centro na parte inferior da tela.
        raquete.goto(0, -250)

        # Ajusta a velocidade da bola com base no novo nível,
        # aumentando a dificuldade.
        ajustar_velocidade_bola(nivel)

        # Limpa o texto de pontuação e nível anterior para atualizar
        # com os novos dados.
        exibir_pontuacao.clear()

        # Escreve a pontuação atual e o novo nível na tela, mantendo o
        # jogador informado sobre o progresso.
        exibir_pontuacao.write(f"Pontuação: {pontuacao}  Nível: {nivel}",
                               align="center",
                               font=("Courier", 24, "normal"))

        # Cria novos blocos para o novo nível, redefinindo o campo de jogo.
        criar_blocos()

        # Força uma atualização da janela do jogo para refletir as mudanças visuais.
        janela.update()

        # Pausa o jogo por 2 segundos antes de iniciar o novo
        # nível, dando ao jogador um breve descanso.
        time.sleep(2)

    # Atualiza a janela do jogo para gaantir que todras as mudanças
    # visuais sejam processadas.
    janela.update()

    # Configura um temporizador para chamar a função 'loop_jogo' novamente
    # após 10 milissegundos, mantendo o jogo em execução contínua.
    janela.ontimer(loop_jogo, 10)


# Chama a função 'loop_jogo' para começar o loop principal do jogo.
loop_jogo()

# Entra no loop principal do Tkinter, que mantém a janela aberta e lida com
        # eventos como cliques e teclas pressionadas.
janela.mainloop()