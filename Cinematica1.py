#cargar librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd    #se puede cargar mas tarde
import sys
#import scipy as sc    #no utilizada

sys.stdout

# ----------------------------------------------------------------- #
### Movimiento Rectilineo Uniforme (MRU) 
# ----------------------------------------------------------------- #

#definir datos iniciales:
xA0=0.0; xB0=100.0; vA0=3.0; vB0=-2.0;

#definir funciones
# MRU para caso especial
def fAx(t):
    return xA0+vA0*t
def fBx(t):
    return xB0+vB0*t
# MRU en general
def fMRU(x,v,t):
    return x+v*t
# MRUA en general
def fMRUA(x,v,a,t):
    return x+v*t+0.5*a*t**2

#definir arrays de numpy

tinicial=0
tfinal=50
tpasos=tfinal-tinicial+1
#tlin=np.linspace(0,50,51)
tlin=np.linspace(tinicial,tfinal,tpasos)
xlinA=fMRU(xA0,vA0,tlin)
xlinB=fMRU(xB0,vB0,tlin)



plt.title("MRU")
plt.plot(tlin,xlinA,label="A")
plt.plot(tlin,xlinB,label="B")
#forma alternativa
#plt.plot(tlin,fAx(tlin))
#plt.plot(tlin,fBx(tlin))
plt.xlabel("x[metros]")
plt.ylabel("t[segundos]")

plt.xlim(0,40)
plt.ylim(0,120)
plt.legend()
#plt.savefig('plot_MRU_1D.pdf')  
plt.show()
#plt.legend.remove()

# ----------------------------------------------------------------- #
print("\n Solucion analitica: en tcolision xA=xB, => xB-xA=0")

tcolision=-(xB0-xA0)/(vB0-vA0)
xAcolision=fAx(tcolision)
xBcolision=fBx(tcolision)

print('t colision = %3.2f ' % (tcolision))
print('xA colision = %3.1f ' % (xAcolision))
print('xB colision = %3.1f ' % (xBcolision))

# ----------------------------------------------------------------- #
# tabla de posiciones de tiempo,xA,xB:

#import pandas as pd
# libreria cargada arriba

#columns1=['t','xA','xB']

df=pd.DataFrame(tlin,columns=['t'])
xA=pd.DataFrame(xlinA,columns=['xA'])
xB=pd.DataFrame(xlinB,columns=['xB'])


df['xA']=xA['xA']
df['xB']=xB['xB']

print("\n\n -------------------------------------------------------\n")
print(" tabla de posiciones en funcion del tiempo, MRU\n")
print(df)


# ----------------------------------------------------------------- #
### Movimiento Rectilineo Uniformemente Acelerado (MRUA) 
# ----------------------------------------------------------------- #

aB=0.1
xlinC=fMRUA(xB0,vB0,aB,tlin)
xlinD=fMRUA(xB0,vB0,aB*1.5,tlin)

plt.title("MRUA")
plt.plot(tlin,xlinA,label="A")
plt.plot(tlin,xlinB,label="B, a=0")
plt.plot(tlin,xlinC,label="B, a=0.1")
plt.plot(tlin,xlinD,label="B, a=0.15")
#forma alternativa
#plt.plot(tlin,fAx(tlin))
#plt.plot(tlin,fBx(tlin))

plt.xlabel("x[metros]")
plt.ylabel("t[segundos]")

plt.xlim(0,50)
plt.ylim(0,160)
plt.legend()
#plt.savefig('plot_MRUA_1D.pdf')  
plt.show()

# ----------------------------------------------------------------- #
#movimiento relativo. 
#Definir coordinadas de posicion relativa con respecto a A.
#en este sistema A esta' quieto (con origen en A), el terreno se mueve con respecto a A.
plt.title("moviento relativo, origen en A")
xterreno=-xlinA
xAA=xlinA-xlinA
xBA=xlinB-xlinA
xCA=xlinC-xlinA
xDA=xlinD-xlinA
plt.plot(tlin,xAA,label="A")
plt.plot(tlin,xBA,label="B")
plt.plot(tlin,xCA,label="B, a=0.1")
plt.plot(tlin,xDA,label="B, a=0.15")
plt.plot(tlin,xterreno,label="posicion xA0")

plt.xlabel("x[metros]")
plt.ylabel("t[segundos]")

plt.xlim(0,50)
plt.ylim(-125,100)
plt.legend()
#plt.savefig('plot_MRUA_relativo_1D.pdf')  
plt.show()

# ----------------------------------------------------------------- #
#import pandas as pd
# libreria cargada arriba

#columns1=['t','xA','xB']

#definido arriba:
#df=pd.DataFrame(tlin,columns=['t'])
#xA=pd.DataFrame(xlinA,columns=['xA'])
#xB=pd.DataFrame(xlinB,columns=['xB'])

xC=pd.DataFrame(xlinC,columns=['xC'])

#df['xA']=xA['xA']
#df['xB']=xB['xB']
df['xC']=xC['xC']
df['xD']=fMRUA(xB0,vB0,aB*1.5,tlin)
print("\n\n -------------------------------------------------------\n")
print(" tabla de posiciones en funcion del tiempo, MRUA\n")
print(df)

dfr=pd.DataFrame(tlin,columns=['t'])
dfr['xA']=pd.DataFrame(xAA,columns=['xA'])
dfr['xB']=pd.DataFrame(xBA,columns=['xB'])
dfr['xC']=pd.DataFrame(xCA,columns=['xC'])
dfr['xD']=pd.DataFrame(xDA,columns=['xD'])

print("\n\n -------------------------------------------------------\n")
print(" tabla de posiciones relativas en funcion del tiempo, MRUA\n")
print(dfr)
print("\n -------------------------------------------------------\n")
