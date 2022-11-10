from quadruple import Quadruple

quadruple = Quadruple()

class Semantics:
    def __init__(self, variables_control):
        self.variables_control = variables_control
        self.pTypes= []
        self.pilaO = []
        self.pOper = []
        self.quads = [quadruple.createGoTo().getQuad()] #initiate with goto Main
        self.pSaltos = []
        self.resultMatch = [] #Append a type check before expression is finished
        self.tempCounter = 0
        self.k_arguments = 0 #Number of processed arguments per function call
        self.calling_function = None #Current function call

    def printQuadsWithNames(self): 
        #Imprime quads con nombres en lugar de direcciones
        print("Quads:")
        quadStr = "["
        for i, x in enumerate(self.quads):
            for j in x:
                if type(j)!=str and type(x[0])!=int:
                    if(x[0]=='goto'):
                        quadStr+=f', {x[-1]}'
                        break
                    if(x[0]=='gotoF' or x[0]=='gotoV'):
                        quadStr+=f', {self.variables_control.find_dir_name(x[1])}, {x[-1]}'
                        break
                    else:
                        dirName =self.variables_control.find_dir_name(j)
                        if dirName : quadStr+=f', {dirName}'
                else:
                    dirName =self.variables_control.find_dir_name(j)
                    if dirName : 
                        quadStr+=f', {dirName}'
                    else:
                        quadStr+=f', {str(j)}'
            quadStr = quadStr[:1] + '' + quadStr[2 + 1:]
            quadStr+=']'
            print(i, quadStr)
            quadStr="["
    
    def printQuads(self):
        print("Quads:")
        for i, x in enumerate(self.quads):
            print(i, x)

    def endStatus(self):
        self.printQuadsWithNames()
     #   self.printQuads()
        self.variables_control.print_table()
        print("PilaO:", self.pilaO, "PTypes:", self.pTypes, "pOper:", self.pOper,"pSalos:", self.pSaltos)
    
    def getCounter(self):
        return len(self.quads)

    def insertId(self, id, idType):
        self.pTypes.append(idType)
        self.pilaO.append(id)
      #  print("Pilas:", self.pilaO, self.pTypes)

    def addOper(self, oper):
        self.pOper.append(oper)
     #   print(self.pOper)
    
    def addAssign(self):
        self.pOper.append("=")

    def addCounterToSaltos(self):
        #Add current counter (migaja)
        self.pSaltos.append(len(self.quads))

    def returnExpression(self):
        var_name, var_type = self.variables_control.addFuncReturn()
        self.insertId(var_name, var_type)
    
    def checkAssign(self):
        if 0<len(self.pOper) and (self.pOper[-1]=="="):
            right = self.variables_control.find_vars_dir(self.pilaO.pop())
            left = self.variables_control.find_vars_dir(self.pilaO.pop())
            right_type = self.pTypes.pop()
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), -1, left, self.pTypes.pop(), right_type, right)
            self.quads.append(quad.getQuad())


    def checkTerm(self):
        if 0<len(self.pOper) and (self.pOper[-1]=="+" or self.pOper[-1]=="-"):
            res = "t"+str(self.tempCounter)
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), self.variables_control.find_vars_dir(self.pilaO.pop()), self.variables_control.find_vars_dir(self.pilaO.pop()), self.pTypes.pop(), self.pTypes.pop(), res)
            dirTemp = self.variables_control.addTemp(res, typeRes)
            newQuad = quad.getQuad()
            newQuad[-1] = dirTemp
            self.quads.append(newQuad)
            self.pilaO.append(res)
            self.pTypes.append(typeRes)
            self.tempCounter+=1
     #   print("Res:'", self.quads, self.pilaO, self.pTypes)

    def checkFact(self):
        if 0<len(self.pOper) and (self.pOper[-1]=="*" or self.pOper[-1]=="/"):
            res = "t"+str(self.tempCounter)
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), self.variables_control.find_vars_dir(self.pilaO.pop()), self.variables_control.find_vars_dir(self.pilaO.pop()), self.pTypes.pop(), self.pTypes.pop(), res)
            dirTemp = self.variables_control.addTemp(res, typeRes)
            newQuad = quad.getQuad()
            newQuad[-1] = dirTemp
            self.quads.append(newQuad)
            self.pilaO.append(res)
            self.pTypes.append(typeRes)
            self.tempCounter+=1
     #   print("Res:", self.quads, self.pilaO, self.pTypes, self.pOper)

    def checkCompare(self):
        if 0<len(self.pOper) and (self.pOper[-1]=="&&" or self.pOper[-1]=="!!" or self.pOper[-1]==">" or self.pOper[-1]=="<" or self.pOper[-1]=="==" or self.pOper[-1]=="!="):
            res = "t"+str(self.tempCounter)
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), self.variables_control.find_vars_dir(self.pilaO.pop()), self.variables_control.find_vars_dir(self.pilaO.pop()), self.pTypes.pop(), self.pTypes.pop(), res)
            dirTemp = self.variables_control.addTemp(res, typeRes)
            newQuad = quad.getQuad()
            newQuad[-1] = dirTemp
            self.quads.append(newQuad)
            self.pilaO.append(res)
            self.pTypes.append(typeRes)
            self.tempCounter+=1
    
    def checkParen(self):
        #Fondo negro    
        if 0<len(self.pOper) and (self.pOper[-1]=="("):
            self.pOper.pop()

    def createGoTo(self):
        quadGoto = quadruple.createGoTo()
        self.quads.append(quadGoto.getQuad())
        self.pSaltos.append(len(self.quads)-1)

    def createGoToF(self):
        quadGoto = quadruple.createGoToF(self.variables_control.find_vars_dir(self.pilaO.pop()))
        if self.pTypes.pop() == 'bool':
            self.quads.append(quadGoto.getQuad())
            self.pSaltos.append(len(self.quads)-1)
        else: 
            raise ValueError("IF, WHILE and FOR blocks are conditional")

    def createGoToV(self):
        quadGoto = quadruple.createGoToV(self.variables_control.find_vars_dir(self.pilaO.pop()))
        if self.pTypes.pop() == 'bool':
            self.quads.append(quadGoto.getQuad())
            self.pSaltos.append(len(self.quads)-1)
        else: 
            raise ValueError("IF, WHILE and FOR blocks are conditional")
    
    def assignGoTo(self, plus=0):
        if 0<len(self.pSaltos):
            salto = self.pSaltos.pop()
            quad= self.quads[salto]
            quad[-1] = len(self.quads)+plus
            self.quads[salto] = quad

    def assignCrumb(self):
        #Add end of do while to goto
        if 0<len(self.pSaltos):
            salto = self.pSaltos.pop()
            migaja = self.pSaltos.pop()
            quad= self.quads[salto]
            quad[-1] = migaja
            self.quads[salto] = quad

    def assignEndLoop(self):
        if 0<len(self.pSaltos):
            salto = self.pSaltos.pop()
            falso = self.pSaltos.pop()
            retorno = self.pSaltos.pop()
            quad= self.quads[salto]
            quad[-1] = retorno
            self.quads[salto] = quad
            quad= self.quads[falso]
            quad[-1] = len(self.quads)
            self.quads[falso] = quad
    
    def resetCounter(self):
        self.tempCounter=0

    def resetArgumentCount(self):
        self.k_arguments=0

    def addFuncArguments(self):
        op = self.pilaO.pop()
        varType = self.pTypes.pop()
        expectedType = self.variables_control.get_arg_type(self.k_arguments, self.calling_function)
        if(varType == expectedType): #Compare expected arg types
            varDir = self.variables_control.find_vars_dir(op)
            quad = quadruple.createParam(varDir, self.k_arguments)
            self.quads.append(quad.getQuad())
        else:
            raise ValueError(f'Expected {op} of type {expectedType}')
        self.k_arguments += 1
    
    def addFuncEra(self, name): #Generate Space
        quad = quadruple.createEra(name)
        self.quads.append(quad.getQuad())
        self.calling_function=name
    
    def addFuncGoSub(self):
        initial_address = self.variables_control.getFuncInitialAddress(self.calling_function)
        quad = quadruple.createGoSub(self.calling_function, initial_address)
        self.quads.append(quad.getQuad())
        self.k_arguments = 0
  #      self.variables_control.change_scope(self.calling_function)

    def endFunc(self):
        #Append initial direction to goto main after function is done
        current_function, initial_address = self.variables_control.get_current_scope()
        if current_function == 'main':
            self.quads[0][-1] = initial_address
        else:
            quad = quadruple.endFunc()
            self.quads.append(quad.getQuad())
        self.calling_function = None
    
    def checkReturnValue(self):
        if (self.variables_control.find_vars_scope(self.calling_function) == '#'):
            var_type = self.variables_control.find_vars_type(self.calling_function)
            self.insertId(self.calling_function, var_type)
            res = "t"+str(self.tempCounter)
            dirTemp = self.variables_control.addTemp(res, var_type)
            self.tempCounter+=1
            self.insertId(res, var_type)
            self.addAssign()
            self.checkAssign()

    def endProgram(self):
        quad, typeRes = quadruple.createQuad("end", None, None, "#", "#", None)
        self.quads.append(quad.getQuad())