from TDSLBase import *
from interfaces import Selenium
from metaperms.itea_demo import META_PERM
from data.TDSLData import DS
from hlfs import web


@testcase(
    id="TC_GURU99_LOGIN_002",
    description="test login with HLF",
    objective="To verify login of test website"
)
class TC_GURU99_LOGIN_001(Base):

    @resources
    def init(self):
        self.User = Selenium(META_PERM.webTester)

    @procedure('Test Procedure')
    def procedure(self):
        web.Login(self.User,
                  url=DS.pages.login_page.url,
                  userInput=DS.pages.login_page.userInput,
                  userName=DS.credential.user,
                  passInput=DS.pages.login_page.passInput,
                  password=DS.credential.password,
                  submitButton=DS.pages.login_page.loginBtn,
                  successFlag=DS.pages.home_page.welcome_banner
                  )

        self.User.get("http://testing-ground.scraping.pro/login")
