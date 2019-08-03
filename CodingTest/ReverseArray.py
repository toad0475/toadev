def Revstr(str_):
	for i in str_:
		temp = list[-(1)]
		list[-(i+1)]= list[i]
		list[i] = temp
	return list
	
a = input("입력배열:")
print(Revstr(a))
