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
            self.assign
        ]
    
    def quadArtimetic(self, op, value1, value2):
        if(op<len(self.opFunc)):
            operation = self.opFunc[op]
            return operation(value1, value2)
    
    def addition(self, value1, value2):
        print(value1,'+',value2)
        if not value1 or not value2:
            raise ValueError("Addition invalid, both operators should have values")
        return value1 + value2

    def substraction(self, value1, value2):
        print(value1,'-',value2)
        if not value1 or not value2:
            raise ValueError("Substraction invalid, both operators should have values")
        return value1 - value2
    
    def multiplication(self, value1, value2):
        print(value1,'*',value2)
        if not value1 or not value2:
            raise ValueError("Multiplication invalid, both operators should have values")
        return value1 * value2
    
    def division(self, value1, value2):
        print(value1,'/',value2)
        if not value1 or not value2:
            raise ValueError("Division invalid, both operators should have values")
        return value1 / value2
    
    def assign(self, value1, value2):
        return value1
        




    