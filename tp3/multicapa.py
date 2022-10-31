import math
import matplotlib.pyplot as plt

##comentado tenemos la logica de este perceptron con back propagation
"""def perceptron_multicapa(xor, comb):
        #pesos primera
        w0=0.9
        w1=0.7
        w2=0.5
        #pesos segunda
        w3=0.3
        w4=-0.9
        w5=-1
        #pesos tercera
        w6=0.8
        w7=0.35
        w8=0.1
        #pesos cuarta
        w9=-0.23
        w10=-0.79
        w11=0.56
        w12=0.6
        #entradas
        e0=1
        e1=0
        e2=0
        #salida deseada
        sd=0

        #PRIMER NEURONA
        #sumatoria primer neurona
        x1=(w0*e0) + (w1*e1) + (w2*e2)
        s1=1/(1+e**(-x1))
        print("s1: ", s1)

        #SEGUNDA NEURONA
        #sumatoria SEGUNDA neurona
        x2=(w3*e0) + (w4*e1) + (w5*e2)
        s2=1/(1+e**(-x2))
        print("s2: ", s2)

        #TERCER NEURONA
        #sumatoria TERCER neurona
        x3=(w6*e0) + (w7*e1) + (w8*e2)
        s3=1/(1+e**(-x3))
        print("s3: ", s3)

        #CUARTA NEURONA
        #sumatoria CUARTA neurona
        x4=(w10*s1) + (w11*s2) + (w12*s3) + (w9*e0)
        sr=1/(1+e**(-x4))
        print("Salida real: ", sr)

        E=sd-sr
        print("E: ", E)

        df=sr*(1-sr)*E
        print("df: ", df)
        print("\n")

        #learning rate
        lr=0.1

        #back propagation
        print("BACK PROPAGATION\n")
        dw9=lr*e0*df
        w9n=dw9+w9
        print("dw9: ", dw9)
        #print("w9: ", w9n)
        dw10=lr*s1*df
        w10n=dw10+w10
        print("dw10: ", dw10)
        #print("w10: ", w10n)
        dw11=lr*s2*df
        w11n=dw11+w11
        print("dw11: ", dw11)
        #print("w11: ", w11n)
        dw12=lr*s3*df
        w12n=dw12+w12
        print("dw12: ", dw12)
        #print("w12: ", w12n)

        doc1=s1*(1-s1)*df
        Dwoc1=lr*e0*doc1
        Dw0=Dwoc1
        Dw1=lr*e1*doc1
        Dw2=lr*e2*doc1
        print("Dw0: ", Dw0)
        print("Dw1: ", Dw1)
        print("Dw2: ", Dw2)
        w0n=Dw0+w0
        w1n=Dw1+w1
        w2n=Dw2+w2
        #print("w0: ", w0n)
        #print("w1: ", w1n)
        #print("w2: ", w2n)

        doc2=s2*(1-s2)*df
        Dwoc2=lr*e0*doc2
        Dw3=Dwoc2
        Dw4=lr*e1*doc2
        Dw5=lr*e2*doc2
        print("Dw3: ", Dw0)
        print("Dw4: ", Dw1)
        print("Dw5: ", Dw2)
        print("\n")
        w3n=Dw3+w3
        w4n=Dw4+w4
        w5n=Dw5+w5
        #print("w3: ", w3n)
        #print("w4: ", w4n)
        #print("w5: ", w5n)

        doc3=s3*(1-s3)*df
        Dwoc3=lr*e0*doc3
        Dw6=Dwoc2
        Dw7=lr*e1*doc3
        Dw8=lr*e2*doc3
        #print("Dw6: ", Dw6)
        #print("Dw7: ", Dw7)
        #print("Dw8: ", Dw8)
        w6n=Dw6+w6
        w7n=Dw7+w7
        w8n=Dw8+w8
        #print("w6: ", w6n)
        #print("w7: ", w7n)
        #print("w8: ", w8n)
        print("NUEVOS PESOS:")
        print("--------------")
        print("w9: ", w9n)
        print("w10: ", w10n)
        print("w11: ", w11n)
        print("w12: ", w12n)
        print("w0: ", w0n)
        print("w1: ", w1n)
        print("w2: ", w2n)
        print("w3: ", w3n)
        print("w4: ", w4n)
        print("w5: ", w5n)
        print("w6: ", w6n)
        print("w7: ", w7n)
        print("w8: ", w8n)
        print("--------------")"""

