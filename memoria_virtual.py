class MemoriaVirtual:
    def __init__(self):
        self.memoria = {
            'global': {
                'int' : [],
                'float' : [],
                'bool' : [],
                'string' : [],
                'temp': {
                    'int' : [],
                    'float' : [],
                    'bool' : [],
                    'string' : [],
                },
            },
            'constantes': {
                'int' : [],
                'float' : [],
                'bool' : [],
                'string' : [],
            },
            'local': [],
        }
        self.vars = {
            'global': {
                'int' : [0, 15, 1000],
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
        
    def crearMemoriaLocal(self):
        newMem = {                
            'int' : [],
            'float' : [],
            'bool' : [],
            'string' : [],
            'temp': {
                'int' : [],
                'float' : [],
                'bool' : [],
                'string' : [],
            },
        }
        self.memoria['local'].append(newMem)
        return newMem
    
    def borrarMemoriaLocal(self):
        self.memoria['local'].pop()
    
    def encontrarScope(self, dirVar):
        for x in self.vars:
            for i in self.vars[x]:
                dirs = self.vars[x][i]
                if(dirs[1]<=dirVar and dirVar<=dirs[2]):
                    return x, i, dirs[1]
    
    def insertarValor(self, valor, dirVar):
        scope, varType, dirInicial = self.encontrarScope(dirVar)
       # print(scope, varType, dirInicial, dirVar, dirVar-dirInicial, valor)
       # self.memoria[scope][varType][dirVar] = valor
    
    def crearMemoriaGlobal(self, resource_count):
        for i in resource_count:
           # print(i, resource_count[i])
            if i != 'temp':
                self.memoria['global'][i] = [None] * resource_count[i]
            else:
                for j in resource_count[i]:
                    self.memoria['global'][i][j] = [None] * resource_count[i][j]
        print(self.memoria['global'])
    
    def crearMemoriaConst(self, resource_count):
        for i in resource_count:
           self.memoria['constantes'][i] = [None] * resource_count[i]
        print(self.memoria['constantes'])
    
    def crearMemoriaFunc(self, resource_count):
        self.crearMemoriaLocal()
        for i in resource_count:
           # print(i, resource_count[i])
            if i != 'temp':
                self.memoria['local'][-1][i] = [None] * resource_count[i]
            else:
                for j in resource_count[i]:
                    self.memoria['local'][-1][i][j] = [None] * resource_count[i][j]
        print(self.memoria['local'])



    