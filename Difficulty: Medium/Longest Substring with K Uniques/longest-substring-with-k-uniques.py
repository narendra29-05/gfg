
from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        d=defaultdict(int)
        left=0
        max_length=-1
        for i in range (len(s)):
            d[s[i]]+=1
            while len(d)>k:
                d[s[left]]-=1
                if d[s[left]] == 0:
                    del d[s[left]]
                left+=1
            if len(d)==k:
                max_length=max(max_length,i-left+1)
                
        return max_length
        
        
            
        
        