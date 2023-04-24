class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        num_dict = {}
        for i in range(len(nums)):
            if(nums[i] in num_dict):
                num_dict[nums[i]]+=1
            else:
                num_dict[nums[i]]=0
        print(num_dict)

        # for i in range(len(nums)):
        #     num_dict[nums[i]]+=1
        
        for i in range(len(nums)):
            if(num_dict[nums[i]]>=1):
                return nums[i]
            
		#use floyd's cycle detection