Given a package with a weight limit limit
and a list weights of item weights

implement a function get_indices_of_item_weights that finds two items
whose sum of weights equals the weight limit limit.

Your function will return a tuple of integers
where each element represents the item weights of the two packages

The higher valued index should be placed in the zeroth index 
and the smaller index should be placed in the first index.

Your solution should run in linear time.

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    return None






























class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}
        
        # for i in range(len(nums)):
        #     if (target - nums[i]) in cache:
        #         # What do we put in the brackets?
        #         key = target - nums[i]
        #         index1 = cache[key]
        #         index2 = i
        #         return [index1, index2]
        #         # return array of indices
        #     else:
        #         cache[nums[i]] = i
        #         # cache → { 2: 0, 7: 1, 11: 2 }
        
        for i in range(len(nums)):
            cache[nums[i]] = i
            
        for i in range(len(nums)):
            if (target - nums[i]) in cache and cache[target - nums[i]] != i:
                # What do we put in the brackets?
                key = target - nums[i]
                index1 = cache[key]
                index2 = i
                return [index1, index2]