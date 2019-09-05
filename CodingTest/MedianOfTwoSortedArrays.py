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
	if n+m/2 == 0:
		pass
	
	if nums1[int(n/2)] > nums2[int(m/2)]:
		return findMedianSortedArrays(
			nums1[:int(n/2)+1],nums2[int(m/2)+1:])
	else:
		return findMedianSortedArrays(
			nums1[int(n/2)+1:],nums2[:int(m/2)+1])



findMedianSortedArrays(
	[1,4,7,9,22,24],
	[2,3,5,8,10]
	)
