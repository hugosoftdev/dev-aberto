from pandas.io.json import json_normalize

json =  [{'keyA': 1,
             'keyB': 2,
             'keyC': [{
                     'keyCA': 3,
                     'keyCB': {'keyCBA':4,
                               'keyCBB':5,
                               'keyCBC': [{'keyCBCA':6, 'keyCBCB':7, 'keyCBCC':8},
                                          {'keyCBCA':9, 'keyCBCB':10, 'keyCBCC':11},
                                          {'keyCBCA':12, 'keyCBCB':13, 'keyCBCC':14}],
                               'keyCBD':15},
                     'keyCC':16}],
            'keyD':17,
            'keyE': [{
                     'keyEA':18,
                     'keyEB': {'keyEBA':19,'keyEBB':20}
                     }]
            },{
            'keyA': 31,
            'keyB': 32,
            'keyC': [{
                    'keyCA': 33,
                    'keyCB': {'keyCBA': 34,
                              'keyCBB': 35,
                              'keyCBC': [{'keyCBCA': 36, 'keyCBCB': 37, 'keyCBCC': 38},
                                         {'keyCBCA': 39, 'keyCBCB': 40, 'keyCBCC': 41},
                                         {'keyCBCA': 42, 'keyCBCB': 43, 'keyCBCC': 44}],
                              'keyCBD': 45},
                    'keyCC': 46}],
            'keyD': 47,
            'keyE': [{
                    'keyEA': 48,
                    'Missing keyEB': 49
                    }]
            }]
                    
json_normalize(data = json, record_path = ['keyE', 'keyEB'], meta = ['keyA'])
