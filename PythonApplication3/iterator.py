class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index== 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]

rev= Reverse('spam')
iter(rev)
for char in rev:
    print(char)

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse('golf'):
    print(char)

