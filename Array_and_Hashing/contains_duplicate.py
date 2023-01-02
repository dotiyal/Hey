class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Leet Code
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
      
        """
        # my_code
        hash_set = set(nums)
        if len(nums) > len(hash_set):
            return True
        else:
            return False
        """
        
