from memoria_virtual import MemoriaVirtual
memoria_virtual = MemoriaVirtual()

class QuadsOperations:
    def __init__(self):
        self.quad=[]
        self.operationCodes = {
                    '+':1,
                    '-':2,
                    '*':3,
                    '/':4,
                    '=':5,
                    '>':6,
                    '<':7,
                    '!=':8,
                    '==':9,
                    '%':10,
                    '!!':11,
                    '&&':12,
                    '^':13,
                    'end':14
        }
        self.opFunc=[
            None,
            self.addition,
            self.substraction,
            self.multiplication,
            self.division,
            None,
            self.lessthan,
            self.greaterthan,
            self.notequal,
            self.equals,
            self.diff,
            self.or_,
            self.and_,
            self.exp
        ]
    
    def quadArtimetic(self, op, value1, value2):
        if(op<len(self.opFunc)):
            operation = self.opFunc[op]
            return operation(value1, value2)
    
    def addition(self, value1, value2):
     #   print(value1,'+',value2)
        if int(value1) is None or int(value2) is None:
            raise ValueError("Added operators should have values")
        return value1 + value2

    def substraction(self, value1, value2):
     #   print(value1,'-',value2)
        if int(value1) is None or int(value2) is None:
            raise ValueError("Substracted operators should have values")
        return value1 - value2
    
    def multiplication(self, value1, value2):
     #   print(value1,'*',value2)
        if int(value1) is None or int(value2) is None:
            raise ValueError("Multiplied operators should have values")
        return value1 * value2
    
    def division(self, value1, value2):
     #   print(value1,'/',value2)
        if int(value1) is None or int(value2) is None:
            raise ValueError("Divided operators should have values")
        return value1 / value2
    
    def diff(self, value1, value2):
        if int(value1) is None or int(value2) is None:
            raise ValueError("Compared operators should have values")
        return value1 % value2

    def exp(self, value1, value2):
        if int(value1) is None or int(value2) is None:
            raise ValueError("Exp operators should have values")
        return value1 ^ value2
        
    def lessthan(self, value1, value2):
        if int(value1) is None or int(value2) is None:
            raise ValueError("Compared operators should have values")
      #  print((value1,'>',value2),value1 > value2)
        return value1 > value2

    def greaterthan(self, value1, value2):
        if int(value1) is None or int(value2) is None:
            raise ValueError("Compared operators should have values")
        return value1 < value2

    def notequal(self, value1, value2):
        return value1 != value2

    def equals(self, value1, value2):
        return value1 == value2

    def or_(self, value1, value2):
        return (value1 or value2)

    def and_(self, value1, value2):
        return (value1 and value2)



    