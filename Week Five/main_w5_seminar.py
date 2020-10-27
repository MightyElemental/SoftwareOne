import random
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
# This is extremely inefficient method. I believe it has a time complexity classification of O(n^2)
'''
Function largestSubList(numbers:List): List
    bestSubList = empty List
    bestSubListTotal := -9999999 # should be the smallest possible integer
    for start := 0 to numbers.size() do
        subList = empty List
        subListTotal := 0
        for end := start to numbers.size() do
            subList.append(numbers[end])
            subListTotal += numbers[end]
            if(subListTotal > bestSubListTotal) then
                bestSubListTotal = subListTotal
                bestSubList = subList.copy() # to ensure the result does not change unless desired
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
        sub_list = []
        sub_list_total = 0
        for end in range(start,len(numbers)):
            sub_list.append(numbers[end])
            sub_list_total += numbers[end]
            if(sub_list_total>bestSubListTotal):
                bestSubListTotal = sub_list_total
                bestSubList = sub_list.copy()
    return bestSubList

# This does n*(n-1)/2 comparisons

print("---")
print(largest_sub_list([ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]))
# [4, -1, 2, 1]

'''
--==Could you think of a better approach?==--
This is quite difficult, and a better approach will be explained during the seminar session. But
it does not hurt to have a thought about it beforehand.
'''

# Probably use start and end pointers. Not sure how that would work since they'd need to look forward to the end which could use a lot of processing.


# ---- Exercise 2 ----
'''
Given a matrix (2D list) A[0. . n − 1, 0. . m − 1] of numbers, find the largest possible sum of a
rectangle submatrix. The top-left element in the matrix is A[0][0], and the element A[r][c] is
the element at row r, column c.

+-----+----+----+----+----+
|  6  | -5 | -7 |  4 | -4 |
+-----+----+----+----+----+
|  -9 |  3 | -6 |  5 |  2 |
+-----+----+----+----+----+
| -10 |  4 |  7 | -6 |  3 |
+-----+----+----+----+----+
|  -8 |  9 | -3 |  3 | -7 |
+-----+----+----+----+----+

For example, for the matrix given above, the rectangle with the largest sum is highlighted in
red with sum 17.
'''
def sum_submatrix(matrix:list, x1:int,y1:int,x2:int,y2:int)->int:
    result = 0
    for x in range(x1,x2):
        for y in range(y1,y2):
            result += matrix[x][y]
    return result

def get_submatrix_rect(matrix:list, rect:list)->list:
    return get_submatrix(matrix, rect[0], rect[1], rect[2], rect[3])

def get_submatrix(matrix:list, x1:int,y1:int,x2:int,y2:int)->list:
    new_matrix = []
    for x in range(x1,x2):
        row = []
        for y in range(y1,y2):
            row.append(matrix[x][y])
        new_matrix.append(row)
    return new_matrix

def largest_submatrix(matrix: list, width: int, height: int)->list:
    best_sum = -99999
    rect = []
    for x1 in range(width):
        for y1 in range(height):
            for x2 in range(x1,width):
                for y2 in range(y1,height):
                    curr_sum = sum_submatrix(matrix,x1,y1,x2,y2)
                    if(curr_sum > best_sum):
                        best_sum = curr_sum
                        rect=[x1,y1,x2,y2]
    return best_sum, get_submatrix_rect(matrix, rect)

matrix = [
    [6,-5,-7,4,-4],
    [-9,3,-6,5,2],
    [-10,4,7,-6,3],
    [-8,9,-3,3,-7]
]

print("---")
print(largest_submatrix(matrix,5,4))