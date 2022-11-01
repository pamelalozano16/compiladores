from quadruple import Quadruple

quadruple = Quadruple()

class Semantics:
    def __init__(self, variables_control):
        self.variables_control = variables_control
        self.pTypes= []
        self.pilaO = []
        self.pOper = []
        self.quads = []
        self.pSaltos = []
        self.tempCounter = 0
    
    def printQuads(self):
        print("Quads:")
        for i, x in enumerate(self.quads):
            print(i, x)

    def endStatus(self):
        self.printQuads()
        print("PilaO:", self.pilaO, "pOper:", self.pOper,"pSalos:", self.pSaltos)

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
        self.pSaltos.append(len(self.quads))
    
    def checkAssign(self):
        if 0<len(self.pOper) and (self.pOper[-1]=="="):
            right = self.variables_control.find_vars_dir(self.pilaO.pop())
            left = self.variables_control.find_vars_dir(self.pilaO.pop())
            right_type = self.pTypes.pop()
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), -1, left, self.pTypes.pop(), right_type, right)
            self.quads.append(quad.getQuad())


    def checkTerm(self):
        if 0<len(self.pOper) and (self.pOper[-1]=="+" or self.pOper[-1]=="-" or self.pOper[-1]=="="):
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
        if 0<len(self.pOper) and (self.pOper[-1]=="("):
            self.pOper.pop()

    def createGoTo(self):
        quadGoto = quadruple.createGoTo()
        self.quads.append(quadGoto.getQuad())
        self.pSaltos.append(len(self.quads)-1)

    def createGoToF(self):
        quadGoto = quadruple.createGoToF(self.variables_control.find_vars_dir(self.pilaO.pop()))
        self.quads.append(quadGoto.getQuad())
        self.pSaltos.append(len(self.quads)-1)

    def createGoToV(self):
        quadGoto = quadruple.createGoToV(self.variables_control.find_vars_dir(self.pilaO.pop()))
        self.quads.append(quadGoto.getQuad())
        self.pSaltos.append(len(self.quads)-1)
    
    def assignGoTo(self, plus=0):
        if 0<len(self.pSaltos):
            salto = self.pSaltos.pop()
            quad= self.quads[salto]
            quad[-1] = len(self.quads)+plus
            self.quads[salto] = quad

    def assignCrumb(self):
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

    def endProgram(self):
        quad, typeRes = quadruple.createQuad("end", None, None, "#", "#", None)
        self.quads.append(quad.getQuad())