from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -------------------------------------------------------
# Us Bank Business Altitude Connect World Elite Mastercard
# -------------------------------------------------------

def altitudeConnectWorldEliteMastercard(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "ein": 786754356,
        #         "legalBusinessName": "AAAC",
        #         "country": "IN",
        #         "businessYear": 2000,
        #         "naics": 517810,
                
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "membershipNumber": 456836297456,
        #         "housingStatus": "own",
        #         "grossIncome": 546843,
        #         "annualIncome": 546843,
        #         "monthlymortage": 546,
        #         "mobileNumber": 7349303040,
        #         "businessMobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "employmentType": "full-time",
        #         "state": 'AK',
        #         "zipcode": 99501,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        # product_id = "668fb416133bed94c15bad51"

        driver.get(
            "https://onboarding.usbank.com/usl/business/usb-credit-card/application/business-information?locationCode=18569&offerId=2X1422B7WD&sourceCode=84669&machineType=usbank&preparerType=customer"
        )

        # send_click(
        #     driver, '/html/body/div[1]/div/div[1]/div/div/header/div[3]/div[2]/div/div[2]/div[1]/div[3]/a')
        random_sleep(15)
        # driver.switch_to.window(driver.window_handles[-1])

        ein = data.get("personal").get("ein")
        legalBusinessName = data.get("personal").get("legalBusinessName")
        BusinessNameOnCard = data.get("personal").get("BusinessNameOnCard")
        country = data.get("personal").get("country")
        naics = data.get("personal").get("naics")
        membershipNumber = data.get("personal").get("membershipNumber")
        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        ssn = data.get("personal").get("ssn")
        annualIncome = data.get("personal").get("annualIncome")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        mobileNumber = data.get("personal").get("mobileNumber")
        monthlymortage = data.get("personal").get("monthlyPayment")
        authorizing = data.get("personal").get("authorizing")
        middleName = data.get("personal").get("middleName")
        suffix = data.get("personal").get("suffix")
        dob = data.get("personal").get("dob")
        motherMaidenName = data.get("personal").get("motherMaidenName")
        homeAddress = data.get("personal").get("homeAddress")
        email = data.get("email")
        grossIncome = data.get("personal").get("householdIncome")
        employmentType = data.get("personal").get("employmentType")
        residencyStatus = data.get("personal").get("housingStatus")
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}

        employmentTypeDict = {
            "full-time": "EMPLOYED",
            "part-time": "EMPLOYED",
            "freelance": "EMPLOYED",
            "internship": "EMPLOYED",
        }

        # if not firstName or not lastName or not dob or not motherMaidenName or not ssn or not homeAddress or not city or not zipcode or not state or not email or not mobileNumber or not residencyStatus or not grossIncome:
        #     raise Exception("Missing personal data.")
        random_sleep(20)

        count = 0

        random_sleep(1)

        # Business structure
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="select_businessType"]'
                )
                select = Select(select_element)
                select.select_by_value('CORP')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        random_sleep(1)

        # Employer Identification Number (EIN)
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_taxIdentifier"]',
            ein
        )

        # legalBusinessName
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_legalBusinessname"]',
            legalBusinessName
        )

        # Business name to appear on card
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_businessNameOnCard"]',
            BusinessNameOnCard
        )

        # Country
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="select_countryOfFormation"]'
                )
                select = Select(select_element)
                select.select_by_value(country)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # year Business Started
        random_sleep(1)
        businessYear = data.get("personal").get("businessYear")
        write_delay(
            driver,
            '//*[@id="input_dateOfEstablishment"]',
            businessYear
        )

        # Email
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_email"]',
            email
        )

        # Phone number
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_phoneNumber"]',
            mobileNumber
        )

        # Business Number
        random_sleep(1)
        businessMobileNumber = data.get("personal").get("businessMobileNumber")
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_businessPhoneNumber"]',
            businessMobileNumber
        )

        # Gross Annual
        write_delay(
            driver,
            '//*[@id="input_grossAnnualSales"]',
            grossIncome
        )

        # Continue
        send_click(
            driver,
            '//*[@id="business-type-button"]'
        )

        # -------------------
        # Page - 2
        # -------------------
        
        random_sleep(1)
        write_delay(
            driver, '//*[@id="input_business-address-collectionaddress1"]', homeAddress)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='streetAddress']").send_keys(Keys.TAB)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="#apartmentNumber-blx-residentialAddressBlock-text-validate-input-field").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="input_business-address-collectionzipCode"]', 
            zipcode
        )

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='zipCode']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="input_business-address-collectioncity"]', 
            city, clear=True)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='cityId']").send_keys(Keys.TAB)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, value='//*[@id="select_business-address-collectionstate"]')
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        
        # Save and continue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="submitButton"]'
        )
        
        # ----------------------------
        # Page - 3
        # ----------------------------

        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="input-68d2542a-44ea-48bc-93fa-b41a2006c574"]', 
            naics
        )
        
        # Save and continue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="primary-large"]'
        )
        
        
        # ---------------------
        # Page - 4
        # ---------------------
        
        # First Name
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_firstName"]',
            firstName
        )

        # random_sleep(1)
        # if len(middleName):
        #     write_delay(
        #         driver, '//*[@id="blx-nameBlock-middleName-text-validate-input-field"]', middleName)
        #     random_sleep(1)
        #     # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
        #     random_sleep(1)
        # else:
        #     print("Middle name not provided. Skipping...")
       
        # Last name
        write_delay(
            driver, '//*[@id="input_lastName"]', 
            lastName
        )
        random_sleep(1)
        
        # Save and continue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="submitButton"]'
        )
        
        # --------------------
        # Page -5
        # --------------------
        
        # driver.find_element(by=By.XPATH, value="//input[@name='lastName']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="input_dateOfBirth"]', 
            dob
        )
        random_sleep(1)
        
        # SSN Number
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="input_ssn"]', 
            ssn
        )
        
        # Same Address
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="wrapper_address-checkbox"]/label'
        )
        
        # annual Income Number
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="input_annualIncome"]', 
            grossIncome
        )
        
        # Save and continue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="primary-large"]'
        )
        
        # --------------------
        # Page - 6
        # --------------------
        
        # Business-owner type
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, value='//*[@id="select_businessOwnerType"]')
                select = Select(select_element)
                select.select_by_value('owner')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        
        # Checkbox
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="isSoleOwnerChoice1"]'
        )
        
        # Contniue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="primary-large"]'
        )
        
        # ---------------------
        # Page - 7
        # ---------------------
        # Checkbox
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="addEmployeeCardsChoice2"]'
        )
        
        # Contniue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="primary-large"]'
        )
        
        # ---------------------
        # Page - 8
        # ---------------------
        
        # Checkbox
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="billingOptionTypeChoice1"]'
        )
        
        # Contniue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="saveAndContinue"]'
        )
        
        # ---------------------
        # Page - 9
        # ---------------------
        # Checkbox
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="prebt-radio-groupChoice2"]'
        )
        
        # Contniue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="saveAndContinue"]'
        )
        
        # ---------------------
        # Page - 10
        # ---------------------
        
        # Contniue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="submitButton"]'
        )
        
        # ---------------------
        # Page - 11
        # ---------------------
        # Contniue
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="primary-large"]'
        )

        random_sleep(10)
        random_sleep(1)


        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Us Bank Business Altitude Connect World Elite Mastercard"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Us Bank Business Altitude Connect World Elite Mastercard"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
