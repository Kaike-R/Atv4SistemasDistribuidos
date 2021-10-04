import socket
import sympy
import concurrent.futures
from threading import Thread
import time
import csv



def CalculaPrimoMenor(n,chave):
    referencia = chave
    primos = 0
    while (primos != n):
        if sympy.isprime(referencia) == True:
            primos += 1
        if (primos != n):
            referencia -= 1
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


def CalcularPrimoMaior2(n,chave):
    return sympy.nextprime(chave,ith=n)

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

    
    

def resolve_trhread(n,chave):
    ThreadsQtdd = 5
    tamanholista = len(data)
    index = range(0, tamanholista+(tamanholista//ThreadsQtdd), tamanholista//ThreadsQtdd)
    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(CalculaPrimoMenor, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            #futures.append(future.result())
            primos += future.result()
    return primos



def leitorcsv():
    filename = "dados.csv"

    with open (filename,'r') as csvfile:
        x = None
        csvreader = csvfile.readlines()
        x = csvreader


        print("Finish")

       
print(CalculaPrimoMaior(2,15))
print(CalcularPrimoMaior2(2,15))

