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

def print_depth(data):
    for key, value in data.items():
        index = 1
        if type(value) is dict:
            yield(key, value, index)
            index = index + 1
            yield from print_depth(value)       
        else:
            yield(key, value, index)
            index += 1
            


#print(print_depth(a))


for key, value, index in print_depth(a):
    print(key, value, index)
    





#output

"""

key1 1
key2 1
key3 2
key4 2
key5 3

"""
