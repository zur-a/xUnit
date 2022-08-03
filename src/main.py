from src.TestSuite import TestSuite
from src.TestResult import TestResult
from teste.TestCaseTest import TestCaseTest

suite = TestSuite()
suite.add(TestCaseTest("templateMethodTest"))
suite.add(TestCaseTest("resultTest"))
suite.add(TestCaseTest("failedResultTest"))
suite.add(TestCaseTest("failedResultFormattingTest"))
suite.add(TestCaseTest("suiteTest"))

result = TestResult()

suite.run(result)
print(result.summary())


