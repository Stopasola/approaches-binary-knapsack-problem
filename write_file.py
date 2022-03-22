import csv


def write_benefit_graph(benefit_graph):
    with open('benefit_graph.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(['Arq', 'Ben_EG', 'Ben_PD'])
        for i in range(0, len(benefit_graph)):
            spamwriter.writerow([benefit_graph[i][0], benefit_graph[i][1], benefit_graph[i][2]])


def write_elapsed_time_graph(time_graph):
    with open('GraficoTempo.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(['Arq', 'Tempo_EG', 'Tempo_PD'])
        for i in range(0, len(time_graph)):
            spamwriter.writerow([time_graph[i][0], time_graph[i][1], time_graph[i][2]])


def print_results(knapsack, greedy_result, dynamic_result):
    print("-----------------------------------------")
    print('filemame', knapsack.filemame)
    print('beneficio_EG', greedy_result.get("benefit"))
    print('tempo_EG', greedy_result.get("time"))
    print('beneficio_PD', dynamic_result.get("benefit"))
    print('tempo_PD', dynamic_result.get("time"))
