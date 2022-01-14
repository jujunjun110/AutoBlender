import imp
import unittest
import main
import math


class TestMain(unittest.TestCase):

    def test_calc(self):
        res = main.calcTransform(4, 0, 0)
        self.assertAlmostEqual(res.pos_x, 0)
        self.assertAlmostEqual(res.pos_y, 0)
        self.assertAlmostEqual(res.pos_z, 4)
        self.assertAlmostEqual(math.degrees(res.rot_x), 0)
        self.assertAlmostEqual(math.degrees(res.rot_y), 0)
        self.assertAlmostEqual(math.degrees(res.rot_z), 90)

        root2 = math.sqrt(2)
        root3 = math.sqrt(3)

        res = main.calcTransform(4, 45, 30)
        self.assertAlmostEqual(res.pos_x, root2)
        self.assertAlmostEqual(res.pos_y, root2)
        self.assertAlmostEqual(res.pos_z, 2 * root3)
        self.assertAlmostEqual(math.degrees(res.rot_x), 30)
        self.assertAlmostEqual(math.degrees(res.rot_y), 0)
        self.assertAlmostEqual(math.degrees(res.rot_z), 135)
