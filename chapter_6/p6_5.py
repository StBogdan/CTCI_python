class Jug:

    def __init__(self, capacity_liters):
        super().__init__()
        self.capacity_liters = capacity_liters
        self.current_fill = 0

    def empty(self):
        self.current_fill = 0

    def fill(self):
        self.current_fill = self.capacity_liters

    def fill_from(self, other_jug):
        if self.capacity_liters - self.current_fill > other_jug.current_fill:
            # Pour the whole other jug
            self.current_fill += other_jug.current_fill
            other_jug.current_fill = 0
        else:
            # Just top off the current
            other_jug.current_fill -= self.capacity_liters - self.current_fill
            self.current_fill = self.capacity_liters


if __name__ == "__main__":
    jug_3l = Jug(3)
    jug_5l = Jug(5)

    # Create a fill of 2L in small one
    jug_5l.fill()
    jug_3l.fill_from(jug_5l)
    jug_3l.empty()

    # Fill 5 in the big one, top off the small one with 1L
    jug_3l.fill_from(jug_5l)
    jug_5l.fill()
    jug_3l.fill_from(jug_5l)

    print(f"Now in the big jug, we have {jug_5l.current_fill}")

    # Progress on water quantities in the jugs
    # 5 - 0
    # 2 - 3
    # 2 - 0
    # 0 - 2
    # 5 - 2
    # 4 - 0
