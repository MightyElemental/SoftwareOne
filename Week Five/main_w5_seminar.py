# WEEK 5 - SEMINAR 2

# ---- Exercise 1 ----
'''
Given list A of n numbers, find the largest possible sum of a contiguous sub-list.

[ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

For example, for the list given above, the contiguous sub-list with the largest sum is
[4, -1, 2, 1], with sum 6 (in red).

--==Brute force approach==--
One obvious solution is to calculate the sum of every possible sub-list and the maximum of
those would be the solution. We can start from index 0 and calculate the sum of every possible
sub-list starting with the element A[0]. Then, we would calculate the sum of every possible
sub-list starting with A[1], A[2] and so on up to A[n-1], where n denotes the size of the list.
Note that every single element is a sub-list itself.
Using the pseudo code notation shown in Seminar 1, write the brute force algorithm to solve
the problem. Given a list of size n, how many comparisons are done?
'''

# Answer
# This is extremely inefficient method. I believe it has a time complexity classification of O(n^3)
'''
Function largestSubList(numbers:List): List
    bestSubList = empty List
    bestSubListTotal := -9999999 # should be the smallest possible integer
    for start := 0 to numbers.size() do
        for end := start to numbers.size() do
            subList = empty List
            subListTotal := 0
            for i := start to end do
                subList.append(numbers[end])
                subListTotal += numbers[end]
            endfor
            if(subListTotal > bestSubListTotal) then
                bestSubListTotal = subListTotal
                bestSubList = subList
            endif
        endfor
    endfor
    return bestSubList
'''

# Python version
def largest_sub_list(numbers: list)->list:
    bestSubList = []
    bestSubListTotal = -9999999 # Python integers are unbounded so there is no minimum
    for start in range(len(numbers)):
        for end in range(start,len(numbers)):
            sub_list = []
            sub_list_total = 0
            for i in range(start, end):
                sub_list.append(numbers[i])
                sub_list_total += numbers[i]
            if(sub_list_total>bestSubListTotal):
                bestSubListTotal = sub_list_total
                bestSubList = sub_list
    return bestSubList

print("---")
print(largest_sub_list([ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]))
# [4, -1, 2, 1]

'''
--==Could you think of a better approach?==--
This is quite difficult, and a better approach will be explained during the seminar session. But
it does not hurt to have a thought about it beforehand.
'''