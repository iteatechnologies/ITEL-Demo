from TDSL.TDSLType import *


class DS(DATA_Base):
    class credential:
        password = "UqebyhU"
        user = "mngr230461"

    class pages:
        class login_page:
            url = "http://demo.guru99.com/V4/index.php"
            resetBtn = "//input[@name=\'btnReset\']"
            loginBtn = "//input[@name=\'btnLogin\']"
            userInput = "//input[@name=\'uid\']"
            passInput = "//input[@name=\'password\']"

        class home_page:
            welcome_banner = "//marquee[contains(text(),\'Welcome\')]"

        class newCustomer:
            url = "http://demo.guru99.com/V4/manager/addcustomerpage.php"

        login_page = login_page()
        home_page = home_page()
        newCustomer = newCustomer()

    credential = credential()
    pages = pages()
