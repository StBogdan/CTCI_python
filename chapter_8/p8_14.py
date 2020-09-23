from functools import lru_cache, partial
from typing import List


@lru_cache(None)
def count_eval(form: str, result: bool):
    if len(form) == 1:
        literal = int(form)
        return 1 if bool(literal) == result else 0

    ways = 0
    for i in range(0, len(form)-1, 2):
        current_op = form[i+1]
        left_side = partial(count_eval, form[:i+1])
        right_side = partial(count_eval, form[i+2:])

        if current_op == "&":
            if result == True:
                ways += left_side(True) * right_side(True)
            else:
                ways += left_side(False) * right_side(True) \
                    + left_side(True) * right_side(False) \
                    + left_side(False) * right_side(False)
        elif current_op == "^":
            if result == False:
                ways += left_side(False) * right_side(False) \
                    + left_side(True) * right_side(True)
            else:
                ways += left_side(True) * right_side(False) \
                    + left_side(False) * right_side(True)
        elif current_op == "|":
            if result == False:
                ways += left_side(False) * right_side(False)
            else:
                ways += left_side(True) * right_side(True) \
                    + left_side(False) * right_side(True) \
                    + left_side(True) * right_side(False)
        
    # print(f"Looking to package {form} for {result}, ways for this {ways}")
    return ways

if __name__ == "__main__":
    exs = [
        ("1^0", True),
        ("1^0|0|1", False),
        ("0&0&0&1^1|0", True)
    ]

    for formula, target in exs:
        print(f"Ways to partition {formula} for {target} are {count_eval(formula, target)}")