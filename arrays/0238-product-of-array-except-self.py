class Solution(object):
    def productExceptSelf(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(arr) <= 1:
            return []

        left_product_arr = []
        temp_product = 1
        left_product_arr.append(temp_product)
        for i in range(1,len(arr)):
            temp_product *=  arr[i-1]
            left_product_arr.append(temp_product)
      
        right_product_arr = []
        temp_product = 1
        right_product_arr.append(temp_product)
        for i in range(len(arr)-1)[::-1]:
            temp_product *= arr[i+1]
            right_product_arr.insert(0,temp_product)

        result = []
        for i in range(len(arr)):
            result.append(left_product_arr[i]*right_product_arr[i])
        return result
        
