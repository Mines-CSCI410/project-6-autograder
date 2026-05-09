import unittest
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

    def assertNoDiff(self, name):
        res = subprocess.run(['diff', f'/autograder/outputs/{name}.hack', f'/autograder/grader/tests/expected-outputs/{name}.hack', '-swy', '--strip-trailing-cr'], check=True, text=True, capture_output=True, timeout=30)
        if res.returncode != 0:
            raise AssertionError(f'Assembler output does not mach the expected output!\n{res.stdout}')

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
