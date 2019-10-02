class QueueP2(object):
    def __init__(self):
        self._queue = []
        return

    @property
    def queue(self):
        return self._queue

    @property
    def count(self):
        return len(self._queue)

    def insert_data(self, newValue):
        self._queue.append(newValue)

    def remove_data(self):
        return self._queue.pop(0)
