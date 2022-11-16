from semantic_cube import SemanticCube
from directions_control import DirectionsControl

semantic_cube = SemanticCube()
directions_control = DirectionsControl()

class Quadruple:
    def __init__(self):
        operator = None
        left = None
        right = None
        res = None
    
    def createQuad(self, operator, right, left, typeRight, typeLeft, res):
        resType = semantic_cube.is_match(typeLeft, typeRight, operator)
        if resType:
            self.operator = directions_control.getOpCode(operator)
            self.right = right
            self.left = left
            self.res = res
            return self, resType
        else:
            raise ValueError('Types mismatch', typeLeft, typeRight, operator)
    
    def createPrint(self, res):
        self.operator="PRINT"
        self.left=None
        self.right=None
        self.res=res
        return self
    
    def createGoToV(self, temp):
        self.operator="gotoV"
        self.left=temp
        self.right=None
        self.res=None
        return self

    def createGoToF(self, temp):
        self.operator="gotoF"
        self.left=temp
        self.right=None
        self.res=None
        return self

    def createGoTo(self):
        self.operator="goto"
        self.left=None
        self.right=None
        self.res=None
        return self

    def createEra(self, func):
        self.operator="ERA"
        self.left=f'{func}'
        self.right=None
        self.res=None
        return self
    
    def createParam(self, op, num):
        self.operator="PARAMETER"
        self.left=op
        self.right=f'#{num}'
        self.res=None
        return self

    def createGoSub(self, func, initial_address):
        self.operator="GOSUB"
        self.left=f'{func}'
        self.right=f'{initial_address}'
        self.res=None
        return self
    
    def arrVer(self, s1, linf, lsup):
        self.operator="VER"
        self.left=s1 # Temp: Dir -> Dir: Arr[elem] -> Res(Temp): Arr[Elem]
        self.right=linf
        self.res=lsup
        return self

    def endFunc(self):
        self.operator="ENDPROC"
        self.left=None
        self.right=None
        self.res=None
        return self
    
    def addDestination(self, dest):
        self.res = dest
        return self
    
    def getQuad(self):
        return [self.operator, self.left, self.right, self.res]
        

    
    

