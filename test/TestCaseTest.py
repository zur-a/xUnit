from src.TestCase import TestCase
from src.WasRun import WasRun
from src.TestResult import TestResult


class TestCaseTest(TestCase):

    #def setUp(self):
        #self.test = WasRun("testMethod")

    def templateMethodTest(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)

    def resultTest(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def failedResultTest(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 1 failed", result.summary())

    def failedResultFormattingTest(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())


TestCaseTest("templateMethodTest").run()
TestCaseTest("resultTest").run()
TestCaseTest("failedResultTest").run()
TestCaseTest("failedResultFormattingTest").run()

