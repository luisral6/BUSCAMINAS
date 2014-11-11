import random
#import re
d={'o': 14, 'h': 7, 'y': 24, 'b': 1, 'j': 9, 'v': 21, 't': 19, 's': 18, 'f': 5, 'e': 4, 'd': 3, 'n': 13, 'l': 11, 'r': 17, 'a': 0, 'q': 16, 'g': 6, 'p': 15, 'x': 23, 'k': 10, 'i': 8, 'z': 25, 'u': 20, 'w': 22, 'c': 2, 'm': 12}
def vecinos(fila,columna,univ):
    if univ[fila][columna]=="*":
        return "*"
    cantvec=0
    for a in range(-1,2):
        for b in range(-1,2):
            px2=fila+a
            py2=columna+b
            if existe(px2,py2,univ):
                if univ[px2][py2]=="*":
                    cantvec+=1
    return cantvec
def nivel():
    global niv
    global tam
    global minas
    niv = 0
    while nivel != 1 and nivel != 2 and nivel != 3:
        niv = int(input("Escoge el nivel a jugar (1, 2 o 3): "))
        if niv == 1:
            print("\n      Nivel 1")
            minas=10
            tam=81
            return print("")
        elif niv ==2:
            tam=144
            minas=20
            print("\n      Nivel 2")
            return print("")
        elif niv == 3:
            minas=40
            tam=256
            print("\n      Nivel 3")
            return print("")
def existe(x,y,universo):
    lenght1=len(universo)
    lenght2=range(lenght1)
    if 1==lenght2.count(x):
        if 1==lenght2.count(y):
            return True
    return False
def impri(tablero,tabbol):
    global niv
    l=[]
    lenght=len(tablero)
    for x in range(0,lenght):
        for y in range(0,lenght):
            if tabbol[x][y]==True:
                l.append("[]")
                if tabbol[x][y]==False:
                    l.append(str(tablero[x][y]))
    if niv==1:
        return print("     a    b    c    d    e    f    g    h    i\n   --------------------------------------------\n 1 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 2 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 3 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 4 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 5 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 6 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 7 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 8 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------\n 9 | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n   --------------------------------------------".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23],l[24],l[25],l[26],l[27],l[28],l[29],l[30],l[31],l[32],l[33],l[34],l[35],l[36],l[37],l[38],l[39],l[40],l[41],l[42],l[43],l[44],l[45],l[46],l[47],l[48],l[49],l[50],l[51],l[52],l[53],l[54],l[55],l[56],l[57],l[58],l[59],l[60],l[61],l[62],l[63],l[64],l[65],l[66],l[67],l[68],l[69],l[70],l[71],l[72],l[73],l[74],l[75],l[76],l[77],l[78],l[79],l[80]))                        

#FALTA IMPLEMENTAR LAS PLANTILLAS DE LOS NIVELES 2 Y 3
    
lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]


jugar=True
cdj=-1
while jugar:
    nivel()
    cdj+=1
    if cdj==0:
        print("Escoja la casilla ingresando la cordenada (Ej.b6)\n")
    lenght=int(tam**.5)
    lismin=[]
    lissel=[]
    listan=[]
    for x in range(0,tam):
        lismin.append("")
        lissel.append(True)
    for x in range(0,minas):
        lismin.remove("")
        lismin.append("*")
    random.shuffle(lismin)
    lissel=lol(lissel,lenght)
    lismin=lol(lismin,lenght)
    for x in range(0,lenght):
        for y in range(0,lenght):
            listan.append(vecinos(x,y,lismin))
    listan=lol(listan,lenght)
    impri(listan,lissel)
    jg=True
    #while jg:
        
    seguir=""
    while (seguir!="Yes" and seguir !="No" and seguir !="yes" and seguir !="no"):
        seguir=str(input("\nContinue (Yes/No) : "))
    if (seguir=="No" or seguir=="no"):
        jugar=False
print("Gracias por jugar =)")


