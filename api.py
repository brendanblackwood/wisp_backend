import hug


@hug.get('/specialmath/{num}')
def special_math(num: hug.types.greater_than(-1)):
    prev2 = 0
    prev1 = 1
    
    if num < 2:
        return num

    # incrementally add the previous two f(n) to n
    for i in range(2, num+1):
        current = i + prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current