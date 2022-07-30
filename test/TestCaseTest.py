from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):

    #def setUp(self):
        #self.test = WasRun("testMethod")

    def templateMethodTest(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod " == test.log)


TestCaseTest("templateMethodTest").run()

