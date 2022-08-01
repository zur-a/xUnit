from src.TestCase import TestCase


class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.log = self.log + "testMethod "

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokesMethod(self):
        raise Exception

