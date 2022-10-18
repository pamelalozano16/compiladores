from quadruple import Quadruple

quadruple = Quadruple()

class Semantics:
    def __init__(self):
        self.pTypes= []
        self.pilaO = []
        self.pOper = []
        self.quads = []
        self.tempCounter = 0
    
    def insertId(self, id, idType):
        self.pTypes.append(idType)
        self.pilaO.append(id)
        print(self.pilaO, self.pTypes)

    def addTerm(self, term):
        self.pOper.append(term)
        print(self.pOper)

    def addFact(self, factor):
        self.pOper.append(factor)
    
    def addAssign(self):
        self.pOper.append("=")
    
    def checkAssign(self):
        if 0<len(self.pOper) and (self.pOper[0]=="="):
            right = self.pilaO.pop()
            right_type = self.pTypes.pop()
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), -1, self.pilaO.pop(), self.pTypes.pop(), right_type, right)
            self.quads.append(quad.getQuad())
            print(self.quads, self.pilaO, self.pTypes)


    def checkTerm(self):
        if 0<len(self.pOper) and (self.pOper[0]=="+" or self.pOper[0]=="-" or self.pOper[0]=="="):
            res = "t"+str(self.tempCounter)
            quad, typeRes = quadruple.createQuad(self.pOper.pop(), self.pilaO.pop(), self.pilaO.pop(), self.pTypes.pop(), self.pTypes.pop(), res)
            self.quads.append(quad.getQuad())
            self.pilaO.append(res)
            self.pTypes.append(typeRes)
            self.tempCounter+=1
            print(self.quads, self.pilaO, self.pTypes)

    def checkFact(self):
        if 0<len(self.pOper) and (self.pOper[0]=="*" or self.pOper[0]=="/"):
            res = "t"+str(self.tempCounter)
            quad, typeRes = quadruple.createQuad(self.pOper[0], self.pilaO.pop(), self.pilaO.pop(), self.pTypes.pop(), self.pTypes.pop(), res)
            self.quads.append(quad.getQuad())
            self.pilaO.append(res)
            self.pTypes.append(typeRes)
            self.tempCounter+=1
    
    


