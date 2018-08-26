from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import os,time


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self, resultMessage):
        filename = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotsDirectory = "../screenshots/"
        relativeFilename = screenshotsDirectory + filename
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFilename)
        destinationDirectory = os.path.join(currentDirectory, screenshotsDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occured")
            print_stack()

    def getByType(self, Type):
        Type = Type.lower()
        if Type == "id":
            return By.ID
        elif Type == "name":
            return By.NAME
        elif Type == "xpath":
            return By.XPATH
        elif Type == "css":
            return By.CSS_SELECTOR
        elif Type == "classname":
            return By.CLASS_NAME
        elif Type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("does not exist")
        return False

    def getTitle(self):
        return self.driver.title

    def getElement(self, Type, locatorType):
        element = None
        try:
            Type = Type.lower()
            byType = self.getByType(Type) #BY.ID
            element = self.driver.find_element(byType, locatorType)
            self.log.info("Element found with " + Type + " and locatorType " + locatorType)

        except:
            self.log.info("Element not found with " + Type + " and locatorType " + locatorType)
        return element

    def islementPresent(self, Type, locatorType):
        try:
            element = self.getElement(Type, locatorType)
            if element is not None:
                self.log.info("element is present")
                return True
            else:
                self.log.info("element is not found")
                return False
        except:
            self.log.info("not found")
            return element

    def elmentsPrensents(self, Type, locator):
            try:
                elementList = self.driver.find_elements(Type, locator)
                if len(elementList)> 0:
                    self.log.info("elements are presents")
                    return True
                else:
                    self.log.info("elements are not found")
                    return False
            except:
                self.log.info("elements are not found")
                return elementList

    def elementClick(self, locatorType, locator):
        element = None
        try:
            element = self.getElement(locatorType, locator)
            element.click()
            self.log.info("clicked on element with locator: " + locator + " and type " + locatorType)
        except:
            self.log.info("cannot click on the element with locator: " + locator + " and type " + locatorType)
            print_stack()
        return element

    def elementSendKeys(self, data, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator + " and type " + locatorType)
        except:
            self.log.info("cannot send data on element with locator: " + locator + " and type " + locatorType)
            print_stack()

    def waitForElement(self, locatorType, locator, timeout=10, poolFrequency=0.5):
        element = None
        try:
            byTpe = self.getByType(locatorType)
            self.log.info("waiting for maximum " + str(timeout + " seconds for element to be clicable"))
            wait = WebDriverWait(self.driver, timeout=10, poolFrequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                               ElementNotVisibleException,
                                                                                               ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byTpe, locator)))
            self.log.info("element appeared on the web page")
        except:
            self.log.info("element not appeared on the web page")
            print_stack()
        return element
