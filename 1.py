import copy

def size(a):
    if len(a) == 0:
        return (0, 0)
    else:
        return(len(a), len(a[0]))

def check_size(now, other):
    n, m = size(now)
    n2, m2 = size(other)
    if n != n2 or m != m2:
        raise MatrixError("Sizez of matrixs are different")
    return (n, m)

class MyMatrix:
    def __init__(self, data: list):
        if not type(data) == list:
            raise TypeError
        self.__matrix = copy.deepcopy(data)
              
    def __repr__(self):
        maxi = - float('INF')
        for elem in self.__matrix:
            for num in elem:
                if len(str(num)) > maxi:
                    maxi = len(str(num))
        s = []
        a = '{:' + str(maxi  + 1) + '}'
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
    
    def __add__(self, other):
        n, m = check_size(self.__matrix, other)
        new = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                new[i][j] = self.__matrix[i][j] + other[i][j]
        return new
    
    def __sub__(self, other):
        n, m = check_size(self.__matrix, other)
        new = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                new[i][j] = self.__matrix[i][j] - other[i][j]
        return new
