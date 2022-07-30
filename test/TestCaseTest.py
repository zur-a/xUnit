from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def templateMethodTest(self):
        self.test.run()
        assert ("setUp testMethod " == self.test.log)


TestCaseTest("templateMethodTest").run()

