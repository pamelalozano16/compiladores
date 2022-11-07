from directions_control import DirectionsControl

directions_control = DirectionsControl()

class VariableControl:
    def __init__(self):
        self.current_scope = 'global'

        self.constants = {
            'vars_table': [],
            'vars_types': [],
            'vars_dir':[]            
        }

        self.args = {
            'global': []
        }

        self.variables_table = {
            'global':{
                'scope': '#', #Scope Anterior
                'return': 'void',
                'vars_table': [],
                'vars_types': [],
                'vars_dir':[],
                'initial_address':-1,
                'resource_count':{
                    'int':0,
                    'float':0,
                    'bool':0,
                    'string':0,
                    'temp':0
                }
            },  
        }

    def change_scope(self, scope):
        self.current_scope=scope

    def get_current_scope(self):
        return self.current_scope, self.variables_table[self.current_scope]['initial_address']
    
    def get_current_scope_return(self):
        return self.variables_table[self.current_scope]['return']

    def print_table(self):
        print('Func table:', self.variables_table)
        print('Args table:', self.args)
        print('Const table:', self.constants)
    
    def is_in_table(self, func_name):
        return func_name in self.variables_table

    def get_arg_type(self, num):
        args_expected = len(self.args[self.current_scope])
        if(args_expected <= num): #Compare number of args expected
            raise ValueError(f'Expected {args_expected} argument but got {num+1}')
        return self.args[self.current_scope][num]

    def find_dir_name(self, num):
        opCode = directions_control.getOpSign(num)
        if opCode: return opCode
        for scopes in self.variables_table:
            try:
                indx=self.variables_table[scopes]['vars_dir'].index(num)
                varName=self.variables_table[scopes]['vars_table'][indx]
                return varName
            except:
                continue
        try:
            indx=self.constants['vars_dir'].index(num)
            varName=self.constants['vars_table'][indx]
            return varName
        except:
            return None
    
    def find_vars_type(self, name):
        for scopes in self.variables_table:
            try:
                indx=self.variables_table[scopes]['vars_table'].index(name)
                varType=self.variables_table[scopes]['vars_types'][indx]
                return varType
            except:
                continue
        try:
            indx=self.constants['vars_table'].index(name)
            varType=self.constants['vars_types'][indx]
            return varType
        except:
            return None

    def find_vars_dir(self, name):
        for scopes in self.variables_table:
            try:
                indx=self.variables_table[scopes]['vars_table'].index(name)
                varDir=self.variables_table[scopes]['vars_dir'][indx]
                return varDir
            except:
                continue
        try:
            indx=self.constants['vars_table'].index(name)
            varDir=self.constants['vars_dir'][indx]
            return varDir
        except:
            return None

    def find_vars_scope(self, name):
        for scopes in self.variables_table:
            if name in self.variables_table[scopes]['vars_table']:
                return self.variables_table[scopes]['scope']

    def find_var(self, name):
        current_scope = self.current_scope
        while current_scope != '#': #Sube hasta global
            try:
                indx = self.variables_table[current_scope]['vars_table'].index(name)
                return current_scope, indx
            except:
                current_scope = self.variables_table[current_scope]['scope']
        try:
            indx=self.constants['vars_table'].index(name)
            return 'const', indx
        except:
            return None

    def add_func(self, name):
        self.variables_table[name]= {
            'return': None,
            'scope': self.current_scope,
            'vars_table':[],
            'vars_types': [],
            'vars_dir':[],
            'initial_address':-1,
            'resource_count':{
                'int':0,
                'float':0,
                'bool':0,
                'string':0,
                'temp':0
            }
        }
        self.args[name]=[]
        self.current_scope = name
       # print("Scope", self.current_scope)

    def add_return(self, return_type):
        self.variables_table[self.current_scope]['return'] = return_type
       # print("Scope", self.variables_table)
    
    def getDir(self, varType, varDir):
        return directions_control.getDirection(varDir, varType)
    
    def add_var(self, name, var_type):
        self.variables_table[self.current_scope]['vars_table'].append(name)
        self.variables_table[self.current_scope]['vars_types'].append(var_type)
        self.variables_table[self.current_scope]['vars_dir'].append(self.getDir(var_type, self.current_scope))
        self.variables_table[self.current_scope]['resource_count'][var_type]+=1
       # self.print_table()
    
    def scope_back(self):
        self.current_scope = self.variables_table[self.current_scope]['scope']
        directions_control.resetLocalDirections()
       # print("Scope", self.current_scope)
    
    def addConst(self, num, varType):
        if(num in self.constants['vars_table']):
            return self.constants['vars_dir']
        self.constants['vars_table'].append(num)
        self.constants['vars_dir'].append(self.getDir(varType, 'const'))
        self.constants['vars_types'].append(varType)

    def addTemp(self, temp, varType):
        self.variables_table[self.current_scope]['vars_table'].append(temp)
        varDir = self.getDir(varType, 'temp')
        self.variables_table[self.current_scope]['vars_dir'].append(varDir)
        self.variables_table[self.current_scope]['vars_types'].append(varType)
        self.variables_table[self.current_scope]['resource_count']['temp']+=1
        return varDir

    def addArgs(self):
        for i in self.variables_table[self.current_scope]['vars_types']:
            self.args[self.current_scope].append(i)
      #  print(self.current_scope, self.variables_table[self.current_scope])

    def addFuncInitialAddress(self, count):
        self.variables_table[self.current_scope]['initial_address'] = count

        


