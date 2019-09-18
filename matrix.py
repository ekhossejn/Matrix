from matrix import MyMatrix

def test_init():
    matrix = [[1], [2], [3]]
    mx = MyMatrix(matrix)
    assert(mx.get_data() == [[1], [2], [3]])
    matrix.pop(-1)
    assert(mx.get_data() == [[1], [2], [3]])
    
def test_repr():
    array = [[-90, 10], [2, -2], [90, 10]]
    assert(MyMatrix(array).__repr__() == '-90  10\n  2  -2\n 90  10')
    assert(MyMatrix([]).__repr__() == '')
    
def test_size():
    mx = MyMatrix([[1], [2], [3]])
    assert(mx.size() == (3, 1))
    mx = MyMatrix([[], [], []])
    assert(mx.size() == (3, 0))

def test_flip_up_down():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    mx.flip_up_down()
    assert(mx.get_data() == [[4, 5, 6], [1, 2, 3]])
    mx.flip_up_down()
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])
    mx = MyMatrix([])
    mx.flip_up_down()
    assert(mx.get_data() == [])

def test_flip_left_right():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    mx.flip_left_right()
    assert(mx.get_data() == [[3, 2, 1], [6, 5, 4]])
    mx.flip_left_right()
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])
    mx = MyMatrix([])
    mx.flip_up_down()
    assert(mx.get_data() == [])

def test_flipped_up_down():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(mx.flipped_up_down().get_data() == [[4, 5, 6], [1, 2, 3]])
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])

def test_flipped_left_right():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(mx.flipped_left_right().get_data() == [[3, 2, 1], [6, 5, 4]])
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])

def test_transpose():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    mx.transpose()
    assert(mx.get_data() == [[1, 4], [2, 5], [3, 6]])

def test_transposed():
    mx = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(mx.transposed().get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(mx.get_data() == [[1, 2, 3], [4, 5, 6]])
