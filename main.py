import socket
import time

# Configurações iniciais
delay_split = 2  # Intervalo entre requisições consecutivas, em segundos

# Lista de hosts fictícios para os quais as requisições serão enviadas
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4",
         "192.168.1.5", "192.168.1.6", "192.168.1.7", "192.168.1.8",
         "192.168.1.9", "192.168.1.10", "192.168.1.11", "192.168.1.12"]

# Dados do proxy fictício
host_proxy = "192.168.100.100"
port_proxy = 80

# Processo de envio de requisições para cada host
for host in hosts:
    # Montagem da requisição HTTP
    http_request = f"GET http://example.com HTTP/1.1\r\n" \
                   f"Host: {host}\r\n" \
                   f"Upgrade: WebSocket\r\n" \
                   f"Connection: Upgrade\r\n" \
                   f"\r\n"  # Cabeçalhos finalizados com uma linha vazia

    # Conexão com o proxy via socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_proxy, port_proxy))  # Conecta-se ao proxy
        s.sendall(http_request.encode())  # Envia a requisição codificada em bytes
        response = b""

        # Recebimento da resposta do proxy
        while True:
            data = s.recv(4096)  # Recebe dados em blocos de 4096 bytes
            if not data:
                break  # Se não receber mais dados, interrompe o loop
            response += data  # Acumula os dados recebidos

        # Exibição da resposta
        print(f"Response from {host}:")
        print(response.decode())  # Decodifica e imprime a resposta
        print("\n" + "="*50 + "\n")  # Separador para melhor visualização entre respostas de hosts diferentes

        time.sleep(delay_split)  # Pausa entre requisições
