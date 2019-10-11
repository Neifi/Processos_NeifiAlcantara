class EquationSolver:
    A = 0
    B = 0
    C = 0
    a = 0
    b = 0
    c = 0
    operator = ""
    equal = ""
    def __init__(self, equation):

        self.equation = equation.split()
        self.operation1 = 0
        self.operation2 = 0
        self.result = 0

        print(self.equation)
        # separar cada part

    def assigment(self):
        try:
            self.b = self.equation[4]
            self.z = self.equation[0]
            self.a = float(self.z[0])
            #print (self.z[2])
            print (self.a)

            if(len(self.z) > 3):
                self.a = float(self.z[0]+self.z[1]+self.z[2])
                self.x = self.z[3]
            else:
                self.x = self.z[1]
            self.operator = self.equation[1]
            self.c = float(self.equation[2])
            self.equal = self.equation[3]
        except Exception:
            return "Valores no admitidos"

    def resolve(self):
        self.assigment()
        try:

            self.A = float(self.a)
            self.B = float(self.b)
            self.C = float(self.c)
            print (str(self.A), str(self.operator), str(self.B), str(self.equal), str(self.C))
        except ValueError:
            return "Valores no admitidos"

        if self.operator != "+" and self.operator != "-" and self.operator != "*" and self.operator != "/":
            return "Operador invalido"

        if self.equal != "=":
            return "Valores no admitidos"
        if self.x != "x":
            return "x no encontrada"

        # Operar
        if self.operator == "+":
            self.operation1 = float(self.B - self.C)

        elif self.operator == "-":
            self.operation1 = float(self.B + self.C)

        elif self.operator == "*":
            self.operation1 = float(self.C / self.B)

        elif self.operator == "/":
            self.operation1 = float(self.C * self.B)

        # Final step
        self.result = float(self.operation1 / self.A)
        return self.result


print(EquationSolver("2x / 3 = 7").resolve())
