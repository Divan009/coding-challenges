import time 

def trap(height) -> int:
    left, right = 0, len(height)-1
    maxLeft, maxRight = height[left], height[right]
    res = 0

    while left < right:
        # this decides to cal from left or right side
        if maxLeft <= maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            res += maxLeft - height[left+1]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            res += maxRight - height[right-1]        

    return res

if __name__ == '__main__':
    # s = [4,2,0,3,2,5]
    s = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(s))