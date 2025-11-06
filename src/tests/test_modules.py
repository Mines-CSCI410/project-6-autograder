import unittest
import subprocess
from os import path

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def assertNoDiff(self, name):
        res = subprocess.call(['diff', f'/autograder/outputs/{name}.hack', f'/autograder/grader/tests/expected-outputs/{name}.hack', '-qsw', '--strip-trailing-cr'])
        if res != 0:
            raise AssertionError('Assembler output does not mach the expected output!')
        pass

class TestModules(TestBase): 
    @weight(95/7)
    @number(1)
    def test_add(self):
        self.assertNoDiff('Add')

    @weight(95/7)
    @number(2)
    def test_max(self):
        self.assertNoDiff('Max')

    @weight(95/7)
    @number(3)
    def test_maxL(self):
        self.assertNoDiff('MaxL')

    @weight(95/7)
    @number(4)
    def test_pong(self):
        self.assertNoDiff('Pong')

    @weight(95/7)
    @number(5)
    def test_pongL(self):
        self.assertNoDiff('PongL')

    @weight(95/7)
    @number(6)
    def test_rect(self):
        self.assertNoDiff('Rect')

    @weight(95/7)
    @number(6)
    def test_rectL(self):
        self.assertNoDiff('RectL')
