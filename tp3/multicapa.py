from math import comb, e

def perceptron_multicapa(xor, comb):
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
    print("--------------")















if __name__ == '__main__':
    xor=['000', '011', '101', '110']
    perceptron_multicapa(xor, comb)