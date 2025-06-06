class Queue:
    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._qList)
    
    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop(0)