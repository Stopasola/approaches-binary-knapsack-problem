#!/usr/bin/python
# -*- coding: utf-8 -*-
from knapsack import Knapsack
from greedy_algorithm import greedy_algorithm
from dynamic_programming import dynamic_programming
from write_file import write_benefit_graph, write_elapsed_time_graph, print_results

folder_path = 'Proposta/Mochila'
file_size = [50, 100, 200, 300, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000]


def mount_filename(file_index):
    return folder_path + str(file_size[file_index]) + '.txt'


if __name__ == '__main__':
    benefit_graph = []
    time_graph = []

    for index in range(0, len(file_size)):
        filename = mount_filename(index)
        knapsack = Knapsack(filename)

        greedy_result = greedy_algorithm(knapsack.capacity, knapsack.benefit, knapsack.cost)
        dynamic_result = dynamic_programming(knapsack.capacity, knapsack.benefit, knapsack.cost,
                                             len(knapsack.cost))

        benefit_graph.append([str('A'+str(filename)), str(greedy_result.get("benefit")),
                              str(dynamic_result.get("benefit"))])
        time_graph.append([str('A'+str(filename)), greedy_result.get("time"), dynamic_result.get("time")])

    write_benefit_graph(benefit_graph)
    write_elapsed_time_graph(time_graph)
    print_results(knapsack, greedy_result, dynamic_result)
