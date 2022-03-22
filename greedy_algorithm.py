import time


def greedy_algorithm(capacity, benefit_array, cost_array):

    start_time = time.time()
    cost_benefit = []
    benefit = 0

    for i in range(0, len(cost_array)):
        if int(cost_array[i]) != 0:
            cost_benefit.append((int(benefit_array[i])/int(cost_array[i]), i))
            cost_benefit.sort(reverse=True)
    i = 0
    while i < len(cost_benefit):
        if capacity >= int(cost_array[cost_benefit[i][1]]):
            capacity -= int(cost_array[cost_benefit[i][1]])
            benefit += int(benefit_array[cost_benefit[i][1]])
        i += 1
    elapsed_time = round((time.time() - start_time), 5)
    
    return {"benefit": benefit, "time": elapsed_time}
