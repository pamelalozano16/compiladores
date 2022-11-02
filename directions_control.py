class DirectionsControl:
    def __init__(self):
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

        self.directions = {
            'global': {
                'int' : [0, 15, 1000], #Counter, First dir, Last dir
                'float' : [0, 1001, 2000],
                'bool' : [0, 2001, 3000],
                'string' : [0, 3001, 4000],
            },
            'local': {
                'int' : [0, 4001, 5000],
                'float' : [0, 5001, 6000],
                'bool' : [0, 6001, 7000],
                'string' : [0, 7001, 8000],
            },
            'const': {
                'int' : [0, 8001, 9000],
                'float' : [0, 9001, 10000],
                'bool' : [0, 10001, 11000],
                'string' : [0, 11001, 12000],
            },
            'temp': {
                'int' : [0, 12001, 13000],
                'float' : [0, 13001, 14000],
                'bool' : [0, 14001, 15000],
                'string' : [0, 15001, 16000],
            }
        }
    
    def getDirection(self, scope, varType):
        if scope not in self.directions: scope = 'local'
        if(self.directions[scope][varType][0] > self.directions[scope][varType][2]):
            raise ValueError("Direccion de memoria llena")
        nextDir = self.directions[scope][varType][0]+self.directions[scope][varType][1]
        self.directions[scope][varType][0] += 1
        return nextDir

    def getOpCode(self, op):
        opCode = self.operationCodes[op]
        return opCode
    
    def getOpSign(self, op):
        for i,x in self.operationCodes.items():
            if x==op: return i
