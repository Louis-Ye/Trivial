import itertools

user_input_target = [24]
user_input_elements = [3, 4, 12, 1]

user_input_target = [float(user_input_target[0])]
user_input_elements = [float(x) for x in user_input_elements]
input_elepairs = [(i, ele) for i, ele in enumerate(user_input_elements)]
sign_input_elepairs = input_elepairs + [(i, -ele) for i, ele in input_elepairs]
operations = [
    lambda a, b, a_s, b_s: (a + b, "({} + {})".format(a_s, b_s)),
    lambda a, b, a_s, b_s: (a - b, "({} - {})".format(a_s, b_s)),
    lambda a, b, a_s, b_s: (a * b, "({} * {})".format(a_s, b_s)),
    lambda a, b, a_s, b_s: (a / b if b != 0 else a,
                            "({} / {})".format(a_s, b_s)),
]

def Search(elements):
    if len(elements) == 1:
        yield (elements[0], "{}".format(elements[0]))
    else:
        for i in xrange(len(elements) - 1):
            for left_val, left_str in Search(elements[0:i + 1]):
                for right_val, right_str in Search(elements[i + 1:]):
                    for Op in operations:
                        yield Op(left_val, right_val, left_str, right_str)

def ValidPerm(perm):
    indexes = set()
    for i, ele in perm:
        if i in indexes:
            return False
        indexes.add(i)
    return True

def main():
    index = 0
    for perm in itertools.permutations(sign_input_elepairs,
                                       len(user_input_elements)):
        if ValidPerm(perm):
            for value, form_str in Search([ele for _, ele in perm]):
                if abs(value - user_input_target[0]) < 0.0001:
                    index += 1
                    print "Answer {}: {} = {}".format(index, form_str, value)

if __name__ == "__main__":
    main()
