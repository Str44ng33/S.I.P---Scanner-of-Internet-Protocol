import shutil
import subprocess
import time
import sys
import threading
import re
import os

def centralizar_texto(texto):
    largura_terminal = shutil.get_terminal_size().columns
    linhas = texto.split('\n')
    texto_centralizado = ""
    for linha in linhas:
        texto_centralizado += linha.center(largura_terminal) + '\n'
    return texto_centralizado

def mostrar_ascii_e_mensagem():
    ciano = '\033[96m'
    amarelo_dourado = '\033[93m'
    laranja = '\033[33m'
    reset = '\033[0m'

    ascii_art = f"""
+----------------------------------------------+
|    ________         ___        ________      |
|   |\   ____\       |\  \      |\   __  \     |
|   \ \  \___|_      \ \  \     \ \  \|\  \    |
|    \ \_____  \      \ \  \     \ \   ____\   |
|     \|____|\  \   ___\ \  \  ___\ \  \___|   |
|       ____\_\  \ |\__\ \__\|\__\ \__\      |
|      |\_________\|__| \|__|\|__| \|__|      |
|      \|_________|                            |
+----------------------------------------------+
"""
    boas_vindas = f"{amarelo_dourado}Bem-vindo ao Scanner of Internet Protocol (S.I.P){reset}"
    github_info = f"{laranja}O GitHub do criador é: https://github.com/Str44ng33{reset}"
    feito_por = f"{laranja}feito pelo Matheus 802 CMM{reset}"

    texto_completo = f"{ciano}{ascii_art}{reset}\n{boas_vindas}\n\n{github_info}\n\n{feito_por}"
    print(centralizar_texto(texto_completo))

def mostrar_tela_loading(mensagem, intervalo=0.05):
    ciano = '\033[96m'
    amarelo_lendario = '\033[93m'
    reset = '\033[0m'
    animações = ['|', '/', '-', '\\']

    sys.stdout.write(ciano + f"\n{mensagem}" + reset)
    sys.stdout.flush()

    for i in range(101):
        sys.stdout.write(f"\r{ciano}Progresso: [{'█' * (i // 2)}{' ' * (50 - i // 2)}] {i}% {animações[i % len(animações)]}{reset}")
        sys.stdout.flush()
        time.sleep(intervalo)

    # Limpa a linha após a conclusão do carregamento
    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()

    # Mensagem "Espera um pouco..."
    sys.stdout.write(f"{amarelo_lendario}Espera um pouco isso vai demorar um pouco (1 minuto ou até 5 minutos dependendo de sua máquina){reset}\n")
    sys.stdout.flush()

def formatar_resultado_nmap(resultado):
    verde = '\033[92m'
    reset = '\033[0m'

    linhas = resultado.split('\n')
    resultado_formatado = ""

    for linha in linhas:
        if "open" in linha or "closed" in linha:
            partes = re.split(r'\s+', linha.strip())
            if len(partes) >= 3:
                porta = partes[0]
                estado = partes[1]
                servico = ' '.join(partes[2:])
                estado_traduzido = "aberta" if estado == "open" else "fechada"
                resultado_formatado += f"{verde}{porta} {estado_traduzido} {servico}{reset}\n"

    return resultado_formatado

def executar_nmap_comando(comando):
    global resultado_nmap
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True, check=True)
        resultado_nmap = resultado.stdout
    except subprocess.CalledProcessError as e:
        resultado_nmap = f"\nErro ao executar o comando: {e}"

def otimizar_performance():
    """ Função para simular o uso intensivo do CPU e ajudar a acelerar o processo. """
    for _ in range(4):  # Ajuste o número de iterações conforme necessário
        [x**2 for x in range(10**6)]  # Computação intensiva simples

def mostrar_loading_ate_final(comando):
    global resultado_nmap
    # Exibe a tela de carregamento e executa o comando nmap
    loading_thread = threading.Thread(target=mostrar_tela_loading, args=("Escaneando...",))
    nmap_thread = threading.Thread(target=executar_nmap_comando, args=(comando,))

    loading_thread.start()
    otimizar_thread = threading.Thread(target=otimizar_performance)
    otimizar_thread.start()

    nmap_thread.start()
    nmap_thread.join()  # Espera a varredura nmap terminar
    otimizar_thread.join()  # Espera a otimização terminar
    loading_thread.join()  # Espera a tela de carregamento terminar

def escolher_opcao():
    global resultado_nmap
    ciano = '\033[96m'
    reset = '\033[0m'
    print(ciano + "\nLista de opções:" + reset)
    print(ciano + "1. Scannear os IPs dos dispositivos conectados no roteador através do IP do roteador" + reset)
    print(ciano + "2. Scannear as portas abertas de um dispositivo" + reset)
    escolha = input(ciano + "\nEscolha uma opção (1 ou 2): " + reset)

    if escolha == "1":
        ip_roteador = input(ciano + "Digite o IP do roteador: " + reset)
        comando = f"nmap -sn {ip_roteador}/24"
        mostrar_loading_ate_final(comando)
        print(ciano + "\nResultado da varredura:" + reset)
        print(resultado_nmap)
    elif escolha == "2":
        ip_dispositivo = input(ciano + "Digite o IP do dispositivo: " + reset)
        comando = f"nmap {ip_dispositivo}"
        mostrar_loading_ate_final(comando)
        resultado_formatado = formatar_resultado_nmap(resultado_nmap)
        print(ciano + "\nResultado da varredura:" + reset)
        print(resultado_formatado)
    else:
        print(ciano + "Escolha inválida. Por favor, selecione 1 ou 2." + reset)

if __name__ == "__main__":
    mostrar_ascii_e_mensagem()
    escolher_opcao()
