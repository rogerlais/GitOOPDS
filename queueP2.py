class QueueP2(object):
    def __init__(self):
        self.data = []

    def get_queue(self):
        return self.data

    def insert_data(self, newValue):
        self.data.append(newValue)

    def remove_data(self):
        return self.data.pop(0)
