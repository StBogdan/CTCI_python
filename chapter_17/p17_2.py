import random


def shuffle_deck():
    deck = [0 for _ in range(52)]
    for i in range(1, 53):
        place = random.randint(0, i-1)
        deck[i-1], deck[place] = deck[place], i
    return deck


if __name__ == "__main__":
    print(shuffle_deck())
