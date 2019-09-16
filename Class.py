import copy
class MyMatrix:
    def __init__(self, data: list):
        if not type(data) == list:
            raise TypeError
        len_stroka = -1
        for i in range(len(data)):
            if len_stroka == -1:
                len_stroka = len(data[0])
            elif len_stroka == len(data[i]):
                continue
            else:
                raise MatrixError('Matrix is wrong')
        self.__matrix = copy.deepcopy(data)

    def get_data(self):
        c = copy.deepcopy(self.__matrix)
        return c
    
    def __repr__(self):
        max_num_len = - float('INF')
        for elem in self.__matrix:
            for num in elem:
                if len(str(num)) > max_num_len:
                    max_num_len = len(str(num))
        s = []
        a = '{:' + str(max_num_len  + 1) + '}'
        for elem in self.__matrix:
            s.append(str())
            for num in elem:
                s[-1] += a.format(num)
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
        a = MyMatrix(copy.deepcopy(self.__matrix))
        a.flip_up_down()
        return a

    def flipped_left_right(self):
        a = MyMatrix(copy.deepcopy(self.__matrix))
        a.flip_left_right()
        return a

    def transpose(self):
        if len(self.__matrix) == 0:
            n, m = 0, 0
        else:
            n, m = len(self.__matrix), len(self.__matrix[0])
        new = [[0 for i in range(n)] for i in range(m)]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                new[j][i] = self.__matrix[i][j]
        self.__matrix = copy.deepcopy(new)

    def transposed(self):
        a = MyMatrix(copy.deepcopy(self.__matrix))
        a.transpose()
        return a
