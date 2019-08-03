def reverse(s):
	revs=''
	for c in s:
		revs = c + revs
	return revs
	
s='hello'
print(reverse(s))
