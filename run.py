import ply_sintax
import sys
import importlib

tests = ['aritmetic', 'while', 'for', 'functions', 'recursividad']
if 1<len(sys.argv):
    tests = [str(sys.argv[1])]

for i in tests:
    with open(f'test_{i}.pyst') as f:
        try:
            contents = f.read()
            result = ply_sintax.parser.parse(contents)
        except EOFError as e:
            print('Error:', e)