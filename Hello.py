#def elevado2 (num):
#    result = num * num
#    return result


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


i=1
for i in range (10):
        tabuada(i)
        print("")

#for x in range(99999999):
#    print(elevado2(x))
  #  i = 1
  #  for i in range(9):
  #      print( i  ,end='', flush=True)



