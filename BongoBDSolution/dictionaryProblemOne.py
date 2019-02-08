#The dictionary which is given is initalized in 'a'

a = {
    'key1': 1,
    'key2':{
        'key3':1,
        'key4':{
            'key5':4
        }
    }
}


print(a['key1'])
print(a['key2']['key3'])

"""
def print_depth(data):
    FirstLoopindex = 1
    for key, value in data.items():
        print(key, FirstLoopindex)
        

    #keyOne = a['key1']
    #print(keyOne)
"""


index = 1
def print_depth(data):
    for key, value in data.items():
        if type(value) is dict:
            yield(key, value, index)
            yield from print_depth(value)       
        else:
            yield(key, value, index)
            
            
#print(print_depth(a))


for key, value, index in print_depth(a):
    print(key,index)
    if type(value) is dict:
        index += 1
    





#output

"""

key1 1
key2 1
key3 2
key4 2
key5 3

"""
