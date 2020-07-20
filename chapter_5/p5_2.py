
# TODO Figure out how to make this work in Python
#  This is the intuition of the CTCI solution

def float_bin_rep(a: float) -> str:
    max_len = 32
    ans = []
    while a > 0:
        print(f"A now is {a}")
        if len(ans) >= max_len:
            raise Exception("Float too long to show")
        a *= 2
        if a >= 1:
            ans.append("1")
            a -= 1
        else:
            ans.append("0")
    return "".join(["0."] + ans)


if __name__ == "__main__":
    exs = [0.72, 0.20, 0.3253, 0.53405, 0.1111113]
    for ex in exs[:1]:
        x_int = int(str(ex)[2:])
        try:
            print(f"Binary of the fract part of {ex} is {float_bin_rep(ex)}, expected {x_int:b}")
        except Exception as e:
            print(f"Issue with showing {ex}, expected {x_int:b}")