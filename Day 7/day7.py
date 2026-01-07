def sumofencr(nums):
    total = 0
    for num in nums:
        digits = str(num)
        max_digit = max(digits)
        encrypted = int(max_digit * len(digits))
        total += encrypted

    return total

