import unittest
import numpy as np
from pyrr import vector, vector3, vector4


class test_vector(unittest.TestCase):
    def test_normalise_single_vector(self):
        result = vector.normalise([1.,1.,1.])
        np.testing.assert_almost_equal(result, [0.57735, 0.57735, 0.57735], decimal=5)

    def test_normalise_batch(self):
        vec = np.array([1.,1.,1.])
        batch = np.tile(vec, (3,1))
        result = vector.normalise([
            [1.,1.,1.],
            [-1.,-1.,-1.],
            [0.,2.,7.],
        ])
        expected = [
            [0.57735, 0.57735, 0.57735],
            [-0.57735,-0.57735,-0.57735],
            [0., 0.274721, 0.961524],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_squared_length_single_vector(self):
        result = vector.squared_length([1.,1.,1.])
        np.testing.assert_almost_equal(result, 3., decimal=5)

    def test_squared_length_batch(self):
        result = vector.squared_length([
            [1.,1.,1.],
            [-1.,-1.,-1.],
            [0.,2.,7.],
        ])
        expected = [
            3.,
            3.,
            53.,
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_length_single_vector(self):
        result = vector.length([1.,1.,1.])
        np.testing.assert_almost_equal(result, 1.73205, decimal=5)

    def test_length_batch(self):
        result = vector.length([
            [1.,1.,1.],
            [-1.,-1.,-1.],
            [0.,2.,7.],
        ])
        expected = [
            1.73205,
            1.73205,
            7.28011,
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_set_length_single_vector(self):
        result = vector.set_length([1.,1.,1.],2.)
        expected = [1.15470,1.15470,1.15470]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_set_length_batch_vector(self):
        result = vector.set_length([
            [1.,1.,1.],
            [-1.,-1.,-1.],
            [0.,2.,7.],
            ], 2.0)
        expected = [
            [1.15470,1.15470,1.15470],
            [-1.15470,-1.15470,-1.15470],
            [0.,0.54944,1.92304],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_dot_adjacent(self):
        result = vector.dot([1.,0.,0.], [0.,1.,0.])
        np.testing.assert_almost_equal(result, 0.0, decimal=5)

    def test_dot_parallel(self):
        result = vector.dot([0.,1.,0.], [0.,1.,0.])
        np.testing.assert_almost_equal(result, 1.0, decimal=5)

    def test_dot_angle(self):
        result = vector.dot([.2,.2,0.], [2.,-.2,0.])
        np.testing.assert_almost_equal(result, 0.36, decimal=5)

    def test_dot_batch(self):
        result = vector.dot([
            [1.,0.,0.],
            [0.,1.,0.],
            [.2,.2,0.]
        ],[
            [0.,1.,0.],
            [0.,1.,0.],
            [2.,-.2,0.]
        ])
        expected = [0.,1.,0.36]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_cross_single_vector(self):
        result = vector.cross([1.,0.,0.], [0.,1.,0.])
        np.testing.assert_almost_equal(result, [0.,0.,1.], decimal=5)

    def test_cross_batch(self):
        result = vector.cross([
            [1.,0.,0.],
            [0.,0.,1.]
        ],[
            [0.,1.,0.],
            [0.,1.,0.],
        ])
        expected = [
            [0.,0.,1.],
            [-1.,0.,0.],
        ]
        np.testing.assert_almost_equal(result, expected, decimal=5)

    def test_interoplation( self ):
        result = vector.interpolate([0.,0.,0.], [1.,1.,1.], 0.5)
        np.testing.assert_almost_equal(result, [.5,.5,.5], decimal=5)

        result = vector.interpolate([0.,0.,0.], [2.,2.,2.], 0.5)
        np.testing.assert_almost_equal(result, [1.,1.,1.], decimal=5)

    
if __name__ == '__main__':
    unittest.main()
