from memoria_virtual import MemoriaVirtual
from quads_operations import QuadsOperations
import json
from pprint import pprint

ASSIGN = 5
END = 14
memoria_virtual = MemoriaVirtual()
quads_operations = QuadsOperations()
instruction_pointer = 0
quads = []

def printQuads():
    print("\nQuads:")
    for i, x in enumerate(quads):
        print(i, x)

# se lee el archivo ovejota, salida de compilacion
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
    quads = ovejota['quads']
   # print(ovejota['global'], ovejota['constants'])

printQuads()

if len(quads) > 10000:
    raise OverflowError('Stack overflow: too many calls')
if quads[0][0] == 'goto':
    instruction_pointer = quads[0][3]
while instruction_pointer < len(quads):
    quad = quads[instruction_pointer]
    print('\nCurrent: ', quad)
    if type(quad[0]) != str: #Is operation
        if quad[0] == ASSIGN:
            value1 = memoria_virtual.obtenerValor(quad[1])
            print('ASSIGN', value1, quad[3])
            memoria_virtual.insertarValor(value1, quad[3])
        elif quad[0] == END:
            print('END\n')
            memoria_virtual.printCurrent()
        else:
            value1 = memoria_virtual.obtenerValor(quad[1])
            value2 = memoria_virtual.obtenerValor(quad[2])
            print('OPERATION', value1, value2)
            value3 = quads_operations.quadArtimetic(quad[0], value1, value2)
            print('RES', value3)
            memoria_virtual.insertarValor(value3, quad[3])
    else:
        if quad[0] == 'PRINT':
            value1 = memoria_virtual.obtenerValor(quad[3])
            print('PRINT', value1)
    instruction_pointer+=1
