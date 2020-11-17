
def is_power(a:int, b:int) -> bool:
    if(b == 1): return a==1
    if(b==0): return a==0
    if (a == b): return True
    if(a<b): return False
    print(a,b)
    return is_power(a/b,b)

print(is_power(3,1))

def rec_sum(numbers: list) -> int:
    if(len(numbers) == 1):
        return numbers[0]
    numbers[0]+=numbers.pop()
    return rec_sum(numbers)