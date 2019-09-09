# Critical Section
# Code segment that accesses a shared resource such as a data structure in memory or external resource
# Should not be executed by more than one thread or a process at a time.

# MUTEX (Lock)
# Mechanism to implement mutual exclusion
# Only one thread or process can possess at a time so it can be used to prevent multiple threads from simultaneously accessing a shared resource.
# Limits access to critical section

# ATOMIC OPERATIONS
# The operation to acquire the lock is an atomic operation which means it is always executed as a single, indivisible action.
# To the rest of the system atomic operation appears to happen instantaneously.
# Cannot be interrupted by other concurrent threads.
