'''
주어진 string 에 모든 단어를 거꾸로 하시오.

Reverse all the words in the given string.

예제)
Input: “abc 123 apple”

Output: “cba 321 elppa”
'''

class ReverseWord:
	def __init__(self, in_str:str):
		self.in_str = in_str
		
	def ReverseWord(self) ->str:
		minMark = 0
		maxMark = 0
		for i in self.in_str:
			if self.in_str[i] == ' ':
				minMark = i	
		return self.in_str
				
	def ReverseStr(self,sepStr:str) ->str:
		for j in sepStr:			
			temp = sepStr[len(sepStr)-j]
			sepStr[len(sepStr)-j] = sepStr[j]
			sepStr[j] = temp
	
		return sepStr
		
		
		
inputStr = ReverseWord("abc 123 apple")
print(inputStr.ReverseWord())






		
		

