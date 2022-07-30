from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):

    def runningTest(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert test.wasRun

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasSetUp