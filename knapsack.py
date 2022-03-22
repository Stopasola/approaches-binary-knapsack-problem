class Knapsack:
    def __init__(self, filemame):
        self.capacity = 0
        self.benefit = []
        self.cost = []
        self.open_knapsack_file(filemame)
        self.filemame = filemame

    def open_knapsack_file(self, filemame):
        file = open(filemame, 'r')
        self.capacity = int(file.readline())
        self.benefit = list(map(int, file.readline().split('\t')[:-1]))
        self.cost = list(map(int, file.readline().split('\t')[:-1]))
        file.close()
