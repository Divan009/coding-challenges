import time

def longestPalindrome(s: str) -> str:
    result = ""
    lenResult = 0
    for i in range(len(s)-1):
        l, r = i, i
        print(f"l, r = {l,r}")
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            print(f"i: {i}, result={result}")
            
            if (r - l + 1) > lenResult:
                print(f"l: {l}, r: {r}")
                print(f"(r - l + 1) > lenResult: {(r - l + 1)}, {lenResult}")
                result = s[l:r+1]
                lenResult = r - l + 1
            l -= 1
            r += 1
        
    return result

if __name__ == '__main__':
    s = "ababd"
    print(longestPalindrome(s))