"""
def harmonic_list(n):
    result = []
    h = 0
    for i in range(1, n + 1):
        h += 1/i
        result.append(h)
    return result
"""

def harmonic_gen(n):
    h = 0
    for i in range(1, n + 1):
        h += 1/i
        yield h


#test1 = 5
#print(harmonic_list(test1))
#test2 = harmonic_gen(5)
#print(list(test2))
