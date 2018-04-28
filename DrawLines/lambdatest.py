# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# print(min(prices,key=lambda k:prices[k]))
#
# a = {
#     'x' : 1,
#     'y' : 2,
#     'z' : 3
# }
#
# b = {
#     'w' : 10,
#     'x' : 11,
#     'y' : 2
# }
#
# print(a.items()&b.items())
#
# ######    0123456789012345678901234567890123456789012345678901234567890'
# record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:37])
#
# print(record[slice(20,23)])
# print(cost)
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]
# from collections import Counter
# word_counts = Counter(words)
# # 出现频率最高的3个单词
# top_three = word_counts.most_common(3)
# print(top_three)
# # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

# nums=[2,3,4,5]
# print(sum(x*x for x in nums))

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
print(re.split("[;,\s]]\s*",line))

filename='table.txt'
print(filename.endswith('.txt'))