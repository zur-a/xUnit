from src.TestResult import TestResult


class TestCase:

    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()

    def setUp(self):
        pass

    def tearDown(self):
        pass
