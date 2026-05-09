import unittest
import os
import subprocess

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def runStudentCode(self, name):
        try:
            process = subprocess.run(['./run_student_code.sh', f'{name}.asm'], check=True, text=True, capture_output=True, timeout=30)
            print(f'{process.stdout.strip()}\n{process.stderr.strip()}'.strip())
        except subprocess.CalledProcessError as err:
            error_message = str(err.stderr).strip()
            raise AssertionError(f'Unable to run student code on {name}.asm: "{error_message}"\n{err.stdout}'.strip())
        except subprocess.TimeoutExpired as err:
            raise TimeoutError(f'Student code timed out after {err.timeout} seconds:\n{str(err.stdout).strip()}')

    def assertDiffMatch(self, name):
        res = subprocess.call(['diff', f'/autograder/grader/tests/expected-outputs/{name}.hack', f'/autograder/source/{name}.hack', '-w', '--strip-trailing-cr'])
        if res == 1:
            diff = subprocess.check_output(['/bin/sh', '-c', f'diff /autograder/grader/tests/expected-outputs/{name}.hack /autograder/source/{name}.hack -w --strip-trailing-cr ; exit 0'], text=True)
            print(f'Files differ!\n{diff}')
            raise AssertionError(f'Student\'s HACK did not match the provided HACK file!')
        elif res > 1:
            raise AssertionError(f'Unable to diff output HACK with expected!')

    def assertFileExists(self, path):
        if not os.path.isfile(path):
            raise AssertionError(f'File "{path}" does not exist!')


    def assertCorrectAssemble(self, name):
        self.runStudentCode(name)
        self.assertFileExists(f'/autograder/source/{name}.hack')
        self.assertDiffMatch(name)

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
