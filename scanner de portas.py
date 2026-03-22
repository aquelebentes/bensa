import socket
import time

target = input("Digite o IP ou domínio: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Não foi possível resolver o domínio.")
    exit()

print("-" * 50)
print(f"Escaneando alvo: {target} ({target_ip})")
print("Escaneamento iniciado...")
print("-" * 50)

start_time = time.time()

for porta in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    resultado = s.connect_ex((target_ip, porta))

    if resultado == 0:
        try:
            servico = socket.getservbyport(porta)
        except:
            servico = "serviço desconhecido"

        print(f"Porta {porta} aberta | Serviço: {servico}")

    s.close()

end_time = time.time()

print("-" * 50)
print(f"Escaneamento finalizado em {round(end_time - start_time, 2)} segundos")
