# Approaches to binary knapsack problem

![image](https://img.shields.io/github/languages/top/stopasola/minimum-cost-graph)


## Introduction

In this work, the chronological performance and the benefit achieved were analized,
through the Dynamic Programming and Greedy Strategy project strategies, implementing 
the binary knapsack problem.


## Hardware Methods and Configurations

It was used python 3.7 programming language and a computer with the following specs:

- Operating System: Windows 10 Professional, 64-bit
- Processor: Intel Core i5-4200U CPU @ 1.60GHz
- RAM memory: 8.00GB
- SSD: 230 GB

The analyzed datasets consist of 14 files containing respectively the infos to resolve the binary knapsack problem.
The sizes of analyzed knapsack consist of `50, 100, 200, 300, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000, 4000 and 5000`. 
All files were executed and further studied.

## Results and discussion

#### Greedy Strategy

In the greedy strategy, a smaller benefit was observed than the programming
dynamics across all file sizes, that is, the greedy strategy is not always
guaranteed the optimal solution to the problem. The results can be seen in the graph of
figure 1.
Related to the runtime for all analyzed files, the strategy
greedy was faster than dynamic programming, due to the use of the
ordering implemented in this strategy. The algorithm used was sort(), native to
python language, which consists of a hybrid implementation between the TimSort algorithms
and MergeSort [1]. The ordering used guaranteed a significant improvement in the
execution, because with the vector responsible for storing the Cost/Benefit information
already sorted, it was only necessary to assign the data found in the first
vector positions, instead of looking for the best Cost/Benefit in a vector
disordered.

#### Dynamic Programming

In this strategy, the best benefits were observed compared to the strategy
greedy, since dynamic programming always guarantees the optimal solution. For
To validate these data we handwritten calculations for a small dataset.
However, related to the execution time, we obtained longer times for this
strategy, this is due to the fact that the implemented algorithm calculates and stores in a
table, all possible possibilities, guaranteeing better results at the cost of a
longer processing time. Although dynamic programming takes longer to
processing compared to the greedy strategy, the use of a table that stores the
information already calculated guarantees faster processing at the cost of an expense of
bigger memory. Below are the comparative charts of both design strategies
implemented.

#### Conclusion

After analyzing the results, we can see that dynamic programming
always gave us the best benefits at the cost of more memory. already in
greedy strategy, we obtained good benefits but less than the optimal ones, combined with a
shorter execution time compared to dynamic programming, this is due to
sort optimization used in the code. However, without the optimization implemented the
processing time would be longer than the execution time of the scheduling strategy
dynamics.

## References

[1] [Visualising Sorting Algorithms: Python's timsort](https://corte.si/posts/code/timsort/index.html)

[2] [Python](https://www.python.org/)

