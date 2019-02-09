
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", "father")
person_b = Person("User", "2", person_a)


"""
// testing purpose print
 
print(person_b.__dict__.keys())
print(person_b.__dict__)
list = person_b.__dict__
print(person_b.__dict__.values())

"""

# dictionary initialized with variable a
a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            "user": person_b
        }
    }
}

depth = 1
for key, value in person_b.__dict__.items():
    if type(value) is type(person_a):
        for k,v in person_a.__dict__.items():
            print(k,v,depth)
            depth += 1
    else:
        print(key,value,depth)
        depth += 1

index = 1


def print_depth(data):
     for key, value in data.items():
        if type(value) is dict:
            yield(key, value, index)
            yield from print_depth(value)
        elif type(value) is type(person_b):
            yield (key, value, index)
            for key, value in person_b.__dict__.items():
                yield (key, value, index)
                if type(value) is type(person_a):
                    for key, value in person_a.__dict__.items():
                        yield (key, value, index)
            yield from print_depth(value)
        else:
            yield(key, value, index)


# or type(person_a) or type(person_b)

for key, value, index in print_depth(a):
    print(key,index)
    if type(value) is dict:
        index += 1
    elif type(value) is type(person_a):
        index += 1
    elif type(value) is type(person_b):
        index += 1
    else:
        index = index




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