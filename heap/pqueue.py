from queue import PriorityQueue
from collections import deque

class PriorityAccumulator:
    """
    Hold a numeric variable and add queued values to it according to priority.
    By default lower numeric priority runs first. Set highest_first=True to
    treat larger numbers as higher priority.
    """
    def __init__(self, initial=0, highest_first=False):
        self._pq = PriorityQueue()
        self._value = initial
        self._highest_first = highest_first
        self._counter = 0  # tie-breaker to preserve insertion order

    def add(self, val, priority=0):
        """
        Queue a numeric val to be added to the accumulator.
        priority: smaller numbers run first unless highest_first=True.
        """
        key = -priority if self._highest_first else priority
        # tuple (priority_key, counter, value) ensures stable ordering
        self._pq.put((key, self._counter, val))
        self._counter += 1

    def apply_next(self):
        """Pop the next item by priority and add it to the internal value. Return new value."""
        if self._pq.empty():
            raise IndexError("no queued values")
        _, _, val = self._pq.get()
        self._value += val
        return self._value

    def apply_all(self):
        """Apply all queued additions in priority order. Return final value."""
        while not self._pq.empty():
            _, _, val = self._pq.get()
            self._value += val
        return self._value

    @property
    def value(self):
        """Current accumulated value (without applying queued items)."""
        return self._value

    def clear_queue(self):
        """Remove all queued items without applying them."""
        while not self._pq.empty():
            self._pq.get()