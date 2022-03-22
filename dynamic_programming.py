import time


def dynamic_programming(capacity, benefit_array, cost_array, cost_array_size):
    start_time = time.time()
    matrix = [[0 for x in range(capacity + 1)] for x in range(cost_array_size + 1)]

    for i in range(cost_array_size + 1):
        for capacity in range(capacity + 1):
            if i == 0 or capacity == 0:
                matrix[i][capacity] = 0
            elif cost_array[i - 1] <= capacity:
                # insert biggest element
                matrix[i][capacity] = max(benefit_array[i - 1] + matrix[i - 1][capacity - cost_array[i - 1]], matrix[i - 1][capacity])
            else:
                matrix[i][capacity] = matrix[i - 1][capacity]  # previous cell element is propagated

    elapsed_time = round((time.time() - start_time), 5)

    return {"benefit": matrix[cost_array_size][capacity], "time": elapsed_time}
