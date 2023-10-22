# Bubble sort prosedure 
def sort(A):
    # lokke som itererer gjennom hele lista stopper 2 elementer foyr siste elementet
    for i in range(len(A)):
        for j in range(len(A)-i-1):
        # naar (j-1)-te element er storre enn j-te element i lista vi skal gjore swap og gaar til forrige elementet
            if A[j] > A[j + 1]:
                A.swap(j+1,j)
    return A