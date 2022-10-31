"""
- 문제
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

- 예시
1. 
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

2.
Input: n = 1
Output: ["()"]

** 그림설명
https://www.notion.so/slkiminfo/74080184543c49df975b005e8c4df73a

***
dp 문제로 되어 있으나, 실제 풀이는 dfs 방식 이용
***
"""


class Solution(object):
    def generateParenthesis(self, n):
        self.answer = []
        self.generate('', n, n)
        return self.answer

    def generate(self, prefix, left, right):
        if left:
            self.generate(prefix+"(", left-1, right)
        if left < right:
            self.generate(prefix+")", left, right-1)
        if right == 0:
            self.answer.append(prefix)



solution = Solution()
print(solution.generateParenthesis(n=3))