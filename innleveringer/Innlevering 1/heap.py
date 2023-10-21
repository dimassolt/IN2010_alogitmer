def heapify(A, n, i):
    stoerste = i  
    venstre = 2 * i + 1     
    hoyre = 2 * i + 2     
 
    # See if left child of root exists and is
    # greater than root
    if venstre < n and A[i] < A[venstre]:
        stoerste = venstre
 
    # See if right child of root exists and is
    # greater than root
    if hoyre < n and A[stoerste] < A[hoyre]:
        stoerste = hoyre
 
    # Change root, if needed
    if stoerste != i:
        A.swap(stoerste,i) 
 
        # Heapify the root.
        heapify(A, n, stoerste)
 
def sort(A):
    n = len(A)
 
    # Build a maxheap.
    for i in range(n//2, -1, -1):
        heapify(A, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        A.swap(0,i)
        heapify(A, i, 0)
    return A
 