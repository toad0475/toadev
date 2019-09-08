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
	
