class condicion:

    def _init_(self,num1=5,num2=4):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero

    def usoIf(self):
        # if ... elif ... else ...: periten condicionar la ejecucion de uno o varios bloques
        # de sentencias al cumplimiento de una o mas condiciones.
        if self.numero1 == self.numero2
            print("numero1={}=numero2={}: son iguales",format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3
            print("numero1 y numero3 son iguales")
        else
            print("numeros distintos")
        print("fin if")

#print("instancia de la clase")
#cond2= condicion()
#print(cond2.numero3)
#cond2.usoIf()
cond1= condicion(24,1)
cond1.usoIf()
print("gracias por si visita")
