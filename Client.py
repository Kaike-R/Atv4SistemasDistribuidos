import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(("localhost", 50002))
  print(s)
  s.sendall(b"1000001,15000")

  
  dados = s.recv(1024)
  print(f"Resposta do servidor: {dados.decode()}")