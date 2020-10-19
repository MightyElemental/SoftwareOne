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


# ---- Exercise 2 ----
'''
Write in pseudo code a function merge(listA: List, listB: List) that returns a
sorted list containing the elements of both list where listA and listB are two sorted lists
of integers. If an element exists in both lists, it must appear multiple times in the returned list.
For example:
>>> merge([1,3,4,7],[2,3,5])
[1,2,3,3,4,5,7]
'''

# Just want to comment that I hate pseudocode with a passion, and see no use for it.
# Especially when the syntax is more complex than any (not every) programming language.

'''
Function merge(listA: List, listB: List): List
    result := Array[0..(listA.length+listB.length)] of int
    aindex = 0 : int
    bindex = 0 : int
    while aindex < listA.length || bindex < listB.length do
        if bindex >= listB.length then
            result[aindex+bindex] = listA[aindex]
            aindex = aindex + 1
            continue
        endif
        if aindex >= listA.length then
            result[aindex+bindex] = listB[bindex]
            bindex = bindex + 1
            continue
        endif
        if listA[aindex] <= listB[bindex] then
            result[aindex+bindex] = listA[aindex]
            aindex = aindex + 1
        else
            result[aindex+bindex] = listB[bindex]
            bindex = bindex + 1
        endif
    endwhile
    return result
'''

def merge(listA: list, listB: list) -> list:
    result = []
    aindex = 0
    bindex = 0
    while(aindex < len(listA) or bindex < len(listB)):
        if bindex >= len(listB):
            result.append(listA[aindex])
            aindex = aindex + 1
            continue
        if aindex >= len(listA):
            result.append(listB[bindex])
            bindex = bindex + 1
            continue
        if listA[aindex] <= listB[bindex]:
            result.append(listA[aindex])
            aindex = aindex + 1
        else:
            result.append(listB[bindex])
            bindex = bindex + 1
    return result

print(merge([1,3,4,7],[2,3,5]))

# I am in pain due to the pseudocode


# ---- Exercise 3: reinventing the wheel! ----
'''
For this question we are emulating the method split() from the type str. Write the
algorithm for a function splitText(text:String, delimiters:String) which
returns the list of the words by splitting the string text at each delimiters. The delimiters
themselves are discarded. An example is given below:

>>> sampleText = "As Python's creator, I'd like to say a
few words about its origins."
>>> splitText(sampleText, ", '.")
['As', 'Python', 's', 'creator', 'I', 'd', 'like', 'to',
'say', 'a', 'few', 'words', 'about', 'its', 'origins']

You can assume that a string has a method contains(Character) that returns true if the
character is in the string, false otherwise. This exercise is more challenging than it may look
like.
'''