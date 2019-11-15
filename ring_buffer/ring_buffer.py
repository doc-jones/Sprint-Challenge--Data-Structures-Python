class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item # add an item in-place
    self.current = self.current + 1 # move the pointer

    if self.current >= self.capacity: # when met return to index 0 - oldest
      self.current = 0


  def get(self):
      return self.storage