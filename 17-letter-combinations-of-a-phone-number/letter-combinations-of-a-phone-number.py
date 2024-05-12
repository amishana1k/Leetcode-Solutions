class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        # s = ["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        # r = []
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if int(d[0])==i+1 and int(d[1])==j+1:
        #             d1 = s[i]
        #             d2 = s[j]
        #             for t in range(len(d1)):
        #                 for z in range(len(d2)):
        #                     res = ""
        #                     res = d1[t]+d2[z]
        #                     r.append(res)
        if not d:
            return []

        s = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]
        
        for digit in d:
            temp_result = []
            for char in s[int(digit)]:
                for combination in result:
                    temp_result.append(combination + char)
            result = temp_result
        
        return result

                        

        