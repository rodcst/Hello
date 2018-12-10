#Imprime tabuada
import random
import time

def tabuada (Numero):
    mynum = Numero
    i = 1
    for i in range(11):
        Resultado = mynum * i     
        Print = ""        
        if i >= 10:
            Print = str(mynum) + " X " + str(i) + " = "  
        else:
            Print = str(mynum) + " X  " + str(i) + " = "  
        if Resultado >= 10:
            Print = Print + "" +  str(Resultado)
        else:
            Print = Print + " " +   str(Resultado)
        print (Print)

def TodasTabuadas():
    i=1
    for i in range (10):
            tabuada(i)
            print("")

T1 = time.clock()
TodasTabuadas()
T2 = time.clock()
print ('Demorou {} Seconds' .format(T2 - T1))
