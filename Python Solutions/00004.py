class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        len1, len2 = len(nums1), len(nums2)
        index1 = index2 = 0
        
        while index1 + index2 < len1 + len2:
            if index1 < len1 and index2 < len2:
                if nums1[index1] < nums2[index2]:
                    merged.append(nums1[index1])
                    index1 += 1
                else:
                    merged.append(nums2[index2])
                    index2 += 1
            elif index1 < len1:
                merged.append(nums1[index1])
                index1 += 1
            else:
                merged.append(nums2[index2])
                index2 += 1

        if len(merged) % 2 == 0:
            return (merged[(len(merged) - 1) // 2] + merged[len(merged) // 2]) / 2
        else:
            return merged[len(merged) // 2]