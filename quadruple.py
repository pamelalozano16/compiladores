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
    
    def createGoTo(self, isVariable, temp):
        self.operator="goto"
        if(isVariable==1):
            self.left=True
        if(isVariable==0):
            self.left=False
        self.right = temp
    
    def addDestination(self, quad, dest):
        quad.left = dest
    
    def getQuad(self):
        return [self.operator, self.left, self.right, self.res]
        

    
    

