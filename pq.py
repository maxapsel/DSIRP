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
      >>> insert(3, pq)
      >>> print(pq.data)
      [3, 7]
      >>> insert(5, pq)
      >>> insert(6, pq)
      >>> print(pq.data)
      [3, 6, 5, 7]
    """
    pq.data.append(val)
    i = len(pq.data) - 1
    while i > 0:
        parent = (i - 1) // 2
        if pq.data[parent] <= pq.data[i]:
            break
        pq.data[parent], pq.data[i] = pq.data[i], pq.data[parent]
        i = parent

def priority(val):
    """
      >>> priority(7) == 7
      True
    """
    return val
        
    
def min(pq):
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> min(pq)
      7
    """
    return pq.data[0]


def dm(pq):
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