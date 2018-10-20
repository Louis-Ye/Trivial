
user_input_target = [24.0]
user_input_elements = [1.0, 1.0, 2.0, 6.0]

input_elepairs = [(i, ele) for i, ele in enumerate(user_input_elements)]
input_format = [len(user_input_elements), len(user_input_elements) - 1]
input_ops = ['+', '-', '*', '/']

def Evaluate(elements, ops):
    value = elements[0]
    for i, op in enumerate(ops):
        if op == '+':
            value += elements[i + 1]
        elif op == '-':
            value -= elements[i + 1]
        elif op == '*':
            value *= elements[i + 1]
        elif op == '/':
            if elements[i + 1] != 0:
                value /= elements[i + 1]
    return value

def Search(elements, ops, eleindex_taken):
    if len(elements) == len(user_input_elements):
        if abs(Evaluate(elements, ops) - user_input_target[0]) < 0.0001:
            print 'Answer: ', elements, ops
            # print '---- ', elements_taken, ops_taken
        return
    if len(elements) == len(ops):
        for i, ele in input_elepairs:
            if i not in eleindex_taken:
                taken = eleindex_taken + [i]
                Search(elements + [ele], ops, taken)
                Search(elements + [-ele], ops, taken)
    else:
        for op in input_ops:
            Search(elements, ops + [op], eleindex_taken)

Search([], [], [])
