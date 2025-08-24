# Importa a biblioteca pygame, usada para desenvolver
        # jogos e aplicações gráficas em Python.
import pygame

# Importa a biblioteca random, que permite a geração
        # de números aleatórios.
import random

# Importa a biblioteca sys, que fornece acesso a funções que
        # interagem com o interpretador Python.
import sys

# Configurações básicas para definir a largura e altura
        # da tela do jogo.
LARGURA, ALTURA = 300, 600

# Define o tamanho de cada bloco do jogo. No caso, cada
        # bloco será um quadrado de 30 pixels de lado.
TAMANHO_BLOCO = 30

# Calcula o número de colunas que a tela pode acomodar,
        # dividindo a largura total pela largura de um bloco.
COLUNAS = LARGURA // TAMANHO_BLOCO

# Calcula o número de linhas que a tela pode acomodar,
        # dividindo a altura total pela altura de um bloco.
LINHAS = ALTURA // TAMANHO_BLOCO

# Define a cor branca no formato RGB, que é usada no jogo,
        # onde RGB(255, 255, 255) representa a cor branca.
BRANCO = (255, 255, 255)

# Define a cor preta no formato RGB, que é usada no jogo,
        # onde RGB(0, 0, 0) representa a cor preta.
PRETO = (0, 0, 0)

# Inicializa o módulo de fontes do pygame, que é
        # necessário para renderizar textos.
pygame.font.init()

# Cria uma fonte SysFont, que é uma maneira de usar
        # fontes do sistema, com tamanho 24 para ser usada no jogo.
FONTE = pygame.font.SysFont(None, 24)


# Define uma lista de cores utilizando o formato RGB,
        # onde cada tupla representa uma cor diferente.
CORES = [
    (0, 0, 0),       # Preto: Todos os componentes RGB são 0, resultando em preto.
    (255, 0, 0),     # Vermelho: Máximo de vermelho (255), sem verde (0) e sem azul (0).
    (0, 255, 0),     # Verde: Máximo de verde (255), sem vermelho (0) e sem azul (0).
    (0, 0, 255),     # Azul: Máximo de azul (255), sem vermelho (0) e sem verde (0).
    (255, 255, 0),   # Amarelo: Máximo de vermelho (255) e verde (255), sem azul (0).
    (255, 0, 255),   # Magenta: Máximo de vermelho (255) e azul (255), sem verde (0).
    (0, 255, 255),   # Ciano: Máximo de verde (255) e azul (255), sem vermelho (0).
    (128, 128, 128)  # Cinza: Vermelho, verde e azul em igual intensidade média (128).
]

# Define uma lista de formas para as peças do Tetris. Cada sublista
        # representa uma configuração diferente de blocos.
FORMAS = [
    [[1, 1, 1],      # Forma de 'T': três blocos na primeira linha e um bloco central na segunda linha.
     [0, 1, 0]],
    [[1, 1],         # Forma de 'O': um quadrado de dois por dois blocos.
     [1, 1]],
    [[1, 1, 1, 1]],  # Forma de 'I': uma linha reta de quatro blocos.
    [[1, 1, 1],      # Forma de 'L': três blocos em uma linha e um bloco à esquerda na linha seguinte.
     [1, 0, 0]],
    [[1, 1, 1],      # Forma de 'J': três blocos em uma linha e um bloco à direita na linha seguinte.
     [0, 0, 1]],
    [[1, 1, 1],      # Outra forma de 'T': similar à primeira, para diversidade de rotações.
     [0, 1, 0]],
    [[0, 1, 1],      # Forma de 'S': dois blocos deslocados na primeira linha e dois blocos alinhados na linha seguinte.
     [1, 1, 0]]
]


