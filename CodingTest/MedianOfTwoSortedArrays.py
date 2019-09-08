'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

def findMedianSortedArrays(nums1, nums2):
	n = len(nums1)
	m = len(nums2)
	
	nums1_head = 0
	nums1_tail = n-1
	
	nums2_head = 0
	nums2_tail = m-1
	
	# get median in array
	if n%2:
		nums1_med = float(nums1[n//2])
	else:
		nums1_med = (nums1[n//2]+nums1[n//2-1])/2
	if m%2:
		nums2_med = float(nums2[m//2])
	else:
		nums2_med = (nums2[n//2]+nums2[n//2-1])/2
	
	if nums1_med == nums2_med:
		return nums1_med
	elif nums1_med > nums2_med:
		nums1_head = nums1_med
		return findMedianSortedArrays(
			nums1[:n//2],nums2[m//2:])
	else:
		return findMedianSortedArrays(
			nums1[n//2:],nums2[:m//2+1])
	

print(solution(
	[5,8,9,15],
	[2,5,6]
	))


# 두번째 솔루션

def fmsa(nums1, nums2):
    # 항상 두번재 배열 길이가 길거나 같도록 유지
    if len(nums1)>len(nums2):
        nums1, nums2 = nums2, nums1
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    
    # 둘 중 길이가 긴 배열의 머리와 꼬리
    head = 0
    tail = nums1_len

    # 1을 더하는 이유는 두 배열 길이의 합이 짝수던진 홀수던지 상관없이 중간 값을 나중에 int로 끊어주기 위한 장치
    mid = (nums1_len + nums2_len + 1) / 2

    i = 0
    j = 0

    while (head <= tail):
        i = int((head + tail) / 2)  # i = nums1 의 길이 / 2 
        j = int(mid - i)         # j = (두 개 합친 총 길이 / 2) - i
        
        if i < nums1_len and nums2[j-1] > nums1[i]:
            head = i + 1
        
        elif i > 0 and nums1[i-1] > nums2[j]:
            tail = i - 1
        else:
            maxleft = 0
            
            if i == 0:
                maxleft = nums2[j-1]
            elif j == 0:
                maxleft = nums1[i-1]
            else:
                maxleft = int(max(nums1[i-1], nums2[j-1]))

            if (nums1_len + nums2_len)%2:
                return maxleft
            
            minright = 0
            
            if i == nums1_len:
                minright = nums2[j]
            elif j == nums2_len:
                minright = nums1[i]
            else:
                minright = int(min(nums1[i], nums2[j]))
            
            return (maxleft + minright) / 2
    return -1


nums1 = [4,6]
nums2 = [5]
print(fmsa(nums1,nums2))

	
