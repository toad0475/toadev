# 구현부
def GetLenOfLongestSubstr(in_string):
	if len(in_string) <= 1:
		return 1

	minM = 0
	longestLen = 0
	
	for i in range(len(in_string)-1):
		for j,c in enumerate(in_string[minM:i+1]):
			if c == in_string[i+1]:
				if len(in_string[minM:i+1]) > longestLen:
					longestLen = len(in_string[minM:i+1])
				minM += j+1
		if len(in_string[minM:i+1])+1 > longestLen:
			longestLen = len(in_string[minM:i+1])+1
			
	return longestLen

# 함수 호출
while True:
	string = input("문자열을 입력하세요:")
	print("중복된 문자가 없는 가장 긴 서브 문자개수:{}".format(GetLenOfLongestSubstr(string)))

