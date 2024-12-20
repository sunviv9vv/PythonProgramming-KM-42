def cons(head, tail):
    return [head] + tail

def sumlist(lst):
    if not lst:
        return 0
    return lst[0] + sumlist(lst[1:])

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1, []) == [1], 'Failed test 2'
print('All tests good!')

print(sumlist(l))
assert sumlist(l) == 6, 'Failed on sum'
print('All tests good!')