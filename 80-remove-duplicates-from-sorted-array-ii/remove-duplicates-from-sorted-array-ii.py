class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        indx = 1
        rep = 1
        for i in range(1,len(n)):
            if n[i]==n[i-1]:
                rep+=1
            else: rep = 1
            if rep <=2:
                n[indx] = n[i]
                indx+=1
        return indx
        