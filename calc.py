class Calculator:
    def sum(self,a,b):
        return a+b
    def prod(self,a,b):
        return a*b
    def pow(self,a,b):
        if b == 1:
            return a
        return a*pow(a,b-1)