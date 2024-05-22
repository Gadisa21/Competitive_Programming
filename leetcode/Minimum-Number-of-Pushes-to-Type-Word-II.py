class Solution:
    def minimumPushes(self, word: str) -> int:
        press_letter=defaultdict(int)
        frequency=defaultdict(int)
        press=0
        word=list(word)
        for ch in word:
            frequency[ch]+=1
        word=sorted(word,key= lambda x:frequency[x],reverse=True)
        for ch in word:
            if len(press_letter)<8:
                if not press_letter[ch]:
                    press_letter[ch]=1
            elif len(press_letter)>=8 and len(press_letter)<16:
                if not press_letter[ch]:
                    press_letter[ch]=2
            elif len(press_letter)>=16 and len(press_letter)<24:
                if not press_letter[ch]:
                    press_letter[ch]=3
            else:
                if not press_letter[ch]:
                    press_letter[ch]=4
            press+=press_letter[ch]    

        return press    
        