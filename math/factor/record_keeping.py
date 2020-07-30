class top_ten(object): # record keeping class
    def __init__(self):
        self.list = [record('------', 99999) for _ in range(10)]

    def insert(self, entry):
        if entry < self.list[-1]:
            for i, record in enumerate(self.list):
                if entry < record:
                    self.list[i:i] = [entry]
                    break
    
    def needed(self, entry): # check if a new score belongs on the list
        return entry < self.list[-1].time

    def __str__(self):
        return '\n'.join([f'{str(i+1):>2}' + ' ' + str(record) for i, record in enumerate(self.list[:10])])

class record(object): # basically a dressed up ordered pair with cmp methods
    def __init__(self, name, time): # I should have probably used collections.namedtuple
        self.name = name.upper()
        self.time = time
    
    def __lt__(self, other):
        return self.time < other.time # but i also thought these methods would be convenient

    def __le__(self, other):
        return self.time <= other.time

    def __gt__(self, other):
        return self.time > other.time
    
    def __ge__(self, other):
        return self.time >= other.time
    
    def __eq__(self, other):
        return self.time == other.time
    
    def __ne__(self, other):
        return self.time != other.time

    def __str__(self):
        return (f'{str(self.name):10}' + '   :   ' + f'{self.time:.2f}' + 'sec.')

