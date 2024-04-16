class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pas=[[1],[1,1]] 
        if rowIndex>1:
            for i in range(rowIndex-1):
                curr=[1]   
                last=pas[-1] 
                for i in range(len(last)-1):
                    curr.append(last[i]+last[i+1])
                curr.append(1)
                pas.append(curr)
        return pas[rowIndex]



        
        