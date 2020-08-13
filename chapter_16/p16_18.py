from typing import List


def get_posib_combo(pattern_str: str, n: int) -> List[tuple]:
    ca = pattern_str.count('a')
    cb = pattern_str.count('b')

    if cb == 0:
        if n % ca != 0:
            return []
        else:
            return [(n//ca,0)]

    posibs = []
    for i in range(0, n//ca + 1):
        if (n-(ca*i)) % cb == 0:
            posibs.append((i, (n - ca*i) // cb))
    return posibs


def check_posib(text, pattern, ca, cb):
    # print(f"Checking pos {ca} and {cb}")
    a = text[:ca]
    b = None

    p_i = 1
    t_i = ca
    while p_i < len(pattern) and t_i < len(text):
        if pattern[p_i] == 'a':
            if text[t_i: t_i + ca] != a:
                # print(f"Failed at check {text[t_i: t_i + ca]} agains a: {a}")
                return False
            else:
                t_i += ca
        else:
            if not b:
                b = text[t_i: t_i + cb]
                t_i += cb
            else:
                if text[t_i: t_i + cb] != b:
                    # print(f"Failed at check {text[t_i: t_i + cb]} agains b: {b}")
                    return False
                else:
                    t_i += cb
        p_i += 1
    # print(f"Ending todays check with {p_i} of {len(pattern)} and {t_i} of {len(text)}")
    return p_i == len(pattern) and t_i == len(text)


def flip_pattern(p):
    if p[0] == 'b':
        return p.translate(str.maketrans("ab", "ba", ""))
    else:
        return p


def check_pattern_match(text: str, pattern: str) -> bool:
    pattern = flip_pattern(pattern)
    # print(f"Flipped pattern is : {pattern}")
    posibs = get_posib_combo(pattern, len(text))
    # print(f"Looking at combos pattern is : {posibs}")

    return any(check_posib(text, pattern, ca, cb) for ca, cb in posibs)


if __name__ == "__main__":
    exs = [("catcatgocatgo", "aabab"),
           ("catcatgocatgo", "bbaba"),
           ("catcatgocatgo", "b"),
           ("catcatgjocatgo", "aa"),
           ("catcatgocatgo", "ba"),
           ("catcat", "aaa"),
           ("catcat", "bb"),("a","bb")]
    for text, pattern in exs:
        print(f"'{text}' fits patterns '{pattern}'' ? {check_pattern_match(text, pattern)}")
        print("-"*50)
