class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        ln2 = len(nums2)
        for i in nums1:
            ind = nums2.index(i)
            # print(i, ind, nums2[ind])
            if ind < ln2-1:
                # print(ind < ln2-1)
                for j in range(ind + 1,ln2):
                    if nums2[j] > i:
                        l.append(nums2[j])
                        break
                else:
                    l.append(-1)
            else:
                l.append(-1)
            # print(l)
        return l