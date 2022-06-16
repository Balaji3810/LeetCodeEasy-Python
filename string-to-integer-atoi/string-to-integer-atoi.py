class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2147483648
        MAX_INT =  2147483647
        
        i = 0
        res = 0
        negative = 1
        
        #checking white space
        while i < len(s) and s[i] == " ":
           i += 1
        
        #checking negative
        if i < len(s) and s[i] == "-":
            i += 1
            negative = -1
        
        #checking positive
        elif i < len(s) and s[i] == "+":
            i += 1
        
        checker = set("0123456789")
        
        while i < len(s) and s[i] in checker:
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and int(s[i]) > 7):
                return MAX_INT if negative == 1 else MIN_INT
            res = res * 10 + int(s[i])
            i += 1
            
        return res * negative
          
         
        