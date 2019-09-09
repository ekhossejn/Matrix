import copy
class MyMatrix:
    def __init__(self, data: list):
        if not type(data) == list:
            raise TypeError
        self.__matrix = copy.deepcopy(data)
              
    def __repr__(self):
        s = []
        for i in range(len(self.__matrix)):
            s.append(' '.join(map(str, self.__matrix[i])))
        return '\n'.join(s)

    def size(self) -> tuple:
        if len(self.__matrix) == 0:
            return (0, 0)
        return (len(self.__matrix), len(self.__matrix[0]))

    def flip_up_down(self):
        self.__matrix = self.__matrix[::-1]

    def flip_left_right(self):
        self.__matrix = [elem[::-1] for elem in self.__matrix]

    def flipped_up_down(self):
        a = copy.deepcopy(self.__matrix)
        return a[::-1]

    def flipped_left_right(self):
        a = copy.deepcopy(self.__matrix)
        return [elem[::-1] for elem in a]

    def transpose(self):
        n, m = len(self.__matrix), len(self.__matrix[0])
        new = [[0 for i in range(n)] for i in range(m)]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                new[j][i] = self.__matrix[i][j]
        self.__matrix = copy.deepcopy(new)

    def transposed(self):
        n, m = len(self.__matrix), len(self.__matrix[0])
        new = [[0 for i in range(n)] for i in range(m)]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                new[j][i] = self.__matrix[i][j]
        return new
