'''
문자열 배열(string array)이 주어지면, 제일 긴 공통된 접두사(prefix)의 길이를 찾으시오.

Given an array of strings, find the longest common prefix of all strings.

예제)
Input: [“apple”, “apps”, “ape”]
Output: 2 // “ap”

Input: [“hawaii”, “happy”]
Output: 2 // “ha”

Input: [“dog”, “dogs”, “doge”]
Output: 3 // “dog”
'''

class GetLongestPrefix:
	def __init__(self, in_arr):
		self.in_arr = in_arr
	
	def sortArr(self):
		self.in_arr.sort()
		return self.in_arr
	
	def GetCommonPrefix(self, str1, str2):
		mark = 0
		for i,v in enumerate(str1):
			if str1[i] == str2[i]:
				mark +=1
			else:
				break
		return str1[0:mark]
	
	def longestCommonPrefix(self):
		if len(self.in_arr)<=1:
			return self.in_arr[0]
		sortedArr = self.sortArr()
		prefixArr = self.GetCommonPrefix(sortedArr[0],sortedArr[-1])
		return prefixArr
		
if __name__=="__main__":
	arr = ["dogs", "doggy", "dogs", "do"]
	a = GetLongestPrefix(arr)
	print(a.longestCommonPrefix())
	
