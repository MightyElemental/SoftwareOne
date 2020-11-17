# WEEK 8 - SEMINAR 4

# ---- Exercise 1 ----
'''
Write a recursive algorithm (using pseudo-code) sum_all(numbers:list):list that
takes a multidimensional list of integers as parameters and returns the sum of all elements in
that list. Note, empty lists sum to 0. For examples:
'''

'''
Function sum_all(numbers:list):int
    if numbers.length == 0 then
        return 0
    endif
    if numbers[0] is type list then
        right_list := empty List
        for i:=1 to numbers.length do
            right_list.append(numbers[i])
        endfor
        return sum_all(numbers[0])+sum_all(right_list)
    else
        right_list := empty List
        for i:=1 to numbers.length do
            right_list.append(numbers[i])
        endfor
        return numbers[0]+sum_all(right_list)
    endif
'''

def sum_all(numbers:list)->int:
    if len(numbers) == 0: return 0
    if isinstance(numbers[0], list):
        return sum_all(numbers[0])+sum_all(numbers[1:])
    else:
        return numbers[0]+sum_all(numbers[1:])

#print(sum_all([1,[2,3],4]))

# ---- Exercise 2 ----
