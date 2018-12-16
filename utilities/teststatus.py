from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.sumResults = []

    def setResults(self, result, resulMessage):
        try:
            if result is not None:
                if result is True:
                    self.sumResults.append("PASS")
                    self.log.info(" VERIFICATION SUCCESFULL + " + resulMessage)
                else:
                    self.sumResults.append("FAIL")
                    self.log.info(" VERIFICATION FAILS + " + resulMessage)
                    self.takeScreenshot(resulMessage)
            else:
                self.sumResults.append("FAIL")
                self.log.info(" VERIFICATION FAILS + " + resulMessage)
                self.takeScreenshot(resulMessage)
        except:
            self.sumResults.append("FAIL")
            self.log.info("EXEPTION OCCURED")
            print_stack()

    def mark(self, result, resulMessage):
        """"
        mark the result of the vericitaion point in a test case
        """
        self.setResults(result, resulMessage)

    def finalMark(self, testName, result, resulMessage):
        self.setResults(result, resulMessage)

        if "FAIL" in self.sumResults:
            self.log.error(testName + " ### TEST FAILED ")
            self.sumResults.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST PASSED ")
            self.sumResults.clear()
            assert True == True
