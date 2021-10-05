import socket
import csv
import time


filename = "dados.csv"

def leitorcsv():
    filename = "dados.csv"

    with open (filename,'r') as csvfile:
        
        csvreader = csvfile.readlines()
        


        return csvreader




data = leitorcsv()
port = 50002
timeout = 5


count2 = 0


while count2 < 31:
  timeout_start = time.time()
  count = 0
  while time.time()<timeout_start+timeout:
    
    #for lines in data :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      s.connect(("localhost", port))
      #s.setblocking(False)
    except:
      print("Não conectou")
    print(s)
    s.sendall(data[count].encode())

      
    dados = s.recv(1024)
    print(f"Resposta do servidor: {dados.decode()}")
    s.close()
    count = count+1
  print(count)
  count2 = count2 + 1

    