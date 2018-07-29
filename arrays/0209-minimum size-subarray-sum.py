class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        l = len(nums)-1
        temp_sum = sum(nums[r:l+1])
        if temp_sum > s:
            flag = 0
            flag2 = 0
            while r < l:
                if nums[r] == nums[l]:
                    r1 = r
                    l1 = l
                    while nums[r] == nums[l]:
                        r1 = r1+1
                        l1 = l1-1
                        if nums[r] < nums[l]:
                            flag2 = 1
                            l1 = l1+1
                            break
                        else:
                            flag2 = 1
                            r1 = r1-1
                            break
                    if flag2 == 1:
                        r = r1
                        l = l1
                    else:
                        r = r+1                        
                temp_sum1 = sum(nums[r+1:l+1])
                temp_sum2 = sum(nums[r:l-1+1])
                print "---"
                print temp_sum1, temp_sum2
                if (temp_sum1 < s) or (temp_sum2 < s):
                    flag = 1
                    break
                if temp_sum1 > temp_sum2:
                    r = r+1
                else:                    
                    l = l-1
                print r,l
            if flag == 1:
                if l != r:
                    return l-r
                else:
                    return 1
            else:
                return -1
                
        else:
            return l+1





