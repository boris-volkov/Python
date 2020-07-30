class thing(object):
    def __init__(self, one, two):
        self.a = one
        self.b = two
    def __eq__(self, other):
        return self.a == other.a

# with this eq method, only the 'a'
# element has to match for objects
# to be considered equal by == and 'in'

class other_thing(object):
    def __init__(self, one, two, three):
        self.a = one
        self.b = two
        self.c = three

class thing_list(object):
    def __init__(self):
        self.list = []
    def insert(self, thing):
        self.list.append(thing)
    def __iter__(self):
        return iter(self.list)

# different objects that have
# same first element
thing1 = thing(1,2)
thing2 = thing(1,3)
thing3 = other_thing(1,2,3)

things = thing_list()
things.insert(thing1)

# all these will return true, try it!
print(thing2 in things)
print(thing3 in things)
print(thing1 == thing3)
print(thing1 == thing2)
print(thing3 == thing1)