class Tetris:

    # Método construtor da classe Tetris, onde são inicializadas as
    # configurações básicas do jogo.
    def __init__(self):

        # Inicializa todos os módulos internos necessários para o
        # funcionamento do pygame.
        pygame.init()

        # Cria a janela do jogo com uma largura adicional de 200 pixels para
        # interface de usuário adicional, como pontuação e controles.
        self.tela = pygame.display.set_mode((LARGURA + 200, ALTURA))

        # Define o título da janela do jogo para "Tetris com IA".
        pygame.display.set_caption("Tetris com IA")

        # Inicializa a matriz que representa a grade do jogo com
        # zeros, indicando espaços vazios.
        # A matriz tem 'LINHAS' linhas e 'COLUNAS' colunas, preenchida
        # inicialmente com zeros.
        self.grade = [[0] * COLUNAS for _ in range(LINHAS)]

        # Define a pontuação inicial do jogador como 0.
        self.pontuacao = 0

        # Inicializa a variável que guarda a peça atual em jogo como None,
        # significando que não há peça em jogo no início.
        self.peca_atual = None

        # Define a variável de controle para verificar se o jogo
        # terminou, inicialmente definida como False.
        self.fim_de_jogo = False

        # Define se a inteligência artificial está ativa ou não,
        # inicialmente definida como False.
        self.ia_ativa = False

        # Cria um objeto Clock para controlar o tempo dentro do jogo,
        # usado para limitar a taxa de atualização.
        self.relogio = pygame.time.Clock()

        # Define a frequência com que as peças devem cair, em milissegundos.
        self.frequencia_queda = 500

        # Inicializa um contador de tempo para controlar
        # quando a próxima peça deve cair.
        self.tempo_passado = 0

        # Inicializa uma lista para armazenar os movimentos
        # que a IA deve realizar.
        self.movimentos_ia = []

        # Define o atraso entre os movimentos executados pela IA,
        # para tornar seus movimentos visíveis e naturais.
        self.atraso_movimento_ia = 100

        # Inicializa um contador de tempo que controla o intervalo
        # entre os movimentos da IA.
        self.tempo_movimento_ia = 0

    def nova_peca(self):

        # Define a peça atual do jogo escolhendo aleatoriamente uma
        # forma das definidas na lista FORMAS.
        # A função random.choice seleciona um elemento aleatório de uma lista.
        self.peca_atual = {

            'forma': random.choice(FORMAS),

            # Atribui uma cor aleatória à peça, escolhendo um índice
            # aleatório da lista CORES.
            # random.randint gera um número inteiro aleatório entre os
            # dois argumentos inclusivos.
            # A cor na posição 0 é geralmente preta (usada para fundo),
            # então começamos de 1.
            'cor': random.randint(1, len(CORES) - 1),

            # Define a posição inicial da peça no meio da largura da grade.
            # COLUNAS // 2 calcula a coluna central da grade, e
            # len(FORMAS[0][0]) // 2 ajusta
            # a posição x para que a peça sja centraliezada baseada em sua largura.
            'x': COLUNAS // 2 - len(FORMAS[0][0]) // 2,

            # Define a posição y inicial da peça como 0, significando que
            # ela começará no topo da grade.
            'y': 0,

            # Define a rotação inicial da peça como 0. Isso pode ser alterado
            # para girar a peça durante o jogo.
            'rotacao': 0

        }

    def verificar_colisao(self, desloc_x=0, desloc_y=0, forma=None):

        # Verifica se uma forma específica foi fornecida, se não,
        # usa a forma da peça atual.
        if forma is None:
            forma = self.peca_atual['forma']

        # Itera sobre cada linha da forma da peça, utilizando 'enumerate'
        # para obter tanto o índice 'y' quanto a própria linha.
        for y, linha in enumerate(forma):

            # Itera sobre cada bloco na linha, utilizando 'enumerate' para
            # obter tanto o índice 'x' quanto o valor do bloco.
            for x, valor in enumerate(linha):

                # Verifica se o bloco atual é parte da forma da peça (valor não zero).
                if valor:

                    # Calcula as novas coordenadas x e y da peça ao adicionar os
                    # deslocamentos e a posição atual.
                    novo_x = self.peca_atual['x'] + x + desloc_x
                    novo_y = self.peca_atual['y'] + y + desloc_y

                    # Verifica se a nova posição x está fora das bordas laterais da
                    # grade ou se a nova posição y está fora do limite inferior.
                    if novo_x < 0 or novo_x >= COLUNAS or novo_y >= LINHAS:

                        # Retorna True indicando uma colisão com as bordas da grade.
                        return True

                    # Verifica se a nova posição y é válida e se o espaço correspondente
                    # na grade já está ocupado por outra peça.
                    if novo_y >= 0 and self.grade[novo_y][novo_x]:

                        # Retorna True indicando uma colisão com outra
                        # peça já colocada na grade.
                        return True

        # Se nenhuma das condições de colisão for verdadeira após
        # verificar todos os blocos, retorna False.
        return False

    def rotacionar_peca(self, forma=None):

        # Verifica se uma forma específica foi fornecida para rotação;
        # se não, usa a forma da peça atual.
        if forma is None:
            forma = self.peca_atual['forma']

        # Realiza a rotação da peça. Esta linha é uma combinação de várias
        # operações de manipulação de lista:
        # 1. `zip(*forma)`: O operador '*' desempacota a lista de listas `forma`
        # em argumentos separados para a função `zip`,
        #    que agrupa os elementos de cada "coluna" da matriz em tuplas.
        # 2. `reversed(coluna)`: Reverte cada tupla gerada pelo `zip`,
        # que agora representa uma linha da forma rotacionada,
        # transformando assim as colunas originais em linhas da nova forma.
        # 3. `list(...)`: Converte cada tupla revertida de volta em uma lista.
        # O resultado final é uma nova lista de listas que representa a
        # forma da peça rotacionada em 90 graus no sentido horário.
        return [list(reversed(coluna)) for coluna in zip(*forma)]

    def desenhar_grade(self):

        # Itera sobre cada linha da grade, onde 'y' é o índice da linha.
        for y in range(LINHAS):

            # Itera sobre cada coluna dentro da linha, onde 'x' é o índice da coluna.
            for x in range(COLUNAS):

                # Obtém a cor da célula atual acessando a lista de cores
                # usando o índice armazenado na posição grade[y][x].
                cor = CORES[self.grade[y][x]]

                # Desenha um retângulo na tela na posição calculada a
                # partir dos índices 'x' e 'y'.
                # Multiplica o índice pela dimensão do bloco para converter
                # os índices de grade para pixels.
                # 'TAMANHO_BLOCO' é a largura e a altura do retângulo.
                # O último argumento '0' significa que o retângulo é
                # preenchido com a cor especificada.
                pygame.draw.rect(self.tela, cor,
                                 (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 0)

                # Desenha um retângulo com a cor preta ao redor do retângulo
                # anterior para criar um contorno.
                # Isso ajuda a definir claramente os limites de cada bloco na grade.
                # O último argumento '1' especifica a largura da linha do
                # contorno, tornando-o visível.
                pygame.draw.rect(self.tela, PRETO,
                                 (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

    def desenhar_peca(self):

        # Itera sobre cada linha da forma da peça atual, onde 'y' é o
        # índice da linha e 'linha' são os dados da linha.
        for y, linha in enumerate(self.peca_atual['forma']):

            # Itera sobre cada valor na linha, onde 'x' é o índice da
            # coluna e 'valor' é o conteúdo da célula (1 ou 0).
            for x, valor in enumerate(linha):

                # Verifica se a célula atual da forma é parte ativa da
                # peça (valor igual a 1).
                if valor:

                    # Desenha um retângulo colorido para representar a peça.
                    # A cor é determinada pelo índice da cor armazenado na peça atual.
                    # A posição do retângulo na tela é calculada adicionando a
                    # posição inicial da peça ('x', 'y')
                    # às coordenadas locais da forma ('x', 'y'), multiplicado
                    # pelo tamanho de cada bloco.
                    pygame.draw.rect(self.tela, CORES[self.peca_atual['cor']],
                                     ((self.peca_atual['x'] + x) * TAMANHO_BLOCO,
                                      (self.peca_atual['y'] + y) * TAMANHO_BLOCO,
                                      TAMANHO_BLOCO, TAMANHO_BLOCO), 0)

                    # Desenha um contorno preto em volta do retângulo colorido para
                    # destacar cada bloco individualmente.
                    # Isso facilita a visualização da configuração da peça na tela,
                    # especialmente quando as peças estão próximas
                    # ou sobrepostas. O parâmetro '1' indica a largura da linha do contorno.
                    pygame.draw.rect(self.tela, PRETO,
                                     ((self.peca_atual['x'] + x) * TAMANHO_BLOCO,
                                      (self.peca_atual['y'] + y) * TAMANHO_BLOCO,
                                      TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

    def fixar_peca(self):

        # Itera sobre cada linha da forma da peça atual,
        # onde 'y' é o índice da linha.
        for y, linha in enumerate(self.peca_atual['forma']):

            # Itera sobre cada valor na linha, onde 'x' é o índice da coluna.
            for x, valor in enumerate(linha):

                # Verifica se a célula atual da forma é uma parte
                # ativa da peça (valor igual a 1).
                if valor:

                    # Fixa a peça na grade atualizando a posição correspondente
                    # na grade com a cor da peça.
                    # A posição na grade é determinada pela posição atual da
                    # peça ('x' e 'y') mais os índices da forma.
                    self.grade[self.peca_atual['y'] + y][self.peca_atual['x'] + x] = self.peca_atual['cor']

        # Chama o método `limpar_linhas` para verificar e remover
        # quaisquer linhas completas na grade.
        self.limpar_linhas()

        # Gera uma nova peça para continuar o jogo.
        self.nova_peca()

        # Reinicia a lista de movimentos planejados pela
        # inteligência artificial (IA), se houver.
        self.movimentos_ia = []

        # Verifica se a nova peça gerada colide imediatamente após ser criada.
        # Isso pode acontecer se a grade estiver cheia.
        if self.verificar_colisao():

            # Se houver uma colisão imediata, marca o fim do jogo.
            self.fim_de_jogo = True

    def limpar_linhas(self):

        # Cria uma lista vazia para armazenar os índices das linhas que estão
        # completamente preenchidas e devem ser removidas.
        linhas_para_remover = []

        # Itera sobre cada linha da grade para verificar se a linha
        # está completamente preenchida.
        for i in range(LINHAS):

            # Verifica se o número 0 (que representa um espaço vazio)
            # não está presente na linha atual.
            # Se 0 não estiver presente, significa que a linha está
            # completamente preenchida.
            if 0 not in self.grade[i]:

                # Adiciona o índice da linha à lista de linhas para remover.
                linhas_para_remover.append(i)

        # Itera sobre cada linha que precisa ser removida.
        for linha in linhas_para_remover:

            # Remove a linha da grade. `del` é usado para deletar a
            # linha no índice especificado.
            del self.grade[linha]

            # Insere uma nova linha vazia no topo da grade para
            # manter o mesmo número de linhas.
            # A nova linha é inserida com todos os espaços representados
            # por 0, indicando que estão vazios.
            self.grade.insert(0, [0 for _ in range(COLUNAS)])

            # Incrementa a pontuação do jogador em 1 ponto para
            # cada linha removida.
            self.pontuacao += 1

    def desenhar_pontuacao(self):

        # Utiliza a fonte definida anteriormente para criar uma
        # imagem de texto que mostra a pontuação atual.
        # `FONTE.render` gera uma superfície com o texto renderizado.
        # O primeiro argumento é o texto a ser renderizado.
        # O segundo argumento `True` indica o uso de antialiasing,
        # tornando o texto mais suave e legível.
        # O terceiro argumento `PRETO` define a cor do texto.
        texto = FONTE.render(f'Pontuação: {self.pontuacao}', True, PRETO)

        # Posiciona a superfície de texto na tela.
        # `self.tela.blit` é um método que desenha uma superfície sobre outra.
        # Neste caso, desenha o texto na tela do jogo.
        # O primeiro argumento é a superfície do texto a ser desenhado.
        # O segundo argumento é a posição (x, y) onde o texto será colocado.
        # Aqui, `LARGURA + 20` calcula uma posição 20 pixels para a direita
        # do limite direito da área de jogo,
        # e `20` é a posição vertical, um pouco abaixo do topo
        # da tela, proporcionando uma margem visual.
        self.tela.blit(texto, (LARGURA + 20, 20))

    def desenhar_botao_ia(self):

        # Determina a cor do botão com base no estado da IA.
        # Se a IA não estiver ativa, o botão será verde (RGB: 0, 200, 0),
        # indicando que pode ser ativada.
        # Se a IA estiver ativa, o botão será vermelho (RGB: 200, 0, 0),
        # indicando que pode ser desativada.
        cor_botao = (0, 200, 0) if not self.ia_ativa else (200, 0, 0)

        # Define o texto do botão baseado no estado da IA.
        # Se a IA estiver desativada, o texto será "Ativar IA".
        # Se a IA estiver ativada, o texto será "Desativar IA".
        texto_botao = "Ativar IA" if not self.ia_ativa else "Desativar IA"

        # Desenha o retângulo que representa o botão na tela.
        # A cor do botão é definida pela variável `cor_botao`.
        # A posição e tamanho do botão são definidos pelas
        # coordenadas (LARGURA + 20, 100) e tamanho (150, 40).
        pygame.draw.rect(self.tela, cor_botao, (LARGURA + 20, 100, 150, 40))

        # Renderiza o texto do botão usando a fonte definida anteriormente.
        # `FONTE.render` cria uma superfície com o texto.
        # O primeiro argumento é o texto a ser renderizado.
        # O segundo argumento `True` indica que o texto será suavizado (antialiasing).
        # O terceiro argumento `BRANCO` define a cor do texto.
        texto = FONTE.render(texto_botao, True, BRANCO)

        # Desenha a superfície do texto na tela, posicionando-a dentro do botão.
        # As coordenadas (LARGURA + 40, 110) posicionam o texto de forma
        # centralizada no botão, considerando as margens.
        self.tela.blit(texto, (LARGURA + 40, 110))


    def controlar_ia(self):

        # Verifica se já existem movimentos planejados pela IA. Se sim,
        # não calcula novos movimentos.
        if self.movimentos_ia:

            # Se a lista de movimentos da IA não estiver vazia, interrompe a
            # função, pois já há movimentos planejados.
            return

        # Inicializa variáveis para armazenar a melhor pontuação e o
        # melhor movimento encontrados pela IA.
        melhor_pontuacao = None
        melhor_movimento = None

        # Guarda a forma original da peça atual para futuras
        # comparações e manipulações.
        forma_original = self.peca_atual['forma']

        # Tenta cada uma das quatro possíveis rotações da
        # peça (0, 90, 180, 270 graus).
        for rotacao in range(4):

            # Inicialmente, a forma rotacionada é igual à forma original.
            forma_rotacionada = forma_original

            # Aplica a rotação necessária de acordo com o índice da iteração.
            for _ in range(rotacao):

                # A função `rotacionar_peca` é chamada para rotacionar a peça.
                # Esta função altera a orientação da matriz da peça,
                # simulando uma rotação física da peça no jogo.
                forma_rotacionada = self.rotacionar_peca(forma_rotacionada)

            # Calcula a largura da forma rotacionada para determinar os
            # limites de movimento horizontais.
            largura_forma = len(forma_rotacionada[0])

            # Ajusta o intervalo de x para posições válidas onde a peça
            # pode ser colocada.
            # O mínimo e máximo de x são calculados baseados nos blocos
            # ativos da peça em sua forma rotacionada.
            # 'x_min' calcula a posição mais à esquerda onde a peça pode
            # iniciar sem ultrapassar os limites do lado esquerdo da grade.

            # Aqui, um loop compreensivo de lista é usado para iterar sobre
            # cada linha 'y' e cada coluna 'x' na forma rotacionada da peça.
            # O loop verifica cada valor 'val' nas posições da matriz da peça.
            # Se 'val' é positivo (indicando parte da peça), o índice 'x'
            # dessa posição é coletado.
            # A função 'min' então encontra o menor valor de 'x' coletado, que
            # indica o ponto mais à esquerda onde um bloco da peça existe.
            # O resultado negativo desse valor mínimo é tomado porque se a
            # parte mais à esquerda da peça está em uma posição x,
            # então a peça pode tecnicamente ser movida para a esquerda
            # até esse valor sem sair da grade.
            x_min = -min([x for y in forma_rotacionada for x, val in enumerate(y) if val])

            # 'x_max' calcula a posição mais à direita onde a peça pode iniciar
            # sem ultrapassar os limites do lado direito da grade.
            # Similarmente, o loop coleta índices 'x' para cada parte
            # ativa da peça ('val' positivo).
            # 'max' encontra o maior valor de 'x', indicando a parte
            # mais à direita da peça.
            # Subtrai-se esse valor do número total de colunas na grade (COLUNAS) e
            # ajusta-se por 1 para manter a peça dentro dos limites visíveis da tela.
            # Isso determina até onde a parte mais à direita da peça pode iniciar
            # antes de ultrapassar o limite direito da grade.
            x_max = COLUNAS - max([x for y in forma_rotacionada for x, val in enumerate(y) if val]) - 1

            # Itera sobre todas as posições horizontais válidas dentro
            # dos limites calculados.
            for x_pos in range(x_min, x_max + 1):

                # Inicia a posição y da peça na parte superior da grade.
                # A variável y_pos é usada para rastrear a queda da peça desde o
                # topo até a posição onde ela colidiria com outra peça
                # ou com o fundo da grade.
                y_pos = 0

                # Verifica continuamente se mover a peça mais para baixo causaria uma colisão.
                # A função 'verificar_colisao' é chamada com deslocamentos ajustados
                # para testar se colocar a peça uma linha abaixo na próxima
                # iteração causará colisão.
                while not self.verificar_colisao(desloc_x=x_pos - self.peca_atual['x'], desloc_y=y_pos + 1,
                                                 forma=forma_rotacionada):
                    # Se não houver colisão ao mover a peça para baixo, incrementa y_pos
                    # para testar a próxima linha abaixo.
                    y_pos += 1

                # Avalia a posição atual da peça na grade para determinar sua
                # pontuação com base em critérios definidos.
                # A função 'avaliar_grade' calcula a pontuação com base na configuração
                # atual da grade e na posição da peça,
                # considerando fatores como completar linhas, a altura da pilha
                # de peças, e outros critérios heurísticos.
                pontuacao = self.avaliar_grade(forma_rotacionada, x_pos, self.peca_atual['y'] + y_pos)

                # Ignora posições inválidas onde a pontuação é mínima.
                # Se a pontuação retornada for '-inf', isso indica uma posição
                # inválida ou desfavorável, e essa posição é ignorada.
                if pontuacao == float('-inf'):
                    continue

                # Se a pontuação atual for melhor que a melhor pontuação encontrada até
                # agora, atualiza a melhor pontuação e o movimento correspondente.
                if melhor_pontuacao is None or pontuacao > melhor_pontuacao:

                    # Se ainda não há uma melhor pontuação (isto é, no primeiro cálculo),
                    # ou se a pontuação atual é maior que a melhor já registrada,
                    # então a pontuação atual se torna a melhor pontuação.
                    melhor_pontuacao = pontuacao

                    # Atualiza o 'melhor_movimento' com as informações da posição e
                    # rotação que resultaram nessa melhor pontuação.
                    melhor_movimento = {

                        # Guarda a rotação que foi testada (0, 1, 2 ou 3, que
                        # correspondem a 0, 90, 180 e 270 graus).
                        'rotacao': rotacao,

                        # Registra a posição horizontal (x) onde a peça seria
                        # colocada para obter essa pontuação.
                        'x': x_pos,

                        # Registra a posição vertical final (y) onde a peça deve parar.
                        # Isso corresponde à maior altura em que a peça não colide.
                        'y': self.peca_atual['y'] + y_pos,

                        # Guarda a forma rotacionada que foi testada.
                        'forma': forma_rotacionada

                    }

        # Se 'melhor_movimento' foi encontrado, isto é, se a IA encontrou um
        # movimento ideal para a peça atual:
        if melhor_movimento:

            # Inicializa a lista de movimentos da IA como vazia.
            # Esta lista será preenchida com as ações que a IA deve
            # realizar (rotacionar, mover para a direita,
            # esquerda, ou para baixo).
            self.movimentos_ia = []

            # Rotaciona a peça o número de vezes necessário para alcançar a
            # rotação definida em 'melhor_movimento'.
            # Por exemplo, se 'melhor_movimento['rotacao']' for 2, isso significa
            # que a peça deve ser rotacionada duas vezes.
            for _ in range(melhor_movimento['rotacao']):

                # Adiciona o comando 'rotacionar' na lista de movimentos
                # para cada rotação necessária.
                self.movimentos_ia.append('rotacionar')

            # Calcula o deslocamento horizontal necessário para mover a
            # peça da sua posição atual para a posição ideal 'x'.
            desloc_x = melhor_movimento['x'] - self.peca_atual['x']

            # Se o deslocamento horizontal for positivo (maior que 0), a
            # peça deve ser movida para a direita.
            if desloc_x > 0:

                # Adiciona o comando 'direita' várias vezes, uma vez para
                # cada passo necessário para mover a peça até o destino.
                self.movimentos_ia.extend(['direita'] * desloc_x)

            # Se o deslocamento horizontal for negativo (menor que 0), a
            # peça deve ser movida para a esquerda.
            elif desloc_x < 0:

                # Adiciona o comando 'esquerda' várias vezes, uma vez para cada
                # passo necessário para mover a peça até o destino.
                self.movimentos_ia.extend(['esquerda'] * (-desloc_x))

            # Calcula o deslocamento vertical necessário para mover a peça da
            # sua posição atual para a posição ideal 'y'.
            desloc_y = melhor_movimento['y'] - self.peca_atual['y']

            # Se o deslocamento vertical for positivo, a peça deve ser movida para baixo.
            # Note que não há necessidade de verificar um deslocamento negativo,
            # pois isso implicaria em mover a peça para cima, o
            # que não ocorre no Tetris.
            if desloc_y > 0:

                # Adiciona o comando 'baixo' várias vezes, uma vez para cada
                # passo necessário para mover a peça até o destino.
                self.movimentos_ia.extend(['baixo'] * desloc_y)

    def avaliar_grade(self, forma, x_pos, y_pos):

        # Cria uma cópia temporária da grade atual. A cópia é usada para
        # simular a colocação da peça sem modificar a grade real.
        # 'linha[:]' faz uma cópia rasa de cada linha da grade.
        grade_temporaria = [linha[:] for linha in self.grade]

        # Itera sobre cada linha e cada bloco da forma da peça para
        # simular sua posição na grade.
        for y, linha in enumerate(forma):
            for x, valor in enumerate(linha):

                # Verifica se o valor do bloco é 1 (ou seja, parte da peça).
                # Blocos com valor 0 são espaços vazios.
                if valor:

                    # Calcula o índice da posição x (horizontal) na grade
                    # onde o bloco da peça seria colocado.
                    x_indice = x_pos + x

                    # Calcula o índice da posição y (vertical) na grade onde o
                    # bloco da peça seria colocado.
                    y_indice = y_pos + y

                    # Verifica se os índices estão dentro dos limites da grade.
                    # Se o bloco estiver fora dos limites horizontais ou
                    # verticais, a posição é inválida.
                    if x_indice < 0 or x_indice >= COLUNAS or y_indice >= LINHAS:

                        # Retorna uma pontuação mínima (infinito negativo)
                        # para posições inválidas.
                        return float('-inf')

                        # Se o índice y for válido (não fora do limite superior),
                        # coloca a peça na grade temporária.
                    if y_indice >= 0:
                        grade_temporaria[y_indice][x_indice] = self.peca_atual['cor']

        # Conta quantas linhas completas existem na grade temporária.
        # Linhas completas são aquelas que não têm nenhum espaço vazio (0).
        linhas_completas = sum([1 for linha in grade_temporaria if 0 not in linha])

        # Calcula a altura da pilha de peças na grade temporária.
        # Isso influencia a pontuação, já que menos altura é melhor.
        altura = self.calcular_altura(grade_temporaria)

        # Conta o número de buracos (espaços vazios sob peças) na grade
        # temporária. Quanto mais buracos, pior a posição.
        buracos = self.contar_buracos(grade_temporaria)

        # Calcula a irregularidade da superfície da grade (diferença
        # de altura entre colunas adjacentes).
        # Menos irregularidade é preferível, pois facilita o encaixe das próximas peças.
        irregularidade = self.calcular_irregularidade(grade_temporaria)

        # Calcula o "contato", que é a quantidade de blocos que estão
        # em contato com o chão ou com outras peças.
        # Mais contato geralmente significa que a peça está mais estável.
        contato = self.calcular_contato(grade_temporaria)

        # Avalia a pontuação da posição simulada. Os pesos multiplicam os
        # valores de cada fator para ajustar sua importância.
        # Linhas completas têm um peso muito alto (1000 pontos por linha),
        # enquanto buracos têm um grande peso negativo (-50 por buraco).
        # A altura da pilha de peças e a irregularidade também são penalizadas,
        # enquanto o contato é recompensado.
        return (linhas_completas * 1000) - (altura * 2) - (buracos * 50) - (irregularidade * 10) + (contato * 5)

    def contar_buracos(self, grade):

        # Inicializa a variável 'buracos' com zero, que será usada para
        # contar o número total de buracos na grade.
        buracos = 0

        # Itera sobre todas as colunas da grade.
        for x in range(COLUNAS):

            # Inicializa uma variável 'bloco_encontrado' como False, que
            # será usada para marcar quando encontramos o primeiro bloco
            # em uma coluna. Isso é importante porque só podemos ter
            # buracos após encontrarmos um bloco.
            bloco_encontrado = False

            # Itera sobre todas as linhas da coluna, de cima para
            # baixo (linha 0 até a última linha).
            for y in range(LINHAS):

                # Se a célula na linha 'y' e coluna 'x' contiver um bloco (valor diferente de 0),
                # isso significa que encontramos
                # um bloco nessa coluna.
                if grade[y][x]:

                    # Marca que encontramos um bloco nesta coluna.
                    bloco_encontrado = True

                    # Se já encontramos um bloco (bloco_encontrado é True) e a
                    # célula atual está vazia (valor igual a 0),
                    # então essa célula é um buraco, já que há um bloco acima dela.
                elif bloco_encontrado and not grade[y][x]:

                    # Incrementa o contador de buracos.
                    buracos += 1

        # Retorna o número total de buracos encontrados na grade.
        return buracos


    def calcular_altura(self, grade):

        # Itera sobre cada linha da grade, começando da linha mais alta (y = 0)
        # até a linha mais baixa (y = LINHAS - 1).
        for y in range(LINHAS):

            # 'any(grade[y])' verifica se há algum bloco (valor diferente de 0) na linha 'y'.
            # Se houver pelo menos um bloco nesta linha, significa
            # que a linha não está vazia.
            if any(grade[y]):

                # Retorna a altura da pilha de peças. A altura é calculada
                # subtraindo o índice da linha 'y'
                # do número total de linhas (LINHAS). Isso indica quantas
                # linhas de peças estão ocupadas a partir do topo.
                return LINHAS - y

        # Se nenhuma linha tiver peças (ou seja, a grade estiver
        # completamente vazia), retorna 0 como a altura.
        return 0


    def calcular_irregularidade(self, grade):

        # Inicializa a variável 'irregularidade' como 0. Esta variável
        # vai armazenar a soma das diferenças de altura
        # entre colunas adjacentes.
        irregularidade = 0

        # Inicializa uma lista chamada 'alturas' que vai armazenar a
        # altura de cada coluna na grade.
        alturas = []

        # Itera sobre cada coluna da grade (de 0 até o número total de colunas).
        for x in range(COLUNAS):

            # Inicializa a variável 'altura_coluna' como 0. Esta variável
            # vai armazenar a altura da pilha de peças na coluna 'x'.
            altura_coluna = 0

            # Itera sobre cada linha da coluna (de cima para baixo).
            for y in range(LINHAS):

                # Se a célula atual (linha 'y' e coluna 'x') contém um
                # bloco (valor diferente de 0),
                # então encontramos a altura da coluna.
                if grade[y][x]:

                    # Calcula a altura da coluna subtraindo a linha atual 'y'
                    # do número total de linhas 'LINHAS'.
                    # Isso nos dá a altura da coluna desde o fundo da grade.
                    altura_coluna = LINHAS - y

                    # Uma vez que encontramos um bloco, podemos parar de
                    # verificar as outras linhas dessa coluna.
                    break

                    # Adiciona a altura encontrada para esta coluna à lista 'alturas'.
            alturas.append(altura_coluna)

        # Agora que temos as alturas de todas as colunas, vamos calcular a
        # diferença de altura entre colunas adjacentes.
        for i in range(1, len(alturas)):

            # A diferença de altura entre a coluna atual 'alturas[i]' e a
            # coluna anterior 'alturas[i - 1]'
            # é somada à variável 'irregularidade'. 'abs' garante
            # que a diferença seja sempre positiva.
            irregularidade += abs(alturas[i] - alturas[i - 1])

        # Retorna a soma total das irregularidades, que indica o
        # quão "acidentada" está a superfície da pilha de peças.
        return irregularidade

    def calcular_contato(self, grade):

        # Inicializa a variável 'contato' com 0. Esta variável vai
        # armazenar o número total de contatos na grade.
        contato = 0

        # Itera sobre todas as linhas da grade.
        for y in range(LINHAS):

            # Itera sobre todas as colunas da grade.
            for x in range(COLUNAS):

                # Se a célula atual (grade[y][x]) contém um bloco (valor diferente de 0),
                # então começamos a verificar os contatos dessa célula
                # com outras células ao redor.
                if grade[y][x]:

                    # Verifica se há contato abaixo do bloco atual.
                    # Se o bloco estiver na última linha (y + 1 >= LINHAS),
                    # então ele está em contato com o chão.
                    # Ou, se houver um bloco na célula diretamente abaixo (grade[y + 1][x]),
                    # isso também conta como um contato.
                    if y + 1 >= LINHAS or grade[y + 1][x]:

                        # Incrementa o contador de contatos.
                        contato += 1

                    # Verifica se há contato à esquerda do bloco atual.
                    # Se o bloco estiver na primeira coluna (x - 1 < 0), então
                    # ele está em contato com a borda esquerda.
                    # Ou, se houver um bloco à esquerda (grade[y][x - 1]),
                    # isso também conta como um contato.
                    if x - 1 < 0 or grade[y][x - 1]:
                        contato += 1

                    # Verifica se há contato à direita do bloco atual.
                    # Se o bloco estiver na última coluna (x + 1 >= COLUNAS),
                    # então ele está em contato com a borda direita.
                    # Ou, se houver um bloco à direita (grade[y][x + 1]), isso
                    # também conta como um contato.
                    if x + 1 >= COLUNAS or grade[y][x + 1]:
                        contato += 1

                    # Verifica se há contato acima do bloco atual.
                    # Se o bloco estiver na primeira linha (y - 1 < 0), então
                    # ele está em contato com a borda superior.
                    # Ou, se houver um bloco diretamente acima (grade[y - 1][x]),
                    # isso também conta como um contato.
                    if y - 1 < 0 or grade[y - 1][x]:
                        contato += 1

        # Retorna o número total de contatos. Quanto maior o valor,
        # mais estável é a posição da peça.
        return contato


    def rodar(self):

        # Inicializa o jogo com uma nova peça. Este método gera
        # uma nova peça para o jogador ou IA mover.
        self.nova_peca()

        # Inicia o loop principal do jogo. Este loop continua rodando
        # enquanto o jogo não tiver terminado (fim_de_jogo == False).
        while not self.fim_de_jogo:

            # Limpa a tela, preenchendo-a com a cor branca, para
            # preparar a renderização de novos elementos.
            self.tela.fill(BRANCO)

            # 'delta_tempo' armazena o tempo (em milissegundos) que passou
            # desde a última iteração do loop.
            # Isso ajuda a sincronizar o jogo com o relógio do sistema,
            # evitando que ele rode muito rápido ou devagar.
            delta_tempo = self.relogio.tick()

            # Adiciona o tempo que passou à variável 'tempo_passado',
            # que controla a queda automática das peças.
            self.tempo_passado += delta_tempo

            # Verifica se a IA está ativada. Caso positivo, a IA
            # controla os movimentos da peça.
            if self.ia_ativa:

                # Acumula o tempo passado desde o último movimento da IA.
                self.tempo_movimento_ia += delta_tempo

                # Se o tempo acumulado pela IA exceder o atraso
                # definido (atraso_movimento_ia), executa o próximo movimento.
                if self.tempo_movimento_ia > self.atraso_movimento_ia:

                    # Reseta o temporizador de movimentos da IA.
                    self.tempo_movimento_ia = 0

                    # Se não há movimentos programados pela IA, chama a
                    # função para a IA calcular os melhores movimentos.
                    if not self.movimentos_ia:
                        self.controlar_ia()

                    # Se existem movimentos programados pela IA, executa o
                    # próximo movimento da lista de movimentos.
                    if self.movimentos_ia:

                        # Retira o primeiro movimento da lista de movimentos
                        # programados pela IA. A função pop(0) remove e retorna
                        # o primeiro item da lista, que é o próximo movimento a ser executado.
                        proximo_movimento = self.movimentos_ia.pop(0)

                        # Verifica se o próximo movimento é 'esquerda'. Além disso,
                        # chama a função verificar_colisao para garantir
                        # que mover a peça para a esquerda não causará uma colisão
                        # com outra peça ou a parede da grade.
                        # Se não houver colisão, move a peça atual uma coluna para a
                        # esquerda (diminuindo o valor de x).
                        if proximo_movimento == 'esquerda' and not self.verificar_colisao(desloc_x=-1):
                            self.peca_atual['x'] -= 1  # Move a peça para a esquerda.

                        # Verifica se o próximo movimento é 'direita'. Se for,
                        # verifica se há colisão ao mover a peça para a direita.
                        # Se não houver colisão, move a peça atual uma coluna para a
                        # direita (aumentando o valor de x).
                        elif proximo_movimento == 'direita' and not self.verificar_colisao(desloc_x=1):
                            self.peca_atual['x'] += 1  # Move a peça para a direita.

                        # Verifica se o próximo movimento é 'rotacionar', ou seja, a
                        # IA deseja rotacionar a peça.
                        # A peça é rotacionada chamando o método rotacionar_peca, que
                        # retorna a nova forma rotacionada.
                        # Em seguida, verifica se a rotação causaria uma colisão.
                        # Se não causar, aplica a nova rotação à peça atual.
                        elif proximo_movimento == 'rotacionar':
                            nova_forma = self.rotacionar_peca()  # Rotaciona a peça.
                            if not self.verificar_colisao(forma=nova_forma):
                                self.peca_atual['forma'] = nova_forma  # Aplica a rotação se for válida.

                        # Verifica se o próximo movimento é 'baixo'. A IA deseja
                        # mover a peça para baixo.
                        # Verifica se mover para baixo causaria uma colisão.
                        # Se não houver colisão, move a peça uma linha para baixo.
                        # Se houver colisão (a peça não pode descer mais), a peça é
                        # fixada na grade chamando o método fixar_peca.
                        elif proximo_movimento == 'baixo':
                            if not self.verificar_colisao(desloc_y=1):
                                self.peca_atual['y'] += 1  # Move a peça uma linha para baixo.
                            else:
                                self.fixar_peca()  # Fixa a peça na posição atual se colidir com o fundo ou outra peça.


                else:

                    # Se a IA está ativa mas o atraso de movimento (atraso_movimento_ia)
                    # ainda não foi atingido,
                    # o jogo continua a controlar a queda automática da peça,
                    # simulando a gravidade.

                    # Se o tempo acumulado ('tempo_passado') desde a última queda da
                    # peça exceder o tempo de queda definido ('frequencia_queda'),
                    # isso significa que a peça precisa descer uma linha
                    # para simular a gravidade.
                    if self.tempo_passado > self.frequencia_queda:

                        # Reseta o temporizador de queda, ou seja, 'tempo_passado' volta a
                        # zero para começar a contar o tempo até a próxima queda.
                        self.tempo_passado = 0

                        # Verifica se a peça pode descer uma linha sem colidir com
                        # outra peça ou o fundo da grade.
                        # A função 'verificar_colisao' verifica se mover a peça
                        # para baixo (desloc_y=1) causaria uma colisão.
                        if not self.verificar_colisao(desloc_y=1):

                            # Se não houver colisão, a peça desce uma linha,
                            # incrementando o valor de 'y' em 1.
                            self.peca_atual['y'] += 1

                        else:

                            # Se houver uma colisão (a peça atinge outra peça ou o
                            # fundo da grade), a peça é "fixada" na posição atual.
                            # Isso significa que a peça não poderá mais se mover ou descer, e
                            # o jogo vai gerar uma nova peça.
                            self.fixar_peca()


            else:
                # Se a IA não está ativa (o jogador está controlando a peça
                # manualmente), a queda automática das peças (gravidade) continua.

                # Verifica se o tempo acumulado ('tempo_passado') excedeu o
                # tempo de queda definido ('frequencia_queda').
                # Isso significa que a peça precisa descer uma linha
                # para simular a gravidade.
                if self.tempo_passado > self.frequencia_queda:

                    # Reseta o temporizador de queda, ou seja, 'tempo_passado'
                    # volta a zero para que o ciclo de queda continue.
                    self.tempo_passado = 0

                    # Verifica se é possível mover a peça uma linha para baixo sem
                    # colidir com outras peças ou com o fundo da grade.
                    # A função 'verificar_colisao' é chamada com 'desloc_y=1', o que
                    # significa que estamos tentando mover a peça para baixo.
                    if not self.verificar_colisao(desloc_y=1):

                        # Se não houver colisão, a peça desce uma linha. Isso é
                        # feito incrementando o valor de 'y' em 1.
                        self.peca_atual['y'] += 1

                    else:

                        # Se houver colisão (a peça atinge o fundo da grade ou
                        # outra peça), a peça é "fixada" na posição atual.
                        # Isso significa que a peça não pode mais se mover e
                        # o jogo gera uma nova peça.
                        self.fixar_peca()

            # Itera sobre todos os eventos capturados pelo Pygame.
            for evento in pygame.event.get():

                # Verifica se o evento é o fechamento da janela do jogo.
                # Se o jogador clicar no botão de fechar (evento QUIT), o jogo é encerrado.
                if evento.type == pygame.QUIT:
                    pygame.quit()  # Fecha o Pygame corretamente.
                    sys.exit()  # Sai do programa.

                # Verifica se o evento é uma tecla sendo pressionada (KEYDOWN) e
                # se a IA não está ativa (ou seja, o jogador está controlando).
                # Isso impede que o jogador faça movimentos enquanto a IA está no controle.
                if evento.type == pygame.KEYDOWN and not self.ia_ativa:

                    # Se a tecla pressionada for a seta para a esquerda (K_LEFT) e
                    # não houver colisão ao tentar mover a peça para a esquerda,
                    # então o jogo permite que a peça seja movida para a esquerda,
                    # diminuindo o valor de 'x' da peça em 1.
                    if evento.key == pygame.K_LEFT and not self.verificar_colisao(desloc_x=-1):
                        self.peca_atual['x'] -= 1  # Move a peça uma posição para a esquerda.

                    # Se a tecla pressionada for a seta para a direita (K_RIGHT) e
                    # não houver colisão ao tentar mover a peça para a direita,
                    # então o jogo permite que a peça seja movida para a direita,
                    # aumentando o valor de 'x' da peça em 1.
                    if evento.key == pygame.K_RIGHT and not self.verificar_colisao(desloc_x=1):
                        self.peca_atual['x'] += 1  # Move a peça uma posição para a direita.

                    # Se a tecla pressionada for a seta para baixo (K_DOWN) e não houver
                    # colisão ao tentar mover a peça para baixo,
                    # então o jogo permite que a peça desça uma linha,
                    # aumentando o valor de 'y' da peça em 1.
                    if evento.key == pygame.K_DOWN and not self.verificar_colisao(desloc_y=1):
                        self.peca_atual['y'] += 1  # Move a peça uma linha para baixo.

                    # Se a tecla pressionada for a seta para cima (K_UP), o
                    # jogador está tentando rotacionar a peça.
                    if evento.key == pygame.K_UP:

                        # A função 'rotacionar_peca()' é chamada para criar
                        # uma nova forma rotacionada.
                        nova_forma = self.rotacionar_peca()  # Gera a nova forma rotacionada da peça.

                        # O jogo então verifica se essa nova rotação causaria uma
                        # colisão. Se a nova forma não colide com nada,
                        # a peça pode ser rotacionada com segurança, então o valor
                        # da 'forma' da peça atual é atualizado para a nova forma rotacionada.
                        if not self.verificar_colisao(forma=nova_forma):
                            self.peca_atual[
                                'forma'] = nova_forma  # Aplica a rotação à peça se for válida, sem causar colisões.

                # Verifica se o evento foi um clique do mouse (MOUSEBUTTONDOWN).
                # Isso captura quando o jogador clica em qualquer lugar na tela do jogo.
                if evento.type == pygame.MOUSEBUTTONDOWN:

                    # Obtém as coordenadas x e y da posição do mouse no momento do clique.
                    # 'pygame.mouse.get_pos()' retorna a posição atual do
                    # cursor do mouse no formato (x, y).
                    x_mouse, y_mouse = pygame.mouse.get_pos()

                    # Verifica se o clique foi dentro da área do botão IA.
                    # O botão IA está representado por um retângulo definido
                    # pelas coordenadas (LARGURA + 20, 100)
                    # e com uma largura de 150 pixels e altura de 40 pixels.
                    # A expressão LARGURA + 20 <= x_mouse <= LARGURA + 170 verifica
                    # se o clique foi horizontalmente dentro do botão,
                    # e 100 <= y_mouse <= 140 verifica se o clique foi
                    # verticalmente dentro do botão.
                    if LARGURA + 20 <= x_mouse <= LARGURA + 170 and 100 <= y_mouse <= 140:

                        # Alterna o estado da IA. Se a IA estava desativada, ela
                        # será ativada; se estava ativada, será desativada.
                        # 'not self.ia_ativa' inverte o estado atual de 'ia_ativa'.
                        self.ia_ativa = not self.ia_ativa

                        # Limpa a lista de movimentos programados pela IA.
                        # Isso é feito para garantir que, ao alternar o estado da IA,
                        # ela comece a calcular novos movimentos
                        # a partir do zero, sem utilizar comandos de movimento
                        # anteriores que podem não fazer mais sentido.
                        self.movimentos_ia = []

            # Chama o método para desenhar a grade na tela. A grade é a
            # matriz de células onde as peças do Tetris
            # se movem e se encaixam. Cada célula da grade pode estar
            # vazia ou conter parte de uma peça.
            self.desenhar_grade()

            # Chama o método para desenhar a peça atual na tela, com base
            # na posição e formato atual da peça.
            # Isso garante que a peça controlada pelo jogador ou IA
            # seja visível na tela.
            self.desenhar_peca()


            # Chama o método para desenhar a pontuação do jogador na tela.
            # A pontuação é atualizada à medida que
            # o jogador remove linhas completando a grade.
            self.desenhar_pontuacao()

            # Chama o método para desenhar o botão da IA na tela. O botão
            # permite ao jogador alternar entre controlar a peça
            # manualmente ou ativar a IA para controlar a peça.
            # O estado atual da IA (ativa ou desativada) também é mostrado.
            self.desenhar_botao_ia()

            # Atualiza a tela do Pygame com as mudanças feitas até agora.
            # Todos os desenhos realizados (grade, peça, pontuação,
            # botão IA) são exibidos na tela do jogo, garantindo que o
            # jogador veja a atualização visual do estado do jogo.
            pygame.display.update()

            # Verifica se o estado do jogo é "fim de jogo". Se for, o jogo foi
            # perdido, e a mensagem "Fim de Jogo" é exibida.
            if self.fim_de_jogo:

                # Cria o texto "Fim de Jogo" com uma determinada fonte (FONTE) e cor (PRETO).
                # O método 'render' do objeto fonte gera uma superfície de
                # texto que pode ser exibida na tela.
                texto_game_over = FONTE.render("Fim de Jogo", True, PRETO)

                # Desenha o texto "Fim de Jogo" na tela do Pygame, centralizado
                # na largura da tela.
                # A posição x é calculada para centralizar o texto na
                # metade da largura da tela menos 50 pixels,
                # e a posição y é no meio da altura da tela.
                self.tela.blit(texto_game_over, (LARGURA // 2 - 50, ALTURA // 2))

                # Atualiza a tela do Pygame para que a mensagem "Fim de Jogo"
                # seja visível ao jogador.
                pygame.display.update()

                # Aguarda 2 segundos (2000 milissegundos) antes de fechar o
                # jogo, permitindo que o jogador
                # veja a mensagem "Fim de Jogo" por um breve período.
                pygame.time.wait(2000)

                # Encerra o Pygame corretamente, liberando todos os recursos utilizados.
                pygame.quit()

                # Sai do programa, encerrando o jogo completamente.
                sys.exit()


# Cria uma instância da classe 'Tetris'.
# Isso inicializa o jogo, criando a grade, configurando as
        # variáveis necessárias,
        # e preparando o ambiente do Pygame para
        # desenhar o jogo na tela.
jogo = Tetris()

# Chama o método 'rodar()' da instância 'jogo', que inicia o
        # loop principal do jogo.
# O método 'rodar()' mantém o jogo rodando, processa eventos (como
        # teclas pressionadas e cliques de mouse),
        # controla o movimento das peças e a IA, e desenha
        # tudo na tela até que o jogo termine.
jogo.rodar()