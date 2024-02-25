class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        palindrome=list(palindrome)
        if  palindrome[0]=="a":
            i=0
            while i<len(palindrome) and palindrome[i]=="a":
                i+=1
            if i>=len(palindrome):
                palindrome[-1]="b"
            elif i==len(palindrome)//2:
                if palindrome[i]=="a":
                    palindrome[-1]="a"
                else:
                    palindrome[-1]="b"
            else:
                palindrome[i]="a"
        else:
            palindrome[0]="a"
        return ''.join(palindrome)
    
        