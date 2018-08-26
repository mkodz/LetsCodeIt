from selenium import webdriver

class WebdriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getwebDriverInstance(self):
        baseURL= "https://letskodeit.teachable.com"

        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
