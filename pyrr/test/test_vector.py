import unittest
import math

import numpy

from pyrr import vector, vector3, vector4


class test_vector( unittest.TestCase ):
    def test_create(self):
        vec = vector3.create()
        self.assertTrue(numpy.array_equal(vec, [0.0, 0.0, 0.0]), "Vector zeros not zeroed")
    
    def test_normalise_single_vector(self):
        vec = numpy.array([1.0, 1.0, 1.0])
        result = vector.normalise(vec)

        length = math.sqrt(numpy.sum(vec ** 2))
        expected = vec / length

        self.assertTrue(numpy.array_equal(result, expected), "Vector normalise not unit length")

    def test_normalise_batch(self):
        vec = numpy.array([1.0, 1.0, 1.0])
        batch = numpy.tile(vec, (3, 1))
        result = vector.normalise( batch )
        
        lengths = numpy.array([math.sqrt(numpy.sum(vec ** 2))])
        lengths = numpy.tile(lengths, (3,1))
        expected = batch / lengths

        self.assertTrue(numpy.array_equal(result, expected), "Batch vector normalise not unit length")

    def test_squared_length_single_vector(self):
        vec = numpy.array([1.0, 1.0, 1.0])
        result = vector.squared_length(vec)
        expected = numpy.sum(vec ** 2)
        self.assertEqual(result, expected, "Vector squared length incorrect")

    def test_squared_lenght_batch(self):
        vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
        batch = numpy.tile( vec, (3,1) )
        result = vector.squared_length( batch )

        expected = numpy.array([numpy.sum(vec ** 2)])
        expected = numpy.tile(expected, (3,))

        self.assertTrue(
            numpy.array_equal( result, expected ),
            "Vector squared length calculation incorrect"
            )

    def test_length_single_vector(self):
        vec = numpy.array([1.0, 1.0, 1.0])
        result = vector.length(vec)
        expected = math.sqrt(numpy.sum(vec ** 2))
        self.assertEqual(result, expected, "Vector length calculation incorrect")

    def test_length_batch(self):
        vec = numpy.array([1.0, 1.0, 1.0])
        batch = numpy.tile(vec, (3,1))
        result = vector.length(batch)

        expected = numpy.array([math.sqrt(numpy.sum(vec ** 2))])
        expected = numpy.tile(expected, (3,))

        self.assertTrue(numpy.array_equal(result, expected), "Vector batch length calculation incorrect")

    def test_set_length_single_vector(self):
        vec = numpy.array([1.0, 1.0, 1.0])
        length = 2.0
        result = vector.set_length(vec, length)

        current_length = numpy.array([math.sqrt(numpy.sum(vec ** 2))])
        expected = (vec / current_length) * 2.0

        self.assertTrue(numpy.array_equal(result, expected), "Vector length not set correctly")

    def test_set_length_batch_vector(self):
        vec = numpy.array( [ 1.0, 1.0, 1.0 ] )
        length = 2.0
        batch = numpy.tile( vec, (3,1) )
        result = vector.set_length( batch, length )

        current_length = numpy.array([math.sqrt(numpy.sum(vec ** 2))])
        expected = (vec / current_length) * 2.0
        expected = numpy.tile( expected, (3,1) )

        self.assertTrue(numpy.array_equal(result, expected), "Vector length not set correctly")

    def test_dot_adjacent(self):
        vec1 = numpy.array([1.0, 0.0, 0.0])
        vec2 = numpy.array([0.0, 1.0, 0.0])
        result = vector.dot(vec1, vec2)
        expected = numpy.sum(vec1 * vec2)
        assert expected == 0.0
        self.assertTrue(numpy.array_equal(result, expected), "Dot product of adjacent vectors incorrect")

    def test_dot_parallel(self):
        vec1 = numpy.array([0.0, 1.0, 0.0])
        vec2 = numpy.array([0.0, 1.0, 0.0])
        result = vector.dot(vec1, vec2)
        expected = numpy.sum(vec1 * vec2)
        assert expected == 1.0
        self.assertTrue(numpy.array_equal(result, expected), "Dot product of parallel vectors incorrect")

    def test_dot_angle(self):
        vec1 = numpy.array([1.0, 1.0, 0.0])
        vec2 = numpy.array([0.0, 1.0, 0.0])
        result = vector.dot(vec1, vec2)
        expected = numpy.sum(vec1 * vec2)
        self.assertTrue(numpy.array_equal(result, expected), "Dot product of angled vectors incorrect")

    def test_dot_batch(self):
        vecs1 = numpy.array([
            # adjacent
            [1.0, 0.0, 0.0],
            # parallel
            [0.0, 1.0, 0.0],
            # angled
            [1.0, 1.0, 0.0]
        ])
        vecs2 = numpy.array([
            # adjacent
            [0.0, 1.0, 0.0],
            # parallel
            [0.0, 1.0, 0.0],
            # angled
            [0.0, 1.0, 0.0]
        ])
        result = vector.dot(vecs1, vecs2)
        expected = numpy.sum(vecs1 * vecs2, axis=-1)
        self.assertTrue(numpy.array_equal(result, expected), "Vector dot calculation incorrect")

    def test_cross_single_vector(self):
        vec1 = numpy.array([1.0, 0.0, 0.0])
        vec2 = numpy.array([0.0, 1.0, 0.0])

        result = vector.cross(vec1, vec2)

        expected = numpy.cross(vec1, vec2)
        self.assertTrue(numpy.array_equal(result, expected), "Vector cross product incorrect")

    def test_cross_batch(self):
        vec1 = numpy.array([1.0, 0.0, 0.0])
        vec2 = numpy.array([0.0, 1.0, 0.0])
        batch1 = numpy.tile(vec1, (3,1))
        batch2 = numpy.tile(vec2, (3,1))

        result = vector.cross(batch1, batch2)

        expected = numpy.cross(vec1, vec2)
        expected = numpy.tile(expected, (3,1))

        self.assertTrue(numpy.array_equal(result, expected), "Vector cross product incorrect")

    def test_interoplation( self ):
        vec1 = numpy.array([0.0, 0.0, 0.0])
        vec2 = numpy.array([1.0, 1.0, 1.0])
        result = vector.interpolate(vec1, vec2, 0.5)
        expected = numpy.array([0.5, 0.5, 0.5])
        self.assertTrue(numpy.array_equal(result, expected), "Interoplation value incorrect")

    
if __name__ == '__main__':
    unittest.main()
