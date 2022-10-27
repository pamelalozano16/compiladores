from semantic_cube import SemanticCube

semantic_cube = SemanticCube()

class Quadruple:
    def __init__(self):
        operator = None
        left = None
        right = None
        res = None
    
    def createQuad(self, operator, right, left, typeRight, typeLeft, res):
        resType = semantic_cube.is_match(typeLeft, typeRight, operator)
        if resType:
            self.operator = operator
            self.right = right
            self.left = left
            self.res = res
            return self, resType
        else:
            raise ValueError('Types mismatch', typeLeft, typeRight, operator)
    
    def createGoToV(self, temp):
        self.operator="gotoV"
        self.left=temp
        self.right=-1
        self.res=None
        return self

    def createGoToF(self, temp):
        self.operator="gotoF"
        self.left=temp
        self.right=-1
        self.res=None
        return self

    def createGoTo(self):
        self.operator="goto"
        self.left=-1
        self.right=-1
        self.res=None
        return self
    
    def addDestination(self, dest):
        self.res = dest
        return self
    
    def getQuad(self):
        return [self.operator, self.left, self.right, self.res]
        

    
    

