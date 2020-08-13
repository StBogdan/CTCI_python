from typing import Tuple, List


def living_people(ppl: List[Tuple[int, int]]) -> int:
    year_now = 0
    max_pop = 0
    max_pop_year = 0

    births, deaths = zip(*ppl)
    births = list(births)
    deaths = list(deaths)

    births.sort()
    deaths.sort()

    in_i = 0
    out_i = 0
    now_pop = 0

    while in_i < len(births):
        year_now = births[in_i]

        # All deaths up to this year (excl)
        while out_i < len(deaths) and deaths[out_i] < year_now:
            max_pop -= 1
            out_i += 1

        now_pop += 1
        if now_pop > max_pop:
            max_pop = now_pop
            max_pop_year = births[in_i]
        in_i += 1

    return max_pop_year


if __name__ == "__main__":
    ex = [(1900, 2000), (1910, 1920), (1944, 1944), (1944, 1944),
          (1934, 1944)]
    ex2 = [(12, 15), (20, 90), (10, 98), (1, 72), (10, 98),
           (23, 82), (13, 98), (90, 98), (83, 99), (75, 94)]

    print(f"Most living ppl in the list are in year {living_people(ex2)}")
