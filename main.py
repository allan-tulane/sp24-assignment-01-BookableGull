"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x == 0:
        return 0
    else:
        return x + foo(x - 1)
    ### TODO
        pass

def longest_run(mylist, key):
    sequence_amount = 0
    max_sequence = 0
    for number in mylist:
        if number == key and sequence_amount == 0:
            sequence_amount = 1
        elif number == key and sequence_amount > 0:
            sequence_amount += 1
        else:
            sequence_amount = 0
        if sequence_amount > max_sequence:
            max_sequence = sequence_amount
    return max_sequence
    ### TODO
pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    def _find_longest_run(mylist, key, current_streak, max_streak):
        if not mylist:
            return max_streak
        if mylist[0] == key:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
        return _find_longest_run(mylist[1:], key, current_streak, max_streak)

    return _find_longest_run(mylist, key, 0, 0)

    ### TODO
    pass



