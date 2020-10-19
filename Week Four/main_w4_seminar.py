# WEEK 4 - SEMINAR 1

# ---- Exercise 1 ----
'''
You have given a sorted list of numbers with no duplicates, and you need to find the pairs of
numbers in that list whose sum is equal to the given target value.
Numbers can be either positive, negative, or both.
a) Test Case 1:
    Input: [1, 2, 4, 4], target = 8
    Output: [(4, 4)]
b) Test Case 2:
    Input: [1, 2, 4, 4], target = 8
    Output: [(4, 4)]
c) Test Case 3:
    Input: [-1, 1, 2, 4, 8], target = 7
    Output: [(-1, 8)]
d) Test Case 4:
    Input: [2, 4, 5, 7], target = 9
    Output: [(2,7), (5, 4)]
e) Test Case 5:
    Input: [2, 4, 5, 7], target = 8
    Output: []
Write an algorithm to find all such pairs given a list and a target. Note there are two approaches
to the problem, one called brute force where we try all possible combination of pairs and keep
the correct one (computationally expensive), one cleverer that is far more efficient.
'''

def find_pairs(num_pool: list, target: int) -> list:
    result = []
    for num in num_pool:
        val = target-num
        if(val in num_pool):
            if(val == num and num_pool.count(num) < 2): continue
            pair = (num,val)
            num_pool.remove(num)
            if(pair not in result): result.append(pair)
    return result

print(find_pairs([1, 2, 4, 4], 8)) # [(4, 4)]
print(find_pairs([-1, 1, 2, 4, 8], 7)) # [(-1, 8)]
print(find_pairs([2, 4, 5, 7], 9)) # [(2, 7), (5, 4)]
print(find_pairs([2, 4, 5, 7], 8)) # []
print(find_pairs([-3, -1, 2, 3, 5, 9, 11], 8)) # [(-3, 11), (3, 5), (9, -1)]