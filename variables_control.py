from directions_control import DirectionsControl

class VariableControl:
    def __init__(self):
        self.current_scope = 'global'
        self.directions_control = DirectionsControl()

        self.variables_table = {
            'global':{
                'scope': '#', #Scope Anterior
                'return': 'void',
                'vars_table': [],
                'vars_types': [],
                'vars_dir':[]
            },  
        }

    def change_scope(self, scope):
        self.current_scope=scope

    def print_table(self):
        print(self.variables_table)
    
    def is_in_table(self, func_name):
        return func_name in self.variables_table
    
    def find_vars_type(self, name):
        for scopes in self.variables_table:
            try:
                indx=self.variables_table[scopes]['vars_table'].index(name)
                varType=self.variables_table[scopes]['vars_types'][indx]
                return varType
            except:
                continue

    def find_vars_dir(self, name):
        for scopes in self.variables_table:
            try:
                indx=self.variables_table[scopes]['vars_table'].index(name)
                varType=self.variables_table[scopes]['vars_dir'][indx]
                return varType
            except:
                continue

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
        return None
    
    def add_func(self, name, return_type):
        self.variables_table[name]= {
            'return': return_type,
            'scope': self.current_scope,
            'vars_table':[],
            'vars_types': [],
            'vars_dir':[]
        }
        self.current_scope = name
       # print("Scope", self.current_scope)
    
    def getDir(self, varType, varDir):
        return self.directions_control.getDirection(varDir, varType)
    
    def add_var(self, name, var_type):
        self.variables_table[self.current_scope]['vars_table'].append(name)
        self.variables_table[self.current_scope]['vars_types'].append(var_type)
        self.variables_table[self.current_scope]['vars_dir'].append(self.getDir(var_type, self.current_scope))
       # self.print_table()
    
    def scope_back(self):
        self.current_scope = self.variables_table[self.current_scope]['scope']
       # print("Scope", self.current_scope)
    
    def addConst(self, num, varType):
        self.variables_table['global']['vars_table'].append(num)
        self.variables_table['global']['vars_dir'].append(self.getDir(varType, 'const'))
        self.variables_table['global']['vars_types'].append(varType)
    #    self.print_table()

        


