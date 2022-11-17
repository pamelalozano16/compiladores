from pprint import pprint

class MemoriaVirtual:
    def __init__(self):   
        self.dp={}

        self.memoria = {
            'global': {
                'int' : [],
                'float' : [],
                'bool' : [],
                'string' : [],
            },
            'const': {
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
    
    def printCurrent(self):
        pprint(self.memoria)
        
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
            'nombre': None,
        }
        self.memoria['local'].append(newMem)
        return newMem
    
    def borrarMemoriaLocal(self):
        self.memoria['local'].pop()

    def encontrarDir(self, scope, varType, indx):
        return self.vars[scope][varType][1]+indx
    
    def currentFuncName(self):
        return self.memoria['local'][-1]['nombre']
    
    def encontrarScope(self, dirVar):
        if dirVar in self.dp:
            return self.dp[dirVar]
        for x in self.vars:
            isTemp = False
            if x == 'temp':
                isTemp = True
            for i in self.vars[x]:
                dirs = self.vars[x][i]
                if(dirs[1]<=dirVar and dirVar<=dirs[2]):
                    self.dp[dirVar] = (x, i, dirs[1], isTemp)
                    return x, i, dirs[1], isTemp
    
    def insertarValor(self, valor, dirVar):
        scope, varType, dirInicial, isTemp = self.encontrarScope(dirVar)
        dir = dirVar-dirInicial
      #  print(f'INSERT [{scope}][{varType}][{dir}]', valor)
        if isTemp:
            self.memoria['local'][-1]['temp'][varType][dir] = valor
        elif scope == 'local':
            self.memoria[scope][-1][varType][dir] = valor
        else:
            self.memoria[scope][varType][dir] = valor
        #print('RESULT')
        #pprint(self.memoria)
    
    def obtenerValor(self, dirVar):
        if not dirVar:
            return None
        scope, varType, dirInicial, isTemp = self.encontrarScope(dirVar)
        dir = dirVar-dirInicial
       # print('obt', scope, varType, dirInicial, dir)
        if scope == 'temp':
            return self.memoria['local'][-1][scope][varType][dir]
        if scope == 'local':
                return self.memoria[scope][-1][varType][dir]
        else:
               return self.memoria[scope][varType][dir]
    
    def crearMemoriaGlobal(self, resource_count):
        for i in resource_count:
           # print(i, resource_count[i])
            if i != 'temp':
                self.memoria['global'][i] = [None] * (resource_count[i]+1)

    def crearMemoriaConst(self, memoria):
        resource_count = memoria['resource_count']
        for i in resource_count:
           self.memoria['const'][i] = [None] * (resource_count[i]+1)
        for ind, value in enumerate(memoria['vars_dir']):
            self.insertarValor(memoria['vars_table'][ind], value)
    
    def crearMemoriaFunc(self, resource_count, nombre):
        self.crearMemoriaLocal()
        self.memoria['local'][-1]['nombre'] = nombre
        for i in resource_count:
           # print(i, resource_count[i])
            if i != 'temp':
                self.memoria['local'][-1][i] = [None] * resource_count[i]
            else:
                for j in resource_count[i]:
                    self.memoria['local'][-1][i][j] = [None] * (resource_count[i][j] + 1)



    