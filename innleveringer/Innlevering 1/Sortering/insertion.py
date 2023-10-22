# Insertion sort prosedure 
def sort(A):
    # lokke som itererer gjennom hele lista starter fra 2-elemntet
    for i in range(1, len(A)):
        j = i
        # naar (j-1)-te element er storre enn j-te element i lista vi skal gjore swap og gaar til forrige elementet
        while j > 0 and A[j-1] > A[j]:
            A.swap(j-1,j)
            j = j-1
    return A