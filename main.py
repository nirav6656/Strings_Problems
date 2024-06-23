# ------------STRINGS-------------

# 1021. Remove Outermost Parentheses

# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         temp = ""
#         count = 0
#         sum = 0
#         n = len(s)
#         for i in range(n):
#             if s[i] == "(":
#                 sum += 1
#             elif s[i] == ")":
#                 sum -= 1
#             if sum == 0:
#                 new_string = s[count+1:i]
#                 count = i+1
#                 temp = temp + new_string
#         return temp

# Here is the another version of above code

# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         result = []
#         count = 0
#         sum = 0
#         n = len(s)
#         for i in range(n):
#             if s[i] == "(":
#                 sum += 1
#             elif s[i] == ")":
#                 sum -= 1
#             if sum == 0:
#                 result.append(s[count+1:i])
#                 count = i + 1
#         return "".join(result)

# 151. Reverse Words in a String


def reverseWords(s) -> str:
    s = s.split()
    temp = []
    n = len(s)
    for i in reversed(range(n)):
        temp.append(s[i])
        print(s[i])
    return " ".join(temp)
reverseWords("sky is blue")

