from typing import List


def eval_operation(ops_string: str) -> float:
    tokens = tokenise(ops_string)

    reduced_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "/":
            reduced_tokens[-1] /= tokens[i+1]
            i += 2
        elif tokens[i] == "*":
            reduced_tokens[-1] *= tokens[i+1]
            i += 2
        else:
            reduced_tokens.append(tokens[i])
            i += 1

    final_result = reduced_tokens[0]
    i = 1
    # print(tokens)
    # print(reduced_tokens)
    while i < len(reduced_tokens):
        if reduced_tokens[i] == "+":
            final_result += reduced_tokens[i+1]
        elif reduced_tokens[i] == "-":
            final_result -= reduced_tokens[i+1]
        i += 2

    return final_result


def tokenise(raw: str) -> list:
    tokens = []
    cnum = None  # Only have positive integers
    for c in raw:
        if c.isdigit():
            if cnum:
                cnum *= 10
                cnum += int(c)
            else:
                cnum = int(c)
        elif c in "-+/*":
            if cnum:
                tokens.append(cnum)
                cnum = None
            tokens.append(c)
        else:
            raise Exception("Unknown charater is string: ", c)

    if cnum:
        tokens.append(cnum)

    return tokens


if __name__ == "__main__":
    exs = [
        "234-134+50/25*5*2+3",
    ]

    for ex in exs:
        print(f"Result of operation {ex} is {eval_operation(ex)}")
