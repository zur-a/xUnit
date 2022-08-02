from src.TestCase import TestCase
from src.WasRun import WasRun
from src.TestResult import TestResult
from src.TestSuite import TestSuite


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
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def failedResultFormattingTest(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        result.testFailed()
        result.testFailed()
        assert("1 run, 3 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        result = suite.run()
        assert("2 run, 1 failed" == result.summary)


print(TestCaseTest("templateMethodTest").run().summary())
print(TestCaseTest("resultTest").run().summary())
print(TestCaseTest("failedResultTest").run().summary())
print(TestCaseTest("failedResultFormattingTest").run().summary())

