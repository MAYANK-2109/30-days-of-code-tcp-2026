def longestConsecutive(self, nums):
        numset=set(nums)
        maxlen=0
        for num in numset:
            if (num-1) not in numset:
                currnum= num
                currmax=1
                while (currnum+1) in numset:
                    currnum+=1
                    currmax+=1
                maxlen= max(maxlen, currmax)
        return maxlen