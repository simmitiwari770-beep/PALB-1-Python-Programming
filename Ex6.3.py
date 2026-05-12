#Given a string s consisting of balanced parentheses, calculate the score of the string based on the following rules:
class Solution:
    def scoreOfParentheses(self, s):
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    score += 1 << depth   # 2^depth
        
        return score
