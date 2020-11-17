import math

def is_power(a:int, b:int) -> bool:
    if(b == 1): return a==1
    if(b==0): return a==0
    if (a == b): return True
    if(a<b): return False
    print(a,b)
    return is_power(a/b,b)

#print(is_power(3,1))

def rec_sum(numbers: list) -> int:
    if(len(numbers) < 1): return 0
    if(len(numbers) == 1): return numbers[0]
    numbers[0]+=numbers.pop()
    return rec_sum(numbers)

#print(rec_sum([1,2,3,4]))

def sum_digits(number):
    if number == 0: return 0
    if number < 0: number = -number
    return number % 10 + sum_digits(number // 10)

#print(sum_digits(1234567))

def flatten(mlist: list)->list:
    if len(mlist) == 0: return []
    if isinstance(mlist[0],list):
        return flatten(mlist[0])+flatten(mlist[1:])
    else:
        return mlist[:1]+flatten(mlist[1:])

#print(flatten([[1], [1,[2,3]],3,4]))



def iselfish_cheating(word: str)->bool:
    print(word)
    if(len(word) > 100): return False # prevent massive strings for now
    if not word[-1].isalpha():
        word_text, flags, index = word.split("|")
        if(flags=="111"): return True
        flags = [int(x) for x in flags]
        index = int(index)
        if word_text[index] == "e": flags[0] = 1
        elif word_text[index] == "l": flags[1] = 1
        elif word_text[index] == "f": flags[2] = 1
        flags = "".join(str(x) for x in flags)
        index = str(index+1)
        word = f"{word_text}|{flags}|{index}"
        return iselfish_cheating(word)
    else:
        word+="|000|0"
        return iselfish_cheating(word)
        

#print(iselfish_cheating("unfriendly"))

def iselfish(word: str, flags: int = 0b000) -> bool:
    if flags == 0b111: return True
    if len(word) <= 0: return False
    if word[0] == "e": flags |= 0b100
    elif word[0] == "l": flags |= 0b010
    elif word[0] == "f": flags |= 0b001
    return iselfish(word[1:], flags)

#print(iselfish("unfriendly"))

def something_ish(pattern: str, word: str, flags: int = 0b0) -> bool:
    if flags == 2**len(pattern)-1: return True
    if len(word) <= 0: return False
    try:
        index = pattern.index(word[0])
        flags |= 2**index
    except ValueError: pass #if not in word, ignore
    return something_ish(pattern, word[1:], flags)

print(something_ish("clboh","hello barry scott"))