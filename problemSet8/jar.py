class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if isinstance(n, int) and n >= 0:            
            total = self.size + n
            if total > self.capacity:
                raise ValueError('exceeds capacity')
            self.size = total
        else:
            raise ValueError('n must be a non negative integer')

    def withdraw(self, n):
        if isinstance(n, int) and n >= 0:         
            if n > self.size:
                raise ValueError('exceeds size')
            new_size = self.size - n
            self.size = new_size
        else:
            raise ValueError('n must be a non negative integer')

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        if isinstance(value, int) and value >= 0:
            self._capacity = value
        else:
            raise ValueError('Capacity must be a positive integer')

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, num):
        self._size = num


# jar = Jar()
# print(jar.size, jar)
# print('----')

# jar.deposit(1)
# print(jar.size, jar)
# print('----')

# jar.deposit(5)
# print(jar.size, jar)
# print('----')


# jar.withdraw(5)
# print(jar.size, jar)
# print('----')

# jar.deposit(1)
# print(jar.size, jar)
# print('----')

# jar.deposit(10)
# print(jar.size, jar)
# print('----')

