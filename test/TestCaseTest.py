from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def setUpTest(self):
        self.test.run()
        assert ("setUp " == self.test.log)

    def runningTest(self):
        self.test.run()
        assert self.test.wasRun

TestCaseTest("setUpTest").run()
TestCaseTest("runningTest").run()
