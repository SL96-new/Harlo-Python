def findMaxConsecutiveOnes(nums):
    count = max_count = 0
    for num in nums:
        if num == 1:
            # Increment the count of 1's by one.
            count += 1
        else:
            # Find the maximum till now.
            max_count = max(max_count, count)
            # Reset count of 1.
            count = 0
    return max(max_count, count)
print(findMaxConsecutiveOnes([0, 0]))