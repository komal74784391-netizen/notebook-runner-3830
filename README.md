# Notebook Runner

Status: Released (v0.9.4). Schedules interactive notebooks on a pool of warm
kernels and enforces per-user resource quotas.

## Components

- `runner/scheduler.py` - queueing and fair-share scheduling.
- `runner/kernel_pool.py` - kernel lifecycle and reuse.