def mathide(no, entradas, wpeso, outs):
    for n in range(no):
        x=xmath(entradas, wpeso)
        sr=srmath(x)
        outs.append(sr)

def xmath(entradas, wpeso):
    x=0
    for ins in entradas:
        x+=ins*wpeso[0]
    return x

def srmath(x):
    sr=1/(1+math.exp(-x))
    return sr

def Emath(sd, sr):
    E=sd-sr
    return E

def dmath(sr, E):
    df=sr*(1-sr)*E
    return df

def main():
    #defino listas, variables
    e1 = [0, 0, 1, 1]
    e2 = [0, 1, 0, 1]
    sd = [0, 1, 1, 0]
    vias=1
    lr=0.1
    es1 = []
    es2 = []
    es3 = []
    es4 = []
    pesos=[[], [], [], [], [], [], [], [], [], [], [], [], []]

    #defino el bucle para poder iterar
    for var in range (4):
        #pesos definidos en clase
        pesosiniciales = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6]
        no=3
        iter=0

        while True:
            entradas=[vias, e1[var], e2[var]]
            outs=[]
            dwf=[]
            d=[]
            dwoc=[]
            mathide(no, entradas, pesosiniciales, outs)
            entradas=[vias]
            for varios in outs:
                entradas.append(varios)
            x=xmath(entradas, pesosiniciales)
            sr=srmath(x)
            E=Emath(sd[varios], sr)
            if varios==0:
                es1.append(E)
            elif varios==1:
                es2.append(E)
            elif varios==2:
                es3.append(E)
            elif varios==3:
                es3.append(E)
            df=dmath(sr, E)
            for ins in entradas:
                dw=lr*ins*df
                dwf.append(dw)
            for sr in outs:
                dwoc.append(sr*(1-sr)*E)
            entradas=[vias, e1[var], e2[var]]
            for doc in dwoc:
                for ins in entradas:
                    d.append(lr*ins*doc)
            for varios in dwf:
                d.append(varios)
            for i, delta in enumerate(d):
                if len(pesos[i])<10000:
                    pesos[i].append(pesosiniciales[i])
                pesosiniciales[i]=pesosiniciales[i]+d
            iter+=1
            if iter==10000:
                break
        print(f"e1={e1[var]}\n")
        print(f"e2={e2[var]}\n")
        print(f"sd={sd[var]}\n")
        print(f"Iteraciones: {iter}\n")
        print(f"Salida real: {sr}\n")
        print(f"Error: {E}")
    
    print(len(pesos[0]))

    iteraciones=[]
    for i in range(10000):
        iteraciones.append(i)
    
    while True:
        plt.figure(figsize=(15,5))
        plt.subplot(1, 2, 1)
        plt.xlabel("Iteraciones")
        plt.ylabel("Errores")
        plt.title("GRÁFICO DE ERRORES")
        plt.axhline(y=0, color='green', linestyle='.')
        plt.plot(iteraciones, es1)
        plt.plot(iteraciones, es2)
        plt.plot(iteraciones, es3)
        plt.plot(iteraciones, es4)
        plt.subplot(1, 2, 2)
        plt.xlabel("Iteraciones")
        plt.ylabel("Pesos")
        plt.title("GRÁFICO DE PESOS")
        plt.axhline(y=0, color='green', linestyle='.')
        for varios in pesos:
            plt.plot(iteraciones, varios)
        plt.show()

if __name__ == '__main__':
    main()








