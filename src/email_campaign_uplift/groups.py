
class GroupResult:
    def __init__(self, successes, size):
        self.successes = successes
        self.size = size

    @property
    def size(self):
        """the number of people in this variant"""
        return self._size
    
    @size.setter
    def size(self, value):
        """setter property to manage size attribute"""
        if value <= 0:
            raise ValueError("Size cannot be negative or zero. Set a size greater than 0")
        else: 
            self._size = value
    
    @property
    def rate(self):
        return self.successes / self.size

