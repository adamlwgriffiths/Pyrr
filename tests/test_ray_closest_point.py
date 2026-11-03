import numpy as np
import pytest

from pyrr import geometric_tests


@pytest.mark.parametrize('direction', [[1., 0., 0.], [0., -1., 0.], [0., 0., 1.]])
@pytest.mark.parametrize('distance', [-3., 0., 4.])
def test_closest_point_is_on_forward_ray(direction, distance):
    origin = np.array([2., 3., 4.])
    direction = np.asarray(direction)
    perpendicular = np.roll(direction, 1)
    point = origin + distance * direction + 2 * perpendicular
    ray = np.array([origin, direction])
    expected = origin + max(0., distance) * direction
    result = geometric_tests.point_closest_point_on_ray(point, ray)
    np.testing.assert_allclose(result, expected)
