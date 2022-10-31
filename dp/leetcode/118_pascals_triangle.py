"""
- 문제
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

- 예시
1.
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

2.
Input: numRows = 1
Output: [[1]]
"""


# 내 풀이
# class Solution(object):
#     def generate(self, numRows):
#         result = []
#         if numRows == 1:
#             return [[1]]
#         elif numRows == 2:
#             return [[1], [1,1]]
        
#         result = [[1], [1,1]]
        
#         for i in range(3, numRows+1):
#             tmp = [1]
#             for j in range(len(result[-1])-1):
#                 if j < len(result[-1])-1:
#                     tmp.append(result[-1][j]+result[-1][j+1])
#             tmp.append(1)
#             result.append(tmp)
        

#         return result


class Solution(object):
    def generate(self, numRows):
        ps = [[1]]

        for _ in range(numRows-1):
            tmp = [0] + ps[-1] + [0]
            row = []

            for j in range(len(ps[-1])+1):
                row.append(tmp[j]+tmp[j+1])
            
            ps.append(row)
        
        return ps



solution = Solution()
numRows = 5
print(solution.generate(numRows))