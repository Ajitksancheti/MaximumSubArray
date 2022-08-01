def maxSubArray(self, nums):
    a = nums[0]
    b = nums[0]
    start=0
    end=0
    for i in range(1,len(nums)):
        #a = max(nums[i], a + nums[i])
        if(nums[i]>=a+nums[i]):
            a=nums[i]
            if(a>=b):
                start=i
        else:
            a=a+nums[i]
        if(a>=b):
            end=i
            b=a     
        #b = max(b, a)
    indicies=[start, end]
    return b,indicies
        
