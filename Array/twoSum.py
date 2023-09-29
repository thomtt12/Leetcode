# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import List

#### Brute force: sequentially & directly (space complexity = O(1), time = O(n2))
'''
def two_sum(nums, target) -> List[int]:
    # search first element in the array
    for i in range(len(nums)): 
        # search other element in the array
        for j in range(i+1, len(nums)): 
            # if these two elemets sum to pair_sum, print the pair
            if nums[i] + nums[j] == target:
                return [i,j]
    return []


if __name__== "__main__":
    nums = [3,2,4]
    target = 6
    result = two_sum(nums, target)
    print(result)
'''


#### Hashmap ( time complexity = O(n), Space complexity = O(n)  )
'''

def twoSumHashing(nums, target):
    hashmap = {} #initiate an empty dictionary
    for i in range(len(nums)): # go over every number in the array
        hashmap[nums[i]] = i #  key = nums[i], value = i  
    for i in range(len(nums)): 
        difference = target - nums[i]
        if difference in hashmap and hashmap[difference] != i:
            return [i, hashmap[difference]]
        
if __name__=="__main__":

    nums= [3,2,4]
    target = 6
    result= twoSumHashing(nums, target)
    print(result)
'''

####Hashmap (time complexity = O(n))
def twoSum (nums, target):
    hashmap ={}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap:
            return [i, hashmap[difference]]
        hashmap[nums[i]] = i # neu difference ko o trong hashmap thi them 1 cap (key,value) vao hashmap
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    result = twoSum(nums, target)
    print(result)
