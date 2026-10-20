# Python: Multithreading vs. Multiprocessing vs. Asyncio. 
**Rules of thumb on which one to choose (if any).**

Every task can be roughly described as CPU-Bound, I/O-Bound, or a combination of both.

1. If mainly CPU-Bound, assuming CPython with GIL enabled, the only relevant option is Multiprocessing.
2. If mainly I/O-Bound, Multiprocessing will almost never be the go-to. (An exception being for example simpler fault isolation)

## How to choose between Multithreading and Asyncio in I/O-Bound tasks?

1. Being each thread adds space (because of the memory allocated for the thread) and time (because of the context switch between them) overhead, asyncio scales better.
2. Asyncio code is relatively harder to comprehend. On the other hand has more predictable task switching, as the scheduling of the switch between threads is controlled by the OS.
3. Asyncio code is less relevant when we need to heavily interact with sync libraries.