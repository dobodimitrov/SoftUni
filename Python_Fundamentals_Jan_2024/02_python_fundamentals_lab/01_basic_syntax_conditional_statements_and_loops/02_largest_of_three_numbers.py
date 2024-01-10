import sys

largest_num = -sys.maxsize

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > largest_num:
    largest_num = num_1
if num_2 > largest_num:
    largest_num = num_2
if num_3 > largest_num:
    largest_num = num_3

print(largest_num)