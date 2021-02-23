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
    index_list = self.arr[self.hash_func(key)]
    current = index_list.head
    if current == None:
      index_list.append((key,value))
    elif current.data[0] == key:
      current.data = (key, current.data[1] + value )
      current = current.next
    else:
      index_list.append((key,value))
  def print_key_values(self):
    for lst in self.arr:
      current = lst.head
      if current == None:
        pass
      else:
        for i in range(lst.length()):
           print(f'{current.data[0]}: {current.data[1]}')
           current = current.next
    

#------------Testing Section------------#
testHashTable = HashTable(10)

testHashTable.insert("Beet", 21)
testHashTable.insert("Beet", 21)
testHashTable.insert("Meet", 21)
testHashTable.insert("Yeet", 21)
testHashTable.insert("Leet", 21)
testHashTable.insert("Seet", 21)
testHashTable.insert("Veet", 21)

for lst in testHashTable.arr:
  lst.print_nodes()

  