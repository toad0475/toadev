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
	
	if n+m == 1:
		if n == 1:
			return nums1[0]
		else:
			return nums2[0]
			
	if n+m == 2:
		if n == 2:
			return (nums1[0]+nums1[1])/2
		elif n == 1:
			return (nums1[0]+nums2[0])/2
		else:
			return (nums2[0]+nums2[1])/2
	
	if nums1[n//2] > nums2[m//2]:
		return findMedianSortedArrays(
			nums1[:n//2],nums2[m//2:])
	else:
		return findMedianSortedArrays(
			nums1[n//2:],nums2[:m//2])


print(findMedianSortedArrays(
	[5,8,9,15],
	[2,5,6]
	))
	
