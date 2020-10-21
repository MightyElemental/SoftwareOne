import re
import textanalysis
# WEEK 4 - ADDITIONAL EXERCISES

# ---- Exercise 1: The King and the Wise man ----
'''
When the creator of the game of chess showed his invention to the ruler of the country, the
ruler was so pleased that he gave the inventor the right to name his prize for the invention. The
man, who was very wise, asked the king this: that for the first square of the chess board, he
would receive one grain of wheat (in some telling, rice), two for the second one, four on the
third one, and so forth, doubling the amount each time. The ruler, arithmetically unaware,
quickly accepted the inventor's offer, even getting offended by his perceived notion that the
inventor was asking for such a low price and ordered the treasurer to count and hand over the
wheat to the inventor. Given that the chessboard is a 8 × 8 board and given the weight of a
single grain of rice is about 30 mg, calculate the total weight of rice the king must give to the
wise man. The program should print the weight of rice for each chessboard square.
'''

# Probabily overcomplicating this, but I'm going to display this in a table
# for position x, y, the amount of rice is calculated as such (first square is 0,0):
# 2**(y*8+x)

## [[gain_count,...],...]
chess_board = []

# milligrams, ..., tonnes, kilotonnes, ..., teratonnes
mass_units = ["mg","g","kg","T","KT","MT","GT","TT"]

# Takes a mass (mg) and converts it to a more readable format
# Longest output is 5 characters
def humanReadableAmount(mass: int, includeFrac: bool = False) -> str:
    unit = 0
    while(mass > 1000):
        unit += 1
        mass /= 1000
    if includeFrac:
        return str(round(mass,3))+mass_units[unit]
    else:    
        return str(int(mass))+mass_units[unit]

# calculate grain amounts
for x in range(8):
    row = []
    for y in range(8):
        grain_count = 2**(x*8+y)
        row.append(grain_count)
    chess_board.append(row)

print("---")

# print grain masses in table (all values are rounded)
print("+-----"*len(chess_board[0])+"+")
for x in range(len(chess_board)):
    masses = ['{s:{c}^{n}}'.format(s=humanReadableAmount(cell*30),n=5,c=' ') for cell in chess_board[x]]
    print("|","|".join(map(str,masses)),"|", sep="")
    print("+-----"*len(chess_board[x])+"+")

# print the total mass of grain
total_grains = sum(sum(chess_board,[]))
print("Total grains:",total_grains)
print("Total mass:",humanReadableAmount(total_grains*30, True))


# ---- Exercise 2, 3: from a resit paper ----
'''
---- Exercise 2 ----
You must use the file textanalysis.py to answer this question. Write a function
get_words_starting_with(text, letter) that returns the list of words starting
with letter in the string text. The result should not be case sensitive, e.g. ’about’ should
be returned if the letter ’a’ or ’A’ is given as parameter. For simplicity, we assume for exercises
2,3, and 4 that the text does not have any punctuations, and words are separated by at least one
blank space.

For example, using the variable sample_text we should obtain:

>>> get_words_starting_with (sample_text, ’a’)
[’As’, ’a’, ’about’, ’adding’, ’a’, ’ago’, ’a’,
’around’, ’Amsterdam’, ’a’, ’and’, ’an’, ’about’,
’a’, ’ABC’, ’appeal’, ’as’, ’a’, ’a’, ’and’, ’a’]
>>> get_words_starting_with(sample_text, ’z’)
[]

---- Exercise 3 ----
As you can see in question 2, there are many repetitions of the word ’a’ in the list. Improve
your solution so no repetition of the same word occurs in the list.

>>> get_words_starting_with(sample_text, ’a’)
[’As’, ’a’, ’about’, ’adding’, ’ago’, ’around’,
’Amsterdam’, ’and’, ’an’, ’ABC’, ’appeal’, ’as’]
'''

# Use regex to find words starting with specific letter
def get_words_starting_with(text: str, letter: str) -> str:
    if(len(letter) != 1): raise Exception("letter must be a single character!")
    return set(re.findall(r"(?i)(\b["+letter+"].*?)\s", text))

print("---")
print(get_words_starting_with(textanalysis.sample_text, 'a'))

# ---- Exercise 4: extension of Practical 2 Exercise 3 ----
'''
In cryptography, a Caesar cipher, also known as the shift cipher, is one of the simplest and
most widely known encryption techniques. It is a type of substitution cipher in which each
letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. 

For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The
method is named after Julius Caesar, who used it to communicate with his generals.

Mathematically, a Caesar cipher can be expressed by
the following equation:
c = (p + a) mod 26

1. Write a function caesar_encrypt that encrypts a plain text into a cypher text using
the Caesar Cipher algorithm. What parameters are needed? Should the function return
something? For simplicity, assume that only alphabet letters are encrypted, other
symbols remain the same.

2. Write a function caesar_decrypt that decrypts a cipher text into a plain text using
the Caesar Cipher algorithm. What parameters are needed?

3. Given the cipher text below, and knowing it has been encrypted using a Caesar Cipher
algorithm, could you decrypt it?
"bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc
bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc
bmtt bpmu bw lw."
'''

def caesar_encrypt(text: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    encrypted_msg = ""
    for c in text.lower():
        if c not in alphabet:
            # "other symbols remain the same"
            encrypted_msg+=c
            continue
        index = alphabet.index(c)
        new_index = (index+shift) % len(alphabet)
        encrypted_msg += alphabet[new_index]
    return encrypted_msg

def caesar_decrypt(text: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    decrypted_msg = ""
    for c in text.lower():
        if c not in alphabet:
            # "other symbols remain the same"
            decrypted_msg+=c
            continue
        index = alphabet.index(c)
        new_index = (index-shift) % len(alphabet)
        decrypted_msg += alphabet[new_index]
    return decrypted_msg

def caesar_decrypt_brute_force(text: str) -> str:
    for i in range(26):
        print("shift +",i,":",caesar_decrypt(text,i))

print("---")
msg = "bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc bmtt bpmu bw lw."
caesar_decrypt_brute_force(msg)
# the good news about computers is that they do what you tell them to do. the bad news is that they do what you tell them to do.


# ---- Exercise 5: Vectors ----
'''
A vector of dimension 𝑛𝑛 can be represented by a list in Python. For example, a vector of
dimension 3 could represent a point in space, and a vector of dimension 4 could represent a
point in space and time (the fourth dimension being the time).

The vector could be stored in a Python list [a, b, c]. There are two simple operations that
can be done on vector, and the result of the two operation is also a vector. The two operations
are: Scalar product, and addition.

Implement two functions:

1. scalar_product(scalar, vector) where scalar is a float and vector is a list
of float. The function returns the scalar product of the two parameters.

2. vector_addition(vector1, vector2) where vector1 and vector2 are
lists of float. The function returns the vector addition of the two parameters. If
vector1 and vector2 don’t have the same dimension, you should print an error
message and return None.
'''

def scalar_product(scalar: int, vector: list) -> list:
    return [scalar*x for x in vector]

def vector_addition(vector1: list, vector2: list) -> list:
    if(len(vector1) != len(vector2)): raise Exception("Vectors must have same dimensions!")
    return [vector1[i]+vector2[i] for i in range(len(vector1))]

vec1 = [3,4,5]
vec2 = [6,7,8]
vec3 = [1,2,3,4,5]

print("---")
print(scalar_product(5, vec1))     # [15, 20, 25]
print(vector_addition(vec1, vec2)) # [9, 11, 13]
print(vector_addition(vec1, vec3)) # Exception: Vectors must have same dimensions!