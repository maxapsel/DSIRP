class PQ:
    """
    >>> pq = new()
    >>> pq.size()
      0
    """
    def __init__(self):
        self.data = []

    def __eq__(self, other):
        return self.data == other.data

    def size(self):
        return len(self.data)

def new():
#returns a priority queue
    """
      >>> pq = new()
      >>> isinstance(pq, PQ)
      True
    """
    return PQ()


def insert(val, pq):
    """
      >>> pq = new()
      >>> pq.size()
      0
      >>> insert(7, pq)
      >>> pq.size()
      1
    """
    pq.data.append(val)

def priority(val):
    """
    """
        
    
def min(pq):
#v
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> min(pq)
      7
    """
    return pq.data[0]


def dm(pq):
#new()
    """
      >>> original = new()
      >>> pq = new()
      >>> pq == original
      True
      >>> insert(7, pq)
      >>> pq == original
      False
      >>> dm(pq)
      >>> pq == original
      True
    """
    pq.data.remove(pq.data[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()