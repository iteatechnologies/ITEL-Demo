from TDSLBase import *
from interfaces import Selenium
from metaperms.itea_demo import META_PERM
from data.TDSLData import DS


@testcase(
    id="TC_GURU99_LOGIN_001",
    description="test login",
    objective="To verify login of test website"
)
class TC_GURU99_LOGIN_001(Base):

    @resources
    def init(self):
        self.User = Selenium(META_PERM.webTester)

    @precondition('Test Precondition')
    def precondition(self):
        self.User.get(DS.pages.login_page.url)

    @procedure('Test Procedure')
    def procedure(self):
        self.User.sendKeys(DS.pages.login_page.userInput, Selenium.SearchType.xpath, DS.credential.user)
        self.User.sendKeys(DS.pages.login_page.passInput, Selenium.SearchType.xpath, DS.credential.password)
        self.User.click(DS.pages.login_page.loginBtn, Selenium.SearchType.xpath)
        self.User.check(2, 1, Selenium.SearchType.xpath, DS.pages.home_page.welcome_banner)
        # time.sleep(10)
        # self.User.check(10,1, Selenium.SearchType.xpath, DS.successFlag)

    @postcondition('Test Post-condition')
    def postcondition(self):
        # self.User.get("http://testing-ground.scraping.pro/login")
        pass
