class Solution:
    def summaryRanges(self, nums):
        self.l = []
        if len(nums) == 0:
            return self.l
        a = nums[0]
        for i in range(len(nums)):
            if i+1 != len(nums):
                if nums[i]+1 == nums[i+1]:
                    continue
                else:
                    b = nums[i]
                    if a == b:
                        self.l.append(str(a))
                        a = nums[i+1]
                    else:
                        self.l.append(str(a)+'->'+str(b))
                        a = nums[i+1]
            else:
                b = nums[i]
                if a == b:
                    self.l.append(str(a))
                else:
                    self.l.append(str(a)+'->'+str(b))
        return self.l