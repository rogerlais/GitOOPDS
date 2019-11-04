
class ProofQueue(object):

    def __init__(self):
        self.data = []
        return

    @property
    def size(self):
        return len(self.data)

    def pop(self):
        return self.data.pop()

    def push(self, value):
        return self.data.append(value)
