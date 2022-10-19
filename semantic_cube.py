class SemanticCube:
    def __init__(self):

        self.cube = {
            'int': {
                'int': {
                    '+':'int',
                    '-':'int',
                    '*':'int',
                    '/':'int',
                    '%':'int',
                    '^':'int',
                    '=':'int',
                    '<':'bool',
                    '>':'bool',
                    '!!':'bool',
                    '&&':'bool',
                    '!=':'bool',
                    '==':'bool',
                },
               'float': {
                    '+':'float',
                    '-':'float',
                    '*':'float',
                    '/':'float',
                    '%':'float',
                    '^':'float',
                    '<':'bool',
                    '>':'bool',
                    '!!':'bool',
                    '&&':'bool',
                    '!=':'bool',
                    '==':'bool',
                },
                'bool': {
                    '!!':'bool',
                    '&&':'bool',                    
                },
            },
            'float': {
                'int': {
                    '+':'float',
                    '-':'float',
                    '*':'float',
                    '/':'float',
                    '%':'float',
                    '^':'float',
                    '<':'bool',
                    '>':'bool',
                    '!!':'bool',
                    '&&':'bool',
                    '!=':'bool',
                    '==':'bool',
                },
               'float': {
                    '+':'float',
                    '-':'float',
                    '*':'float',
                    '/':'float',
                    '%':'float',
                    '^':'float',
                    '=':'float',
                    '<':'bool',
                    '>':'bool',
                    '!!':'bool',
                    '&&':'bool',
                    '!=':'bool',
                    '==':'bool',
                },
                'bool': {
                    '!!':'bool',
                    '&&':'bool',                    
                },
            },
            'bool': {
                'int': {
                    '!!':'bool',
                    '&&':'bool',
                },
               'float': {
                    '!!':'bool',
                    '&&':'bool',
                },
                'bool': {
                    '=':'bool',
                    '!!':'bool',
                    '&&':'bool',
                    '!=':'bool',
                    '==':'bool',                   
                },
            },
            'string':{
                'string': {
                   '=':'string', 
                },
                'bool': {
                    '!!':'bool',
                    '&&':'bool',                    
                },
            },
            '#': {
                '#': {
                    'end':'bool'
                }
            }
        }

    def is_match(self, left, right, op):
        try: 
            return self.cube[left][right][op]
        except:
            return None