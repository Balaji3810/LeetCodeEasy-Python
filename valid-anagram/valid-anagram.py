class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(s) != len(t):
        #    return False
        #countS, countT = {}, {}
        #
        #for i in range(len(s)):
        #    countS[s[i]] = 1 + countS.get(s[i],0)
        #    countT[t[i]] = 1 + countT.get(t[i],0)
        #
        #for c in countS:
        #    if countS[c] != countT.get(c,0):
        #        return False
       # return True
        
        return sorted(s) == sorted(t)
    
         
       # def sortString(s):
       #     s2= list(s)
       #     for i in range(len(s2)):
       #         j = s2[i:].index(min(s2[i:])) + i
       #         s2[i] , s2[j] = s2[j], s2[i]
       #     return s2
       # #return(sortString(s),sortString(t))
       # if sortString(s) != sortString(t):
       #     return False
       # else:
       #     return True
        #print(sortString(s),sortString(t))
        #if sortString(s) != sortString(t):
        #    return False
        #else:
        #    return True
        #        
        