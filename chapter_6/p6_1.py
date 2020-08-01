import random
import math
from typing import List

class Bottle:
    def __init__(self, pill_weight):
        self.pill = pill_weight

def populate_pills(bottle_num:int ) -> List[Bottle]:
    special_bottle = random.randint(0,bottle_num)
    print(f"Special bottle will be {special_bottle+1} (1 indexed)")
    return [Bottle(1.0 if i != special_bottle else 1.1) for i in range(bottle_num)]

def detect_special_bottle(bottles:List[Bottle]) -> int:
    expected_sum =0
    pill_pile = 0
    for i in range(len(bottles)):
        pill_pile += (i+1)* bottles[i].pill * 10
        expected_sum += (i+1) * 10
    
    outstanding_pill = pill_pile - expected_sum
    # print(outstanding_pill)
    return math.ceil(outstanding_pill)

if __name__ == "__main__":
    number_of_bottles =20
    bottles = populate_pills(number_of_bottles)
    print(f"Special bottle is {detect_special_bottle(bottles)}")
