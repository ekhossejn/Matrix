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
        
        len_stroka = -1
        for i in range(len(data)):
            if len_stroka == -1:
                len_stroka = len(data[0])
            elif len_stroka == len(data[i]):
                continue
            else:
                raise MatrixError('Matrix is wrong')
        self.__matrix = copy.deepcopy(data)
              
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
    
    //////////////////////////////////////////////////EX. 1 IS FINISHED///////////////////////////////////////////////////////////
    
    def __add__(self, other):
        n, m = check_size(self.__matrix, other.__matrix)
        new = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                new[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
        return MyMatrix(new)
    
    def __sub__(self, other):
        n, m = check_size(self.__matrix, other.__matrix)
        new = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                new[i][j] = self.__matrix[i][j] - other.__matrix[i][j]
        return MyMatrix(new)

    def __iadd__(self, other):
        self = self + other
        return self
        
    def __isub__(self, other):
        self = self - other
        return self
    
    def __getitem__(self, key):
        if type(key) == int:
            return self.__matrix[key]
        i, j = key
        return self.__matrix[i][j]
    
    def __setitem__(self, key, value):
        i, j = key
        self.__matrix[i][j] = value
    
    def __mul__(self, other):
        if (self.size()[0] != other.size()[1] or self.size()[1] != other.size()[0]):
            raise MatrixError('Matrixs are wrong')
        new = []
        for i in range(self.size()[0]):
            new.append([])
            for j in range(other.size()[1]):
                res = 0
                for c in range(self.size()[1]):
                    res += (self.__matrix[i][c] * other.__matrix[c][j])
                new[i].append(res)
        return MyMatrix(new)
    
    def __imul__(self, other):
        self = self * other
        return self
    
    def rotate_clockwise_90(self):
        copy1 = [[0 for i in range(self.size()[0])] for i in range(self.size()[1])]
        for i in range(self.size()[1]):
            for j in range(self.size()[0]):
                copy1[i][j] = self.__matrix[self.size()[0] - j - 1][i]
        self.__matrix = copy.deepcopy(copy1)
        
    def rotate_counterclockwise_90(self):
        for i in range(3):
            self.rotate_clockwise_90()
