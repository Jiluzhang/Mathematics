# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Contraints: 0 <= digits.length <= 4   digits[i] is a digit in the range['2', '9']

# Runtime Beats 68.22%    Memory Beats 29.19%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #l = [chr(i) for i in range(97, 123)]
        n_l = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if len(digits)==0:
            return []
        elif len(digits)==1:
            return n_l[digits]
        elif len(digits)==2:
            return [i+j for j in n_l[digits[1]] for i in n_l[digits[0]]]
        elif len(digits)==3:
            return [i+j+k for k in n_l[digits[2]] for j in n_l[digits[1]] for i in n_l[digits[0]]]
        elif len(digits)==4:
            p_1 = [i+j for j in n_l[digits[1]] for i in n_l[digits[0]]]
            p_2 = [k+l for l in n_l[digits[3]] for k in n_l[digits[2]]]
            return [a+b for b in p_2 for a in p_1]


# Runtime Beats 57.11%   Memory Beats 99.10%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        if not digits:
            return []
        
        q = ['']
        for num in digits:
            n = int(num)
            for _ in range(len(q)):
                c = q.pop(0)
                for i in l[n]:
                    q.append(c+i)
        return q
