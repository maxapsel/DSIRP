class PQ:
    """
    >>> pq = new()
    >>> pq.size()
      0
    """

def new():
#returns a priority queue
    """
      >>> pq = new()
      >>> isinstance(pq, PQ)
      True
    """


def insert():
    """
      >>> pq = new()
      >>> pq.size()
      0
      >>> insert(7, pq)
      >>> pq.size()
      1
    """

def priority():
    """
    """
        
    
def min():
#v
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> min(pq)
      7
    """


def dm():
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()