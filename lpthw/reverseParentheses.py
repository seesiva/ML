"""
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.
"""

def reverseParentheses(s):
    start=s.find("(")
    end=s.find(")")
    old=s[start:end+1]
    new=s[start+1:end][::-1]
    return s.replace(old,new)