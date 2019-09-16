from Class import MyMatrix

def test_repr():
    array = [[-90, 10], [2, -2], [90, 10]]
    a = MyMatrix([[-90, 10], [2, -2], [90, 10]])
    ans = []
    for elem in array:
            ans.append(str())
            for num in elem:
                ans[-1] += '{:4}'.format(num)
    test = '\n'.join(ans)
    assert(print(a) == print(test))
    
def test_size():
    a = MyMatrix([[1], [2], [3]])
    assert(a.size() == (3, 1))
    a = MyMatrix([])
    assert(a.size() == (0, 0))

def test_flip_up_down():
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    a.flip_up_down()
    assert(a.get_data() == [[4, 5, 6], [1, 2, 3]])

def test_flip_left_right():
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    a.flip_left_right()
    assert(a.get_data() == [[3, 2, 1], [6, 5, 4]])

def test_flipped_up_down():
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(a.flipped_up_down().get_data() == [[4, 5, 6], [1, 2, 3]])
    assert(a.get_data() == [[1, 2, 3], [4, 5, 6]])

def test_flipped_left_right():
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(a.flipped_left_right().get_data() == [[3, 2, 1], [6, 5, 4]])
    assert(a.get_data() == [[1, 2, 3], [4, 5, 6]])

def test_trasnpose():
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    a.transpose()
    assert(a.get_data() == [[1, 4], [2, 5], [3, 6]])

def test_trasnposed():
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(a.transposed().get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(a.get_data() == [[1, 2, 3], [4, 5, 6]])

