def searchRange(nums, target):
    def findBound(first):
        l, r = 0, len(nums) - 1
        pos = -1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                pos = m
                if first:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return pos

    start = findBound(True)
    if start == -1:
        return [-1, -1]
        
    end = findBound(False)
    return [start, end]