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

    def assertCorrectAssemble(self, name):
        self.runStudentCode(name)
        self.assertNoDiff(name)

class TestModules(TestBase): 
    @weight(95/7)
    @number(1)
    def test_add(self):
        self.assertCorrectAssemble('Add')

    @weight(95/7)
    @number(2)
    def test_max(self):
        self.assertCorrectAssemble('Max')

    @weight(95/7)
    @number(3)
    def test_maxL(self):
        self.assertCorrectAssemble('MaxL')

    @weight(95/7)
    @number(4)
    def test_pong(self):
        self.assertCorrectAssemble('Pong')

    @weight(95/7)
    @number(5)
    def test_pongL(self):
        self.assertCorrectAssemble('PongL')

    @weight(95/7)
    @number(6)
    def test_rect(self):
        self.assertCorrectAssemble('Rect')

    @weight(95/7)
    @number(6)
    def test_rectL(self):
        self.assertCorrectAssemble('RectL')
