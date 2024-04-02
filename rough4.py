from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import allure


class Test_Payever:
    startTime = time.time()
    service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()

    '''get the url'''
    driver.get(f"https://commerceos.staging.devpayever.com/registration/fashion")
    time.sleep(1)


    @allure.severity(allure.severity_level.MINOR)
    @allure.title("User Info Steps")
    @allure.tag("Pre-test steps")
    @allure.step("1. Land on the URL. "
                 "2. Click on the first name."
                 "3. Enter first name. "
                 "4. Click on the last name. "
                 "5. Enter the last name. "
                 "6. Click on user email. "
                 "7. Enter user email. "
                 "8. Click on password. "
                 "9. Enter password. "
                 "10. Click on confirm password. "
                 "11. Enter confirm password. "
                 "12. Click on submit. ")
    def test_userdetail(self):
        ''' Fill out the user info '''

        time.sleep(5)
        # click on first name
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/two-column-form/div/peb-form-field-input[1]/div/div/span").click()
        # enter user first name
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/two-column-form/div/peb-form-field-input[1]/div/div/div/input").send_keys("test001")

        time.sleep(2)

        # click  user last name
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/two-column-form/div/peb-form-field-input[2]/div/div/span").click()

        # enter user last name
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/two-column-form/div/peb-form-field-input[2]/div/div/div/input").send_keys("test001")

        time.sleep(2)

        # click on user email
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/peb-form-field-input[1]/div/div/span").click()

        # enter user Email
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/peb-form-field-input[1]/div/div/div/input[1]").send_keys("test007@mail.com")

        time.sleep(2)
        # click on password
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/peb-form-field-input[2]/div/div/span").click()

        # enter password
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/peb-form-field-input[2]/div/div/div/input[1]").send_keys("Password@91")

        time.sleep(2)

        # click on confirm password
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/peb-form-field-input[3]/div/div/span").click()

        # confirm password
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/peb-form-background/div/peb-form-field-input[3]/div/div/div/input[1]").send_keys("Password@91")

        # click on submit
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-create-personal-form/form/div[2]/button[1]").click()


    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Business Info Steps")
    @allure.tag("Pre-test steps")
    @allure.step("1. Click on the company name. "
                 "2. Enter the company name. "
                 "3. Click on number. "
                 "4. Enter Number. "
                 "5. Click on Start with Payever. "
                 "6. Click on Get started. ")
    def test_companydetails(self):
        ''' Fill out bussiness information'''

        time.sleep(5)

        # click on the company name
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-default-business-registration/entry-create-business-form/form/peb-form-background/div/peb-form-field-input/div/div/span").click()

        # Enter company name
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-default-business-registration/entry-create-business-form/form/peb-form-background/div/peb-form-field-input/div/div/div/input").send_keys("CompanyName")

        time.sleep(2)

        # click on enter number
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-default-business-registration/entry-create-business-form/form/peb-form-background/div/two-column-form/div/peb-form-field-input/div/div/span").click()

        # enter number
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-default-business-registration/entry-create-business-form/form/peb-form-background/div/two-column-form/div/peb-form-field-input/div/div/div/input").send_keys("12341231")

        time.sleep(2)
        # click on Get starter with payever
        self.driver.find_element(By.XPATH,"//*[@id='layout-container']/div/entry-default-business-registration/button").click()

        time.sleep(7)

        # click on get started
        self.driver.find_element(By.CLASS_NAME,"welcome-screen-content-button").click()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Validating Checkout Option")
    @allure.tag("user dashboard","fashion")
    @allure.step("1. Validate the presence of the checkout option by verifying the presence of the checkout section element. "
                 "2. If the element is present then it will get the text shown in this section and then validate with the text 'Checkout'. "
                 "3. Either the checkout section element or the text element is not present or the text is not what is expected then it will fail the case. ")
    def test_001(self):
        ''' To verify the presence of the checkout option. '''

        # check for checkout

        try:
            self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[1]")
        except NoSuchElementException:
            assert False
        else:
            name = self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[1]/div[2]").text
            if name == "Checkout":
                assert True
            else:
                assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Validate Transaction Option")
    @allure.tag("user dashboard","fashion")
    @allure.step(
        "1. Validate the presence of the Transaction option by verifying the presence of the Transaction section element. "
        "2. If the element is present then it will get the text shown in this section and then validate with the text 'Transaction'. "
        "3. Either the Transaction section element or the text element is not present or the text is not what is expected then it will fail the case. ")
    def test_002(self) :
        ''' To verify the presence of Transaction option. '''
        try:
            self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[4]")
        except NoSuchElementException:
            assert False
        else:
            name = self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[4]/div[2]").text
            if name == "Transactions":
                assert True
            else:
                assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Validate Connect Option")
    @allure.tag("user dashboard","fashion")
    @allure.step(
        "1. Validate the presence of the Connect option by verifying the presence of the Connect section element. "
        "2. If the element is present then it will get the text shown in this section and then validate with the text 'Connect'. "
        "3. Either the Connect section element or the text element is not present or the text is not what is expected then it will fail the case. ")
    def test_003(self):
        ''' To verify the presence of Connct option. '''
        try:
            self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[2]")
        except NoSuchElementException:
            assert False
        else:
            name = self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[2]/div[2]").text
            if name == "Connect":
                assert True
            else:
                assert False


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Validate Product Option")
    @allure.tag("user dashboard","fashion")
    @allure.step(
        "1. Validate the presence of the Product option by verifying the presence of the Product section element. "
        "2. If the element is present then it will get the text shown in this section and then validate with the text 'Product'. "
        "3. Either the Product section element or the text element is not present or the text is not what is expected then it will fail the case. ")
    def test_004(self):

        ''' To verify the presence of Product option. '''
        try:
            self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[3]")
        except NoSuchElementException:
            assert False
        else:
            name = self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[3]/div[2]").text
            if name == "Products":
                assert True
            else:
                assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Validate Shop Option")
    @allure.tag("user dashboard","fashion")
    @allure.step(
        "1. Validate the presence of the Shop option by verifying the presence of the Shop section element. "
        "2. If the element is present then it will get the text shown in this section and then validate with the text 'Shop'. "
        "3. Either the Shop section element or the text element is not present or the text is not what is expected then it will fail the case. ")
    def test_005(self):

        ''' To verify the presence of Shop option. '''
        try:
            self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[6]")
        except NoSuchElementException:
            assert False
        else:
            name = self.driver.find_element(By.XPATH,"/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[6]/div[2]").text
            if name =="Shop":
                assert True
            else:
                assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Validate Settings Option")
    @allure.tag("user dashboard","fashion")
    @allure.step(
        "1. Validate the presence of the Settings option by verifying the presence of the Settings section element. "
        "2. If the element is present then it will get the text shown in this section and then validate with the text 'Settings'. "
        "3. Either the Settings section element or the text element is not present or the text is not what is expected then it will fail the case. ")
    def test_006(self):
        ''' To verify the presence of Settings option. '''
        try:
            self.driver.find_element(By.XPATH,
                                     "/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[17]")
        except NoSuchElementException:
            assert False
        else:
            name = self.driver.find_element(By.XPATH,
                                            "/html/body/app-root/app-lazy/user-dashboard/base-dashboard/div/div/div/widgets-layout/div/div/apps-widget/pe-widget/div/div/div[1]/div[2]/pe-widget-icons/div/div/div/div[17]/div[2]").text
            if name == "Settings":
                assert True
            else:
                print(name)
                assert False

