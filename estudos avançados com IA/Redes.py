from fpdf import FPDF 

# Criar 30 questões de múltipla escolha com 4 alternativas (A-D) e resposta correta marcada
questoes_multiplas = [
    ("Qual foi a rede precursora da internet?", ["Ethernet", "LAN", "ARPANET", "Wi-Fi"], "C"),
    ("Qual das opções é um protocolo de transferência de páginas web?", ["SMTP", "FTP", "HTTP", "IMAP"], "C"),
    ("Qual camada do modelo OSI é responsável pela entrega fim a fim?", ["Rede", "Aplicação", "Enlace", "Transporte"], "D"),
    ("Em qual camada do modelo OSI o protocolo IP atua?", ["Enlace", "Rede", "Sessão", "Física"], "B"),
    ("O que é o processo de encapsulamento?", ["Transmissão por ondas", "Criptografia de dados", "Adição de cabeçalhos por camadas", "Conexão ponto a ponto"], "C"),
    ("Qual protocolo é orientado à conexão?", ["UDP", "TCP", "IP", "HTTP"], "B"),
    ("O que caracteriza redes do tipo P2P?", ["Clientes solicitam dados", "Servidor centralizado", "Distribuição entre pares", "Conexões via satélite"], "C"),
    ("O que a camada física transmite?", ["Frames", "Segmentos", "Bits", "Pacotes"], "C"),
    ("O que define a camada de enlace?", ["Conexão entre sistemas finais", "Envio sem erros entre nós adjacentes", "Controle de aplicações", "Sincronismo de bits"], "B"),
    ("Qual função é da camada de apresentação?", ["Divisão de pacotes", "Codificação de dados", "Atribuir IP", "Transmissão de bits"], "B"),
    ("O que faz o DNS?", ["Envia e-mails", "Resolve nomes em IPs", "Criptografa dados", "Verifica erros"], "B"),
    ("Qual é a principal diferença entre TCP e UDP?", ["UDP é mais confiável", "TCP é mais leve", "TCP garante entrega ordenada", "UDP utiliza portas"], "C"),
    ("Qual meio é considerado não guiado?", ["Cabo coaxial", "Par trançado", "Fibra ótica", "Ondas de rádio"], "D"),
    ("O que é jitter?", ["Perda de pacotes", "Atraso médio", "Variação do atraso", "Velocidade do link"], "C"),
    ("A camada de rede é responsável por:", ["Codificar bits", "Sincronizar portas", "Roteamento", "Dividir quadros"], "C"),
    ("Qual camada do modelo OSI entrega quadros?", ["Física", "Rede", "Enlace", "Aplicação"], "C"),
    ("O que é vazão em redes?", ["Tempo de atraso", "Quantidade de pacotes perdidos", "Taxa de bits recebidos", "Velocidade do clock"], "C"),
    ("Qual protocolo é usado para envio de e-mails?", ["POP3", "IMAP", "SMTP", "DNS"], "C"),
    ("A camada de aplicação é responsável por:", ["Entrega física", "Gerar pacotes", "Interação com o usuário", "Roteamento de dados"], "C"),
    ("A camada de transporte atua entre:", ["Segmentos e quadros", "Enlace e física", "Rede e sessão", "Aplicação e rede"], "D"),
    ("O que o POP3 permite fazer?", ["Enviar mensagens", "Acessar DNS", "Baixar e-mails", "Roteamento"], "C"),
    ("O que define o modelo OSI como referência?", ["Possui protocolos", "É usado em redes modernas", "Define camadas e funções", "Opera na nuvem"], "C"),
    ("Qual é a unidade de dados da camada de transporte?", ["Bit", "Datagrama", "Segmento", "Quadro"], "C"),
    ("A camada de rede usa qual unidade de dados?", ["Bits", "Quadros", "Datagramas", "Segmentos"], "C"),
    ("A unidade PDU da camada de enlace é:", ["Quadro", "Bit", "Segmento", "Datagrama"], "A"),
    ("Qual camada do modelo OSI fornece o endereço físico?", ["Transporte", "Enlace", "Aplicação", "Física"], "B"),
    ("Qual tecnologia é usada para redes locais com fio?", ["Wi-Fi", "Bluetooth", "Ethernet", "Satélite"], "C"),
    ("Qual alternativa apresenta um protocolo da camada de aplicação?", ["TCP", "HTTP", "IP", "MAC"], "B"),
    ("O protocolo UDP é caracterizado por:", ["Alta confiabilidade", "Conexão orientada", "Baixa latência", "Entrega ordenada"], "C"),
    ("Qual tipo de atraso está ligado à distância física?", ["Fila", "Processamento", "Transmissão", "Propagação"], "D"),
]

# Criar PDF com as 30 questões de múltipla escolha
class QuizPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Fundamentos de Redes - 30 Questões de Múltipla Escolha", ln=True, align="C")
        self.ln(5)

pdf = QuizPDF()
pdf.add_page()
pdf.set_font("Arial", size=11)

for i, (q, options, ans) in enumerate(questoes_multiplas, 1):
    pdf.multi_cell(0, 8, f"{i}. {q}")
    for j, alt in zip("ABCD", options):
        prefix = f"   ({j}) {alt}"
        if j == ans:
            prefix += "  ✅"
        pdf.cell(0, 8, prefix, ln=True)
    pdf.ln(2)

# Salvar o PDF
quiz_path = "/mnt/data/Questoes_Multiplas_Redes.pdf"
pdf.output(quiz_path)
quiz_path
