from memoria_virtual import MemoriaVirtual
import json

memoria_virtual = MemoriaVirtual()

# se lee el archivo ovejota, salida de compilacion
with open('ovejota.json') as json_file:
    ovejota = json.load(json_file)
    memoria_virtual.crearMemoriaGlobal(ovejota['global']['resource_count'])
    memoria_virtual.crearMemoriaConst(ovejota['constants']['resource_count'])
    memoria_virtual.crearMemoriaFunc(ovejota['function_table']['jeje']['resource_count'])
   # print(ovejota['global'], ovejota['constants'])

memoria_virtual.insertarValor(2, 8006)