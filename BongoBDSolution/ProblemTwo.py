
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person("User","1","father")
person_b = Person("User","2",person_a)

a = {
    'key1': 1,
    'key2':{
        'key3':1,
        'key4':{
            'key5':4,
            "user":person_b
        }
    }
}

index = 1
def print_depth(data):
     for key, value in data.items():
        if type(value) is dict:
            yield(key, value, index)
            yield from print_depth(value)
        elif type(value) is object.__doc__:
            for key in person_b.items():
                yield(key, value, index)
                yield from print_depth(value)
        else:
            yield(key, value, index)

for key, value, index in print_depth(a):
    print(key,index)
    if type(value) is dict:
        index += 1

"""
Sample Output:
key1 1
key2 1
key3 2
key4 2
key5 3
user: 3
first_name: 4
last_name: 4
father: 4
first_name: 5
last_name: 5
father: 5

"""