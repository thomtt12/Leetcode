# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


#### Brute Force 
'''
def containsDuplicate(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

'''


#### Sorting

'''
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums [i+1]:
            return True
    return False
'''

##### Counter Function
'''

from collections import Counter

def containsDuplicate(nums):
    freq = Counter(nums) # create a dictionary (key, value) = (phan tu cua nums, so lan xuat hien cua phan tu do)
    for nums, freq in freq.items(): # .items() tra ve cac phan tu trong dictionary, tuple la (key, value) 
        if freq > 1:
            return True
    return False
'''

#### Hashmap 
'''
def containsDuplicate(nums):
    counter ={}
    for num in nums:
        if num not in counter:
            counter[num]=0
        counter[num] +=1
    for num, freq in counter.items():
        if freq > 1:
            return True
    return False
'''

#### Set
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
#set: moi gia tri la duy nhat va khong the co cac phan tu trung lap

if __name__ == "__main__":
    # nums = [1,2,3,1]
    nums = [1,2,3,4]
    result = containsDuplicate(nums)
    print(result)

