import numpy as np


class Tensor(object):
    
    def __init__(self, array):
        self.array = np.array(array)
        self.shape = np.shape(self.array)
        self.size = np.size(self.array)

    def __mul__(self, other):
        return self.array * other.array

    def __and__(self, arg):
        return [self, arg]

    def __matmul__(self, other: list):
        """
        This is an overloaded standard operator __matmul__, @ , 
        it now calculates tensor product using the numpy.tensordot method.
        This method offers several variants of tensor products, for which 
        the variable axes must be added (details: numpy.tensordot) 
        Another method __and__() has been overloaded to be able to implement
        this variable when using the operator

        Final entry
        -------------------
        b = t @ (e & axes)

        About axes
        ------------
        Three common use cases are:
        * ``axes = 0`` : tensor product :math:`a\\otimes b`
        * ``axes = 1`` : tensor dot product :math:`a\\cdot b`
        * ``axes = 2`` : (default) tensor double contraction :math:`a:b`

        When `axes` is integer_like, the sequence for evaluation will be: first
        the -Nth axis in `a` and 0th axis in `b`, and the -1th axis in `a` and
        Nth axis in `b` last.

        :param other: [other: Tensor, axes]
        :return: b = t @ (e & axes)

        Examples
        --------
        A specific concatenation example, but it perfectly illustrates the principle of a tensor product:

            >>> a = [
            ...        [[5, 6, 7],
            ...         [6, 0, 5],
            ...         [5, 6, 55]],
            ...        [[1, 6, 8],
            ...         [5, 6, 55],
            ...         [42, 9, 5]]
            ...        ]
            >>> A = np.array([
            ...        ['a', 'b'],
            ...        ['f', 'c'],
            ...        ['e', 'd'],
            ...        ],  
            ...        dtype=object)
            >>> # Create two instances of the class for multiplication...
            >>> tens_a = Tensor(a)
            >>> tens_b = Tensor(A)
            >>> # Apply operators, '&' removed in brackets for clear consistency and logic
            >>> result = tens_a @ (tens_b & 0)
            >>> print(result)
            [[[[['aaaaa' 'bbbbb']
                ['fffff' 'ccccc']
                ['eeeee' 'ddddd']]

            [['aaaaaa' 'bbbbbb']
                ['ffffff' 'cccccc']
                ['eeeeee' 'dddddd']]

            [['aaaaaaa' 'bbbbbbb']
                ['fffffff' 'ccccccc']
                ['eeeeeee' 'ddddddd']]]


            [[['aaaaaa' 'bbbbbb']
                ['ffffff' 'cccccc']
                ['eeeeee' 'dddddd']]

            [['' '']
                ['' '']
                ['' '']]

            [['aaaaa' 'bbbbb']
                ['fffff' 'ccccc']
                ['eeeee' 'ddddd']]]


            [[['aaaaa' 'bbbbb']
                ['fffff' 'ccccc']
                ['eeeee' 'ddddd']]

            [['aaaaaa' 'bbbbbb']
                ['ffffff' 'cccccc']
                ['eeeeee' 'dddddd']]

            [['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
                ['fffffffffffffffffffffffffffffffffffffffffffffffffffffff'
                'ccccccccccccccccccccccccccccccccccccccccccccccccccccccc']
                ['eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddd']]]]



            [[[['a' 'b']
                ['f' 'c']
                ['e' 'd']]

            [['aaaaaa' 'bbbbbb']
                ['ffffff' 'cccccc']
                ['eeeeee' 'dddddd']]

            [['aaaaaaaa' 'bbbbbbbb']
                ['ffffffff' 'cccccccc']
                ['eeeeeeee' 'dddddddd']]]


            [[['aaaaa' 'bbbbb']
                ['fffff' 'ccccc']
                ['eeeee' 'ddddd']]

            [['aaaaaa' 'bbbbbb']
                ['ffffff' 'cccccc']
                ['eeeeee' 'dddddd']]
    
            [['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
                ['fffffffffffffffffffffffffffffffffffffffffffffffffffffff'
                'ccccccccccccccccccccccccccccccccccccccccccccccccccccccc']
                ['eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddd']]]


            [[['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
                ['ffffffffffffffffffffffffffffffffffffffffff'
                'cccccccccccccccccccccccccccccccccccccccccc']
                ['eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                'dddddddddddddddddddddddddddddddddddddddddd']]

            [['aaaaaaaaa' 'bbbbbbbbb']
                ['fffffffff' 'ccccccccc']
                ['eeeeeeeee' 'ddddddddd']]

            [['aaaaa' 'bbbbb']
                ['fffff' 'ccccc']
                ['eeeee' 'ddddd']]]]]

        A more classic example from the numpy documentation:

            >>> a = np.arange(60.).reshape(3,4,5)
            >>> b = np.arange(24.).reshape(4,3,2)
            >>> c = np.tensordot(a,b, axes=([1,0],[0,1]))
            >>> c.shape
            (5, 2)
            >>> b
            array([[ 4400.,  4730.],
                [ 4532.,  4874.],
                [ 4664.,  5018.],
                [ 4796.,  5162.],
                [ 4928.,  5306.]])
            >>> # A slower but equivalent way of computing the same...
            >>> d = np.zeros((5,2))
            >>> for i in range(5):
            ...   for j in range(2):
            ...     for k in range(3):
            ...       for n in range(4):
            ...         d[i,j] += a[k,n,i] * b[n,k,j]
            >>> b == d
            array([[ True,  True],
                [ True,  True],
                [ True,  True],
                [ True,  True],
                [ True,  True]])
        """
        return np.tensordot(a=self.array, b=other[0].array, axes=other[1])
