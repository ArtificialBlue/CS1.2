from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    #Note: "[LinkedList()] * size" creates a single LinkedList in-memory, and simply multiplies the same LinkedList.
    #Meaning Operations you do on one, you do on all.
    return [LinkedList() for i in range(size)]

  def hash_func(self, key):
    result = hash(key) % self.size
    return result

  def insert(self, key, value):
    pass

  def print_key_values(self):
    pass
    

  