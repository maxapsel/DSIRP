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
    
    


#done
def new():
    """
      >>> pq = new()
      >>> isinstance(pq, PQ)
      True
    """
    return PQ()

#done
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
      >>> insert(1, pq)
      >>> print(pq.data)
      [1, 3, 5, 7, 6]
    """
    if isinstance(val, list):
      for item in val:
        insert(item, pq)
    else:
      pq.data.append(val)
      i = len(pq.data) - 1
      while i > 0:
          parent = (i - 1) // 2
          if pq.data[parent] <= pq.data[i]:
              break
          pq.data[parent], pq.data[i] = pq.data[i], pq.data[parent]
          i = parent


#done
def priority(val):
    """
      >>> priority(7) == 7
      True
    """
    return val
        
#done
def min(pq):
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> min(pq)
      7
    """
    return pq.data[0]

#done
def dm(pq):
    """
      >>> original = new()
      >>> pq = new()
      >>> pq == original
      True
      >>> insert(7, pq)
      >>> insert(5, pq)
      >>> insert(3, pq)
      >>> insert(6, pq)
      >>> insert(1, pq)
      >>> print(pq.data)
      [1, 3, 5, 7, 6]
      >>> pq == original
      False
      >>> dm(pq)
      >>> print(pq.data)
      [3, 5, 7, 6]
      >>> is_heap(pq.data)
      True
      >>> dm(pq)
      >>> is_heap(pq.data)
      True
      >>> dm(pq)
      >>> is_heap(pq.data)
      True
    """
    if len(pq.data) == 0:
      return "Empty"
    
    pq.data.remove(pq.data[0])
    if len(pq.data) > 1:
      i = 0
      n = len(pq.data)
      while True:
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and pq.data[left] < pq.data[i]:
          smallest_child = left
        else:
          smallest_child = i
        if right < n and pq.data[right] < pq.data[smallest_child]:
          smallest_child = right
        if smallest_child == i and is_heap(pq.data):
          break
        elif smallest_child != i and not is_heap(pq.data):
          pq.data[i], pq.data[smallest_child] = pq.data[smallest_child], pq.data[i]
          i = smallest_child
        else:
          i +=1


def is_heap(heap):
  for i in range(1, len(heap)):
    parent = (i - 1) // 2
    if heap[parent] > heap[i]:
      return False
  return True

"""
if __name__ == "__main__":
  import doctest
  doctest.testmod()
"""

from binarytree import build
pq = new()
data = [4, 7, 2, 1, 5, 3, 9, 8]
insert(data, pq)
print("insert(data, pq)")
print(pq.data)
print(build(pq.data))
dm(pq)
print("dm(pq)")
print(pq.data)
print(build(pq.data))
dm(pq)
print("dm(pq)")
print(pq.data)
print(build(pq.data))
insert(0, pq)
print("insert(0, pq)")
print(pq.data)
print(build(pq.data))
insert([45, 32, 97, 21, 12, 33], pq)
print("insert([45, 32, 97, 21, 12, 33], pq)")
print(pq.data)
print(build(pq.data))
dm(pq)
print("dm(pq)")
print(pq.data)
print(build(pq.data))
