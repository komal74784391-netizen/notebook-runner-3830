"""Fair-share scheduler for notebook execution."""

from collections import deque


class Scheduler:
    def __init__(self):
        self._queues = {}

    def submit(self, user, job):
        self._queues.setdefault(user, deque()).append(job)

    def next_job(self, rotation):
        for user in rotation:
            queue = self._queues.get(user)
            if queue:
                return user, queue.popleft()
        return None, None

    def pending(self, user):
        return len(self._queues.get(user, ()))
