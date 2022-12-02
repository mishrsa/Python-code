'''
Dictionary is a key value pair structure 
add an entry dict['key'] = 'value'-> Key value pair added into dictionary 
'Key' in Dictionary - Boolian- Test in Dict
remove entry ->del(grades['Key'])
dict.keys()- Keys values 
dict.values()- values 

Key must be unique

'''

my_dict = {}
grade = {'Anjan': 'A', 'Rajju': 'B', 'Manu': 'c', 'Deepu':'d'}
grade['Anjan']

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for k in aDict.values():
        result += len(k)
    return result