from memoria_virtual import MemoriaVirtual
from quads_operations import QuadsOperations
import json
from pprint import pprint

ASSIGN = 5
END = 14
memoria_virtual = MemoriaVirtual()
quads_operations = QuadsOperations()


class MaquinaVirtual:
    def __init__(self):
        self.quads=[]
        self.instruction_pointer = 0

    def printQuads(self):
        print("\nQuads:")
        for i, x in enumerate(self.quads):
            print(i, x)

    # se lee el archivo ovejota, salida de compilacion
    def run(self):
        with open('ovejota.json') as json_file:
            ovejota = json.load(json_file)
            print('Memoria Global')
            pprint(ovejota['global']['resource_count'])
            memoria_virtual.crearMemoriaGlobal(ovejota['global']['resource_count'])
            print('\nMemoria Const')
            pprint(ovejota['constants'])
            memoria_virtual.crearMemoriaConst(ovejota['constants'])
            print('\nMemoria main')
            pprint(ovejota['function_table']['main']['resource_count'])
            memoria_virtual.crearMemoriaFunc(ovejota['function_table']['main']['resource_count'])
            self.quads = ovejota['quads']
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
                    value1 = memoria_virtual.obtenerValor(quad[1])
                 #   print('ASSIGN', quad[1], value1, quad[3])
                    memoria_virtual.insertarValor(value1, quad[3])
                elif quad[0] == END:
                    print('\n-----------------------END--------------------------------\n')
                  #  memoria_virtual.printCurrent()
                else:
                    value1 = memoria_virtual.obtenerValor(quad[1])
                    value2 = memoria_virtual.obtenerValor(quad[2])
               #     print('OPERATION', value1, value2)
                    value3 = quads_operations.quadArtimetic(quad[0], value1, value2)
                #    print('RESULT', value3, quad[3])
                    memoria_virtual.insertarValor(value3, quad[3])
            else: #Is command
                if quad[0] == 'goto':
                    self.instruction_pointer = quad[3]-1
                if quad[0] == 'gotoF':
                   value1 = memoria_virtual.obtenerValor(quad[1])
                   if value1 == False:
                        self.instruction_pointer = quad[3]-1
                       # print('QUAD',quad, value1, quad[3])
                if quad[0] == 'gotoT':
                   value1 = memoria_virtual.obtenerValor(quad[1])
                   if value1 == True:
                        self.instruction_pointer = quad[3]-1
                if quad[0] == 'PRINT':
                    value1 = memoria_virtual.obtenerValor(quad[3])
                    print('PRINT: ', value1)
            self.instruction_pointer+=1


