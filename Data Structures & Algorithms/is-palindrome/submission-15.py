class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        backward = []

        for c in s: 
            if (ord(c) >= 65 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57):
                forward.append(c.lower())
        
        for i in range(len(forward)-1, -1, -1):
            backward.append(forward[i])
        
        return forward == backward