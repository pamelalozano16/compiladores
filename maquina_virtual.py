from memoria_virtual import MemoriaVirtual
from quads_operations import QuadsOperations
import json
from pprint import pprint

ASSIGN = 5
END = 14
memoria_virtual = MemoriaVirtual()
quads_operations = QuadsOperations()

# Maquina Virtual:
# - Obtener datos de ovejota.json
# - Procesar Cuadruplos
# - Input/Output
class MaquinaVirtual:
    def __init__(self):
        self.quads=[]
        self.instruction_pointer = 0
        self.stored_pointers = []
        self.function_table = {}
        self.args_table = {}

    def printQuads(self):
        print("\nQuads:")
        for i, x in enumerate(self.quads):
            print(i, x)

    # se lee el archivo ovejota, salida de compilacion
    def run(self):
        with open('ovejota.json') as json_file:
            ovejota = json.load(json_file)
            # print('Memoria Global')
            # pprint(ovejota['global']['resource_count'])
            memoria_virtual.crearMemoriaGlobal(ovejota['global']['resource_count'])
            # print('\nMemoria Const')
            # pprint(ovejota['constants'])
            memoria_virtual.crearMemoriaConst(ovejota['constants'])
            # print('\nMemoria main')
            # pprint(ovejota['function_table']['main']['resource_count'])
            memoria_virtual.crearMemoriaFunc(ovejota['function_table']['main']['resource_count'], 'main')
            memoria_virtual.goSub()
            self.quads = ovejota['quads']
            self.function_table = ovejota['function_table']
            self.args_table = ovejota['args_table']
           # self.printQuads()

        self.runQuads()

    def runQuads(self):
        if len(self.quads) > 10000:
            raise OverflowError('Stack overflow: too many calls')
     #   if self.quads[0][0] == 'goto':
      #      self.instruction_pointer = self.quads[0][3]
        print('\n--------------------PYSTACHIO-----------------------------\n')
        while self.instruction_pointer < len(self.quads):
            quad = self.quads[self.instruction_pointer]
        #  print('\nCurrent: ', quad)
            if type(quad[0]) != str: #Is operation
                if quad[0] == ASSIGN:
                    ptrQuad = quad[3]
                    if '(' in str(quad[1]):
                        ptr = str(quad[1])
                        ptrQuad2=ptr[1:-1]
                        value1 = memoria_virtual.obtenerValor(int(ptrQuad2))
                        value2 = memoria_virtual.obtenerValor(value1)
                        value3 = quad[3]
                        if '(' in str(quad[3]):
                            ptr = str(quad[3])
                            ptrQuad=int(ptr[1:-1])
                            value3 = memoria_virtual.obtenerValor(ptrQuad)
                      #  print(ptrQuad)
                        memoria_virtual.insertarValor(value2, int(value3))
                    elif '(' in str(quad[3]):
                        ptr = str(quad[3])
                        ptrQuad=ptr[1:-1]
                        value1 = memoria_virtual.obtenerValor(int(quad[1]))
                        value2 = memoria_virtual.obtenerValor(int(ptrQuad))
                        memoria_virtual.insertarValor(value1, value2)
                    else:
                        value1 = memoria_virtual.obtenerValor(int(quad[1]))
                    #   print('ASSIGN', quad[1], value1, ptrQuad)
                        memoria_virtual.insertarValor(value1, ptrQuad)
                elif quad[0] == END:
                    print('\n-----------------------END--------------------------------\n')
                  #  memoria_virtual.printCurrent()
                else:
                 #   memoria_virtual.printCurrent()
                    ptrQuad1 = quad[1]
                    if '(' in str(quad[1]):
                        ptr = str(quad[1])
                        ptrDir=int(ptr[1:-1])
                        ptrQuad1 = memoria_virtual.obtenerValor(int(ptrDir))
                    value1 = memoria_virtual.obtenerValor(int(ptrQuad1))

                    ptrQuad2 = quad[2]
                    if '(' in str(quad[2]):
                        ptr = str(quad[2])
                        ptrDir=int(ptr[1:-1])
                        ptrQuad2 = memoria_virtual.obtenerValor(int(ptrDir))
                    value2 = memoria_virtual.obtenerValor(int(ptrQuad2))
                  #  print('OPERATION', value1, quad[1], value2)
                    value3 = quads_operations.quadArtimetic(quad[0], value1, value2)
                    ptrQuad = quad[3]
                #    print('RESULT', value3, quad[3])
                    if '(' in str(quad[3]):
                        ptr = str(quad[3])
                        ptrQuad=int(ptr[1:-1])
                    memoria_virtual.insertarValor(value3, ptrQuad)
            else: #Is command
                if quad[0] == 'goto':
                    self.instruction_pointer = quad[3]-1
                if quad[0] == 'gotoF':
                   value1 = memoria_virtual.obtenerValor(quad[1])
                   if value1 == False:
                        self.instruction_pointer = quad[3]-1
                       # print('QUAD',quad, value1, quad[3])
                if quad[0] == 'gotoT':
                   value1 = memoria_virtual.obtenerValor(int(quad[1]))
                   if value1 == True:
                        self.instruction_pointer = quad[3]-1
                if quad[0] == 'ERA':
                    resource_count = self.function_table[str(quad[1])]['resource_count']
                    memoria_virtual.crearMemoriaFunc(resource_count, str(quad[1]))
                if quad[0] == 'PARAMETER':
                    name = memoria_virtual.currentFuncName(True)
                  #  print('local', self.args_table, name, quad[2])
                    varDir = memoria_virtual.encontrarDir('local', self.args_table[name][quad[2]], quad[2])
                    value1 = memoria_virtual.obtenerValor(quad[1])
                   # print('PARAM', value1, varDir)
                    memoria_virtual.insertarValor(value1, varDir, True)
                  #  memoria_virtual.printCurrent()
                if quad[0] == 'GOSUB':
                    memoria_virtual.goSub()
                    name = memoria_virtual.currentFuncName()
                    initial_address = self.function_table[name]['initial_address']
                    self.stored_pointers.append(self.instruction_pointer)
                    self.instruction_pointer = initial_address-1
                   # print('GOSUB', name, initial_address)
                if quad[0] == 'RETURN':
                    name = memoria_virtual.currentFuncName()
                    self.instruction_pointer = self.function_table[name]['end_address']-1
                if quad[0] == 'ENDPROC':
                    memoria_virtual.borrarMemoriaLocal()
                    self.instruction_pointer = self.stored_pointers.pop()
                   # print('END PROC', self.instruction_pointer)
                if quad[0] == 'VER':
                    value1 = int(memoria_virtual.obtenerValor(quad[1]))
                    value2 = int(memoria_virtual.obtenerValor(quad[2]))-1
                    value3 = int(memoria_virtual.obtenerValor(quad[3]))
                    first = quads_operations.quadArtimetic(7, value2, value1)
                    second = quads_operations.quadArtimetic(7, value1, value3)
                    if not (first and second):
                        raise ValueError(f'Index out of range: {value1} in [{value2+1}, {value3}]')
                if quad[0] == 'PRINT':
                   # print(quad)
                    if '(' in str(quad[3]):
                        ptr = str(quad[3])
                        ptrQuad=ptr[1:-1]
                        ptrDir = memoria_virtual.obtenerValor(int(ptrQuad))
                        value1 = memoria_virtual.obtenerValor(int(ptrDir))
                       # print('PING', ptrQuad, ptrDir, value1)
                    else:
                        value1 = memoria_virtual.obtenerValor(int(quad[3]))
                    if r"\n" in str(value1):
                        print("\n")
                        value1=str(value1).replace(r"\n", '')
                    print(value1)
            self.instruction_pointer+=1


