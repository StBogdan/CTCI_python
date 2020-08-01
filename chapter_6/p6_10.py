from typing import List
import random

BOTTLES_NUMBER = 100
TEST_STRIP_NUMBER = 10
MAGIC_INFECTED_BOTTLE_NUM = random.randint(0, BOTTLES_NUMBER)


class TestStrip:

    def __init__(self):
        self.samples = set()
        self.positive = False

    def add_sample(self, sample_id: int):
        self.samples.add(sample_id)


def test_strip(strip: TestStrip):
    if MAGIC_INFECTED_BOTTLE_NUM in strip.samples:
        strip.positive = True


def detect_poison_bottle(bottles: List[int], tests: List[TestStrip]) -> int:
    if len(bottles) > len(tests) ** 2:
        raise Exception("Cannot test in one pass")

    for i, bottle_id in enumerate(bottles):
        # Get the 10bit representation of i
        # use set bits to figure out which test to add_sample on
        for test_num, bit_mask_indicator in enumerate(map(int,f"{i:010b}")):
            if bit_mask_indicator:
                tests[test_num].add_sample(bottle_id)
    
    for strip in tests:
        test_strip(strip)

    # Reconstruct number from positive tests:
    # Pythonist one-liner
    # int("".join(map(str,[int(strip.positive) for strip in tests])),2)

    # Strong C-style for loop
    bottle_index = 1 if tests[0].positive else 0
    for strip in tests[1:]:
        bottle_index<<=1
        if strip.positive:
            bottle_index+=1

    return bottle_index


if __name__ == "__main__":
    soda_bottles = list(range(0, BOTTLES_NUMBER))
    test_strips = [TestStrip() for _ in range(TEST_STRIP_NUMBER)]
    print(
        f"Poison bottle is {detect_poison_bottle(soda_bottles,test_strips)},"
        f" actual {MAGIC_INFECTED_BOTTLE_NUM}")
