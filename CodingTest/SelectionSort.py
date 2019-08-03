#python3
#선택정렬 알고리즘 구현

def SelectionSort(A, n):
	for i in range(n-1):
		least = A[i]
		for j in range(i+1, n):
			if least>A[j]:
				least = A[j]
				A[i],A[j] = A[j],A[i]
	return A

A = [4, 7, 2, 6, 8]
print(SelectionSort(A,len(A)))
