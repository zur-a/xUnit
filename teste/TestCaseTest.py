from src.TestCase import TestCase
from src.WasRun import WasRun
from src.TestResult import TestResult
from src.TestSuite import TestSuite


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()
        self.test = WasRun("testMethod")

    def templateMethodTest(self):
        self.test.run(self.result)
        assert ("setUp testMethod tearDown " == self.test.log)

    def resultTest(self):
        self.test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def failedResultTest(self):
        self.result.testFailed()
        self.test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def failedResultFormattingTest(self):
        self.result.testStarted()
        self.result.testFailed()
        self.result.testFailed()
        self.result.testFailed()
        assert("1 run, 3 failed" == self.result.summary())

    def suiteTest(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


