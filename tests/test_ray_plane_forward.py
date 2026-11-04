import unittest
import numpy as np
from pyrr import geometric_tests, plane, ray


class TestForwardPlaneIntersection(unittest.TestCase):
    def test_rejects_intersections_behind_ray(self):
        for normal in [[0.0, 0.0, 1.0], [0.0, 0.0, -1.0]]:
            surface = plane.create_from_position([0.0, 0.0, 2.0], normal)
            for front_only in [False, True]:
                result = geometric_tests.ray_intersect_plane(
                    ray.create([1.0, 3.0, 4.0], [0.0, 0.0, 1.0]),
                    surface,
                    front_only=front_only,
                )
                self.assertIsNone(result)

    def test_forward_and_origin_intersections_are_retained(self):
        surface = plane.create_from_position([0.0, 0.0, 2.0], [0.0, 0.0, 1.0])
        for height in [2.0, 4.0]:
            for front_only in [False, True]:
                result = geometric_tests.ray_intersect_plane(
                    ray.create([1.0, 3.0, height], [0.0, 0.0, -1.0]),
                    surface,
                    front_only=front_only,
                )
                np.testing.assert_allclose(result, [1.0, 3.0, 2.0])

    def test_parallel_ray_still_has_no_intersection(self):
        self.assertIsNone(
            geometric_tests.ray_intersect_plane(
                ray.create([0.0, 0.0, 1.0], [1.0, 0.0, 0.0]), plane.create_xy()
            )
        )
