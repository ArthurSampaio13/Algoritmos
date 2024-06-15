def f(n):
    if n == 0: # O(1)
        return 0 # O(1)
    if n == 1: # O(1)
        return 1 # O(1)
    if n > 1: # O(1)
        return f(n - 1) * n # O(n)
    
    # T(n) = O(n)