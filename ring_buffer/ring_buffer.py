class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        
    old = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data.remove(self.data[self.old])
            self.data.insert(self.old, item)
            if self.old + 1 == 5:
                self.old = 0
            else:
                self.old += 1
        elif len(self.data) == 0:
            self.data.insert(0, item)
        else:
            self.data.append(item)

    def get(self):
        return self.data