# 개미수열(Ant Sequence) 문제

def antSeq(n):
	if n==1:
		return '1'
	else:
		return antSeq(n-1)

def getContNum(s):
	n = 1
	for i in range(len(s)-2):
		if s[i]==s[i+1]:
			n += 1
		else:
			str(n)
			n=1
			 
