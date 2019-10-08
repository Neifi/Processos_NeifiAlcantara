import random

myList = []


for myList in range(100):
    myList = random.randint(1, 100)


class EquationSolver:

    def __init__(self, equation):

        self.equation = equation.split()
        self.operation1 = 0
        self.operation2 = 0
        self.result = 0
        # separar cada part
        self.z = self.equation[0]
        self.a = self.z[0]
        self.b = self.equation[4]
        self.x = self.z[1]
        self.operator = self.equation[1]
        self.c = self.equation[2]
        self.equal = self.equation[3]

        # cast to int
        self.A = float(self.a)
        self.B = float(self.b)
        self.C = float(self.c)

        print(self.A, self.B, self.C)
        # operate

    def resolver(self):
     if self.operator == "+":
      self.operation1 = float(self.B - self.C)
      pass
     elif self.operator == "-":
      self.operation1 = float(self.B + self.C)
      pass
     elif self.operator == "*":
      self.operation1 = float(self.C / self.B)
      pass
     else:
      self.operation1 = float(self.C * self.B)
      pass
     self.result = float(self.operation1 / self.A)
     return self.result



print (EquationSolver("2x + 3 = 7").resolver())

