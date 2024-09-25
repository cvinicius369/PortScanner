import socket
from datetime import datetime

def scan_ports(target, port_range):
    print(f"Iniciando a varredura de portas em {target}")
    
    # Registra o horário de início da varredura
    start_time = datetime.now()

    # Itera sobre o intervalo de portas especificado
    for port in port_range:
        # Cria um socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Define um tempo limite de 1 segundo para a conexão

        # Tenta se conectar à porta
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Porta {port} está ABERTA")
        else:
            print(f"Porta {port} está FECHADA")

        # Fecha o socket
        sock.close()

    # Registra o tempo total de varredura
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nVarredura concluída em: {total_time}")

# Exemplo de uso
if __name__ == "__main__":
    # Solicita o alvo e o intervalo de portas ao usuário
    target = input("Digite o endereço IP ou hostname do alvo: ")
    start_port = int(input("Digite a porta inicial: "))
    end_port = int(input("Digite a porta final: "))
    
    # Cria um intervalo de portas
    port_range = range(start_port, end_port + 1)
    
    # Executa a varredura de portas
    scan_ports(target, port_range)
