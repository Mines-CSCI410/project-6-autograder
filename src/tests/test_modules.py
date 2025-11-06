import unittest
import subprocess
from os import path

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def runStudentCode(self, name):
        res = subprocess.call(['./run_student_code.sh', f'{name}.asm'])
        if res != 0:
            raise AssertionError(f'Unable to run student\'s assembler on {name}.asm!')

    def assertNoDiff(self, name):
        res = subprocess.call(['diff', f'/autograder/outputs/{name}.hack', f'/autograder/grader/tests/expected-outputs/{name}.hack', '-qsw', '--strip-trailing-cr'])
        if res != 0:
            raise AssertionError('Assembler output does not mach the expected output!')

    def runTest(self, name):
        self.runStudentCode(name)
        self.assertNoDiff(name)

class TestModules(TestBase): 
    @weight(95/7)
    @number(1)
    def test_add(self):
        self.runTest('Add')

    @weight(95/7)
    @number(2)
    def test_max(self):
        self.runTest('Max')

    @weight(95/7)
    @number(3)
    def test_maxL(self):
        self.runTest('MaxL')

    @weight(95/7)
    @number(4)
    def test_pong(self):
        self.runTest('Pong')

    @weight(95/7)
    @number(5)
    def test_pongL(self):
        self.runTest('PongL')

    @weight(95/7)
    @number(6)
    def test_rect(self):
        self.runTest('Rect')

    @weight(95/7)
    @number(6)
    def test_rectL(self):
        self.runTest('RectL')
