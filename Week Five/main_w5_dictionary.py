# WEEK 5 – PRACTICAL 4a


# ---- Exercise 0 ----
'''
In the interpreter, write assignment statements that create dictionaries for the following sets of data:
a) The months of the year, using numbers from 1 to 12 as keys and month names as values.
b) The roman numbers as keys (M, …, X, V, I) and their Arabic number equivalent (1000,
…, 10, 5, 1).
c) The first 7 elements in the periodic table, where keys are chemical symbols ("H", "He",
"Li", etc.) and values are the names of the elements.
d) Create an empty dictionary roman.
    1) Write a series of statements to add to the dictionary the following key-value
        pairing 100,000:T, 1000:M, 500:D, 100:K, L:50, 10:X, 5:V and 1:I.
    2) Write a statement to modify the value associated with the key 100 to C (instead of K)
    3) Write a statement to delete the pairing 100,000:T
'''

# This is really pointless. You can just make this into an array. No need for a dictionary.
months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

roman_nums = {"M":1000, "C":100, "X":10, "V":5, "I":1}

elements = {"H":"Hydrogen", "He":"Helium", "Li":"Lithium", "Be":"Beryllium", "B":"Boron", "C":"Carbon", "N":"Nitrogen"}

roman = {}
roman["T"]=100000
roman["M"]=1000
roman["D"]=500
roman["K"]=100
roman["L"]=50
roman["X"]=10
roman["V"]=5
roman["I"]=1

del roman["K"]
roman["C"]=100

del roman["T"]


# ---- Exercise 1 ----
'''
Write a Python function display_dico(dico) that takes a dictionary as parameter and print the
content of the dictionary, one paired element per line as follow:
Key --> Value

For example:

>>> display_dico({"un":1, "deux":2, "trois":3})
un --> 1
deux --> 2
trois --> 3
'''

def display_dico(dictionary: dict):
    for key in dictionary.keys():
        print(key,"-->",dictionary[key])

print("---")
display_dico({"un":1, "deux":2, "trois":3})


# ---- Exercise 2 ----
'''
Write a function concat_dico(dico1, dico2) that takes two dictionaries as parameters
and returns a single dictionary containing the pairs from both dictionaries. An important
requirement is that both dictionaries are NOT modified by the function.

For example:
>>> concat_dico ({"one":1, "two":2, "three":3}, {"four":4, "five":5})
{"one":1, "two":2, "three":3, "four":4, "five":5}
'''

def concat_dico(dict1: dict, dict2: dict) -> dict:
    result = {}
    result.update(dict1)
    result.update(dict2)
    return result

dict1={"one":1, "two":2, "three":3}
dict2={"four":4, "five":5}

print("---")
print(concat_dico (dict1, dict2))
print(dict1)
print(dict2)

'''
The Advanced bit:
An issue may arise when both dictionaries share a least one common key. Rewrite the function
so that the method store the values in a list if dico1 and dico2 share a common key. In the
example below both dictionaries share the keys "two" and "five".
>>> concatDico ({"one":1, "two":2, "five":5}, {"two": "10", "five":"101"})
{"one":1, "two":[2, "10"], "five":[5,"101"]}
'''

# Has it's limitations, like if a dictionary already has a list as a value, it may put the list in another list
def concatDico(dict1: dict, dict2: dict) -> dict:
    result = {}
    result.update(dict1)
    for key in dict2.keys():
        if key in result:
            result[key] = [result[key],dict2[key]]
        else:
            result[key]=dict2[key]
    return result

print("---")
print(concatDico({"one":1, "two":2, "five":5}, {"two": "10", "five":"101"}))


# ---- Exercise 3 ----
'''
Write a function map_list(keys, values) that takes two list of the same length as
parameters and returns a dictionary where the keys are the elements from the list keys and the
values are the elements from the list values. The mapping follows the lists indices.
For example:
>>> map_list([‘un’, ‘two’], [1,2])
{‘un’:1, ‘two’:2}
'''

def map_list(keys: list, values: list) -> dict:
    return {keys[i]:values[i] for i in range(len(keys))}

print("---")
print(map_list(["one", "two"], [1,2]))

'''
The Advanced bit:
An issue may arise if the list keys as duplicate elements as the keys must be unique. Rewrite
the function so that the method returns None and print an error message if keys has duplicates.
Note that having duplicate values in the values list is fine.
Note: This function could be used to map the list of English alphabet characters with the list of
their frequencies in the English language.
'''

def map_list(keys: list, values: list) -> dict:
    result = {}
    for i in range(len(keys)):
        if(keys.count(keys[i]) > 1):
            print("Keys list has duplicate items!")
            return None
        result[keys[i]]=values[i]
    return result

print("---")
print(map_list(["one", "two", "two"], [1,2,2]))


# ---- Exercise 4 ----
'''
Write a function reverse_dictionary(dico) that reverse the mapping between keys
and values. The parameter dico is a dictionary where the keys and values are all immutable.
The function should return a dictionary where the pair key1:value1 in dico becomes the
pair value1:key1. For example:
>>> reverse_dictionary({"one":1, "two":2})
{1:"one", 2:"two"}
'''

def reverse_dictionary(dico: dict) -> dict:
    result = dico.copy()
    keys = list(dico.keys())
    for i in range(len(dico)):
        result[keys[i]] = dico[keys[-i-1]]
    return result

print("---")
print(reverse_dictionary({"one":1, "two":2}))

'''
The Advanced bit:
An issue may arise again if the dictionary dico has duplicate elements in its values. Rewrite
the function so that the method returns None and print an error message if that is the case.
'''

def reverse_dictionary_no_dupe(dico: dict) -> dict:
    result = dico.copy()
    keys = list(dico.keys())
    for i in range(len(dico)):
        if(list(dico.values()).count(dico[keys[i]])>1):
            print("The dictionary contains duplicated values!")
            return None
        result[keys[i]] = dico[keys[-i-1]]
    return result

print("---")
print(reverse_dictionary_no_dupe({"one":1, "two":2, "three":2}))