#Given a string s, the task is to arrange the string according to the frequency of each character, in ascending order. If two elements have the same frequency, then they are sorted in lexicographical order.
class Solution:
    def frequencySort(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        # sort based on (frequency, character)
        chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        res = ""
        for ch, count in chars:
            res += ch * count
        
        return res
