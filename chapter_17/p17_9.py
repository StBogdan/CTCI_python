


from collections import deque

def analyse_elem(x:int):
    divs = (3,5,7)
    div_occ = [0] * len(divs)
    for i in range(len(divs)):
        div = divs[i]
        temp_x = x
        while temp_x % div == 0:
            div_occ[i] +=1
            temp_x //= div
    
    return div_occ, sum(div_occ)

def get_kth_357(k:int):
    queues = {
        3 : deque(),
        5: deque(),
        7: deque()
    }
    
    queues[3].append(3)
    queues[5].append(5)
    queues[7].append(7)

    elem_now = 0
    for i in range(k):
        min_q_key = min(queues, key=lambda x: queues[x][0])
        elem_now = queues[min_q_key][0]
        # print(f"Series elem {i}\t{elem_now:20}, {analyse_elem(elem_now)}")
        queues[min_q_key].popleft()

        for x in queues:
            if x >= min_q_key:
                queues[x].append(elem_now * x)
    
    return elem_now

if __name__ == "__main__":
    k = 100
    print(get_kth_357(k))


