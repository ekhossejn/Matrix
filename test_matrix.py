from matrix import MyMatrix

def test_repr():
    array = [[-90, 10], [2, -2], [90, 10]]
    ans = []
    for row in array:
            ans.append(str())
            for num in row:
                ans[-1] += '{:3}'.format(num)
                ans[-1] += ' '
            ans[-1] = ans[-1][:-1] 
    sample = '\n'.join(ans)
    assert(repr(MyMatrix(array) == sample))
    assert(repr(MyMatrix([])) == '')
    
def test_size():
    mx = MyMatrix([[1], [2], [3]])
    assert(mx.size() == (3, 1))
    mx = MyMatrix([])
    assert(mx.size() == (0, 0))

def test_flip_up_down():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    mx.flip_up_down()
    assert(mx.get_data() == [[4, 5, 6], [1, 2, 3]])

def test_flip_left_right():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    mx.flip_left_right()
    assert(mx.get_data() == [[3, 2, 1], [6, 5, 4]])

def test_flipped_up_down():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(mx.flipped_up_down().get_data() == [[4, 5, 6], [1, 2, 3]])
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])

def test_flipped_left_right():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(mx.flipped_left_right().get_data() == [[3, 2, 1], [6, 5, 4]])
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])

def test_trasnpose():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    mx.transpose()
    assert(mx.get_data() == [[1, 4], [2, 5], [3, 6]])

def test_trasnposed():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(mx.transposed().get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])
