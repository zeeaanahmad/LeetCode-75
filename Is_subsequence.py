class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=='' and t=='':
            return True
        second_pointer = 0
        temp_str = ''
        
        for i in range(len(t)):
            if len(s)>0 and s[second_pointer]== t[i]:
                print("if working")
                temp_str+=t[i]
                second_pointer+=1
            if len(s)==len(temp_str):
                return True
        return False
                
            
            
        