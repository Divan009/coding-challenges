import time

def threeSum(nums):
    res = []
    nums.sort()

    print(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        print(f"i {i} l {l} r {r}")
        while l < r:
            print(f"nums[i] {nums[i]} nums[l] {nums[l]} nums[r] {nums[r]}")
            
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i],nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
            # time.sleep(5)
    return res


if __name__ == '__main__':
    s = [-3, 3, 4, -3, 1, 2]
    s = [-1,0,1,2,-1,-4]
    s = [-2, -2, 0, 0, 2, 2]
    print(threeSum(s))