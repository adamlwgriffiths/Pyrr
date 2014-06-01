import unittest

class test_import(unittest.TestCase):
    def test_import_files(self):
        from pyrr import aabb
        from pyrr import aambb
        from pyrr import euler
        from pyrr import geometric_tests
        from pyrr import geometry
        from pyrr import integer
        from pyrr import line
        from pyrr import matrix33
        from pyrr import matrix44
        from pyrr import plane
        from pyrr import quaternion
        from pyrr import ray
        from pyrr import rectangle
        from pyrr import sphere
        from pyrr import trig
        from pyrr import utils
        from pyrr import vector3
        from pyrr import vector4

    def test_direct_access(self):
        import pyrr
        pyrr.aabb
        pyrr.aambb
        pyrr.euler
        pyrr.geometric_tests
        pyrr.geometry
        pyrr.integer
        pyrr.line
        pyrr.matrix33
        pyrr.matrix44
        pyrr.plane
        pyrr.quaternion
        pyrr.ray
        pyrr.rectangle
        pyrr.sphere
        pyrr.trig
        pyrr.utils
        pyrr.vector3
        pyrr.vector4

if __name__ == '__main__':
    unittest.main()
