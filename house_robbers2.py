def rob(nums) -> int:
    if len(nums) <= 3:
        return max(nums)
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))    
    
def helper(nums):
    print(nums)
    
    if nums == []:
        return 0
    one, two = nums[-1], 0

    for i in range(len(nums) - 3, -1, -1):
        print("nums[i] one, two")
        print(nums[i], one, two)
        nums[i] += max(one, two)
        print(f"nums[i]: {nums[i]}")

        one, two = nums[i+1], one
    print(max(one, two))
    return max(nums[0], nums[1])

if __name__ == '__main__':
    # l = [0]
    # l = [2,7,9,3,1]
    l = [1,2,3,1]
    print(rob(l))