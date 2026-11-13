"""Warm kernel pool used by the notebook runner."""

import time


class KernelPool:
    def __init__(self, size=8, idle_timeout=900):
        self.size = size
        self.idle_timeout = idle_timeout
        self._kernels = {}

    def acquire(self, user):
        kernel = self._kernels.get(user)
        if kernel is None:
            kernel = {"user": user, "started": time.time(), "busy": True}
            self._kernels[user] = kernel
        else:
            kernel["busy"] = True
        return kernel

    def release(self, user):
        kernel = self._kernels.get(user)
        if kernel:
            kernel["busy"] = False
            kernel["released_at"] = time.time()
