# rekursjon mergesortering prosedure 
def sort(A):
    n = len(A)
    if n <= 1:
        return A
    # deler finner noyaktig indeks for midten i array 
    i = n//2
    # rekursjon del
    A1 = sort(A[:i])
    A2 = sort(A[i:])
    
    return merge(A1,A2,A)

# Prosedure merge analyserer hvor mange iterasjoner som gjores totalt
def merge(A1,A2, A):
    i = 0
    j = 0

    # naar i and j er mindre enn |A1| og |A2| skal vi sammenligne i-te og j-te elementer for
    # aa finne ut hvor lang har vi gaatt med iterering     
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            A[i+j] = A1[i]
            i = i + 1
        else:
            A[i+j] = A2[j]
            j = j + 1
    # naar i er mindre enn |A1| skal vi plasere i-te element  paa plass i + j  
    while i < len(A1):
        A[i+j] = A1[i]
        i = i + 1
    # naar j er mindre enn |A2| skal vi plasere j-te element paa plass i + j
    while j < len(A2):
        A[i+j] = A2[j]
        j = j + 1

    return A
    