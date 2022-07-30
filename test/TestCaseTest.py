from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

    def runningTest(self):
        self.test.run()
        assert(self.test.wasRun)

TestCaseTest("runningTest").run()