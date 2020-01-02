class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = sorted(nums)
        ret = []
        for i in range(len(x)-2):
            for j in range(i+1, len(x)-1):
                for k in range(j+1, len(x)):
                    temp = []
                    if x[i]+x[j]+x[k] == 0:
                        temp.append(x[i])
                        temp.append(x[j])
                        temp.append(x[k])
                        if temp not in ret:
                            ret.append(temp)
        return ret
