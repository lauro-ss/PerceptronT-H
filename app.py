class Perceptron:

    def __init__(self, taxa, limiar, w):
        self.taxa_aprendizado = taxa
        self.limiar = limiar
        self.w = w

    def Calcula(self, Input):
        x = [i for i in Input]
        aux = 0
        Output = 1*(self.limiar*-1)
        for x in x:
            Output = Output + (x*self.w[aux])
            aux = aux + 1
        return 1 if Output >= 0 else -1

    def attPesos(self, Input, d, y):
        for i in range(len(self.w) - 1):
            self.w[i] = self.w[i] + (self.taxa_aprendizado*(Input[i])*(d - y))
            if (i == 0):
                self.limiar = self.w[i]*1

    def Aprender(self, Input, Output):
        y = self.Calcula(Input)
        if y == Output:
            return 1
        else:
            self.attPesos(Input, Output, y)
            return 0


T = [1, 1, 1,
     0, 1, 0,
     0, 1, 0]

H = [1, 0, 1,
     1, 1, 1,
     1, 0, 1]

w = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, -0.1]

p = Perceptron(0.4, 0.5, w)

cont = 0
while (cont < 2):
    if (p.Aprender(T, 1) == 1):
        cont = cont + 1
    if (p.Aprender(H, -1) == 1):
        cont = cont + 1
print("Neurônio aprendeu")
print("------ TESTES ------")
print("Para T o resultado é: ", p.Calcula(T), sep="")
print("Para H o resultado é: ", p.Calcula(H), sep="")
print("------ TESTES DISTORCIDOS ------")
T = [1, 1, 1,
     0, 1, 0,
     0, 0, 0]

H = [0, 0, 1,
     1, 1, 1,
     1, 0, 0]
print("Para T DISTORCIDO o resultado é: ", p.Calcula(T), sep="")
print("Para H DISTORCIDO o resultado é: ", p.Calcula(H), sep="")
