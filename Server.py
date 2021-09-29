import socket
import sympy
import concurrent.futures
from threading import Thread
import time

def CalculaPrimoMenor(n,chave):
    referencia = chave
    primos = 0
    while (primos != n):
        if sympy.isprime(referencia) == True:
            primos += 1
        if (primos != n):
            referencia = referencia - 1
        if (referencia < 0):
            return None        
    return referencia

def CalculaPrimoMaior(n,chave):
    referencia = chave
    primos = 0
    while (primos != n):
        if sympy.isprime(referencia) == True:
            primos += 1
        if (primos != n):
            referencia += 1
    return referencia


def CalcularChave(n,chave):

    

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(CalculaPrimoMenor,n=n,chave=chave)
        future2 = executor.submit(CalculaPrimoMaior,n=n,chave=chave)
        returnValue = future.result()
        returnValue2 = future2.result()
        if(returnValue == None):
            return False
        if(returnValue2 == None):
            return False

        result = returnValue * returnValue2
        return result




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(("localhost", 50002))
  print(s)
  s.listen()
  conexao, addr = s.accept()
  with conexao:
    print(f"Cliente conectado: {addr}")
    while True:
        dados = conexao.recv(1024)
        palavra = dados.decode()
        palavra = palavra.split(",",2)
        #print(palavra[0])
        chave = CalcularChave(eval(palavra[1]),eval(palavra[0]))

        print(f"Mensagem recebida: {dados.decode()}")
        #print(CalcularChave(2,15))
        conexao.sendall(str(chave).encode())