from TDSL.TDSLType import *
from interfaces.Selenium import Selenium
from data.TDSLData import DS


def Login(webUser: Selenium, url, userInput, userName, passInput, password, submitButton, successFlag):
    """
    When {{webUser}} login with userName: {{username}}, {{webUser}} should see the {{successFlag}}
    @param: web
    @param: userInput
    @param: passInput
    @param: username
    @param: password
    @param: submitButton
    @param: successFlag
    """
    webUser.get(url)
    webUser.sendKeys(userInput, Selenium.SearchType.xpath, userName)
    webUser.sendKeys(passInput, Selenium.SearchType.xpath, password)
    webUser.click(submitButton, Selenium.SearchType.xpath)
    webUser.check(2, 1, Selenium.SearchType.xpath, successFlag)
