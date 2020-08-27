
def master_mind_check(answer: str, guess: str):
    hits = 0
    pseudo_hits = 0

    unhit_colours_ans = set()
    unhit_colours_guess = set()
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            hits += 1
        else:
            unhit_colours_ans.add(answer[i])
            unhit_colours_guess.add(guess[i])

    pseudo_hits = len(unhit_colours_ans & unhit_colours_guess)
    return hits, pseudo_hits


if __name__ == "__main__":
    exs = [
        ("RGBY", "GGRR"),
        ("RGBY", "RBGY"),
        ("RRYY", "RYGY")
    ]
    for ans, guess in exs:
        print(
            f"For ans {ans}, guess {guess} has hits, pseudos: {master_mind_check(ans,guess)}")
