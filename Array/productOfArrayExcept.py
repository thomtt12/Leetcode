# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def productExceptSelf(nums):

    ans = [1]*len(nums) #khoi tao mot danh sach 'ans' co cung do dai voi 'nums'
    #construct left product array (from left to right)
    p = 1 
    for i in range(len(nums)):
        ans[i] *= p
        p *= nums[i]
    
    #times right product (from right to left)
    p =1 
    for i in reversed(range(len(nums))):
        ans[i] *= p
        p *=nums[i]
    return ans


if __name__ == "__main__":
    nums = [1,2,3,4]
    result = productExceptSelf(nums)
    print(result)
