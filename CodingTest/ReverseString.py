def Reverse(s):
	if len(s)==0:
		return s
	else:
		return Reverse(s[1:])+s[0]

s='hello'
print(Reverse(s))
