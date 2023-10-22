# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
 
 
def heapify(A, i, n):
    stoerste = i  # Initialize largest as root
    venstre = 2 * i + 1     # left = 2*i + 1
    hoyre = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if venstre < n and A[stoerste] < A[venstre]:
        stoerste, venstre = venstre, stoerste
 
    # See if right child of root exists and is
    # greater than root
    if hoyre < n and A[stoerste] < A[hoyre]:
        stoerste, hoyre = hoyre, stoerste
 
    # Change root, if needed
    if i != stoerste:
        A.swap(stoerste,i)  # swap
 
        # Heapify the root.
        heapify(A, stoerste, n)
 
# The main function to sort an array of given size
 
def BuildMaxHeap(A,n):
    # Build a maxheap.
    for i in range(n//2):
        heapify(A, i, n)
    return A

def sort(A):
    n = len(A)
    BuildMaxHeap(A,n)
    for i in range(n):
        A.swap(i,0)
        # A[i], A[0] = A[0], A[i]  # swap
        heapify(A, 0, i)

    return A
 