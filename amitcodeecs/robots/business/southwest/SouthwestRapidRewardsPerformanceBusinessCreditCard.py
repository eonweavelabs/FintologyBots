from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -------------------------------------------------------
# Southwest Rapid Rewards Performance Business Credit Card
# -------------------------------------------------------

def SouthwestRapidRewardsPerformanceBusinessCreditCard(driver, data, product_id):
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
        #         "businesslegalname": "Business Legal Name",
        #         "no_of_employees": 10,
        #         "EIN": 123456789,
        #         "businessPhoneNumber": 9876543210,
        #         "businessEstablishedDate": "01/01/2005",
        #         "annualBusinessRevenue": 1000000,
        #         "estimatedMonthlySpend": 5000,
        #         "businessDescription": "Business Description",
        #         "businessCategory": "Business Category",
        #         "percentOwnership": 50
        #     }
        # }
        # product_id = "668fb416133bed94c15bad51"

        driver.get(
            "https://secure.chase.com/web/oao/application/card?sourceCode=HJJT&action=guest&cellCode=61DS&combo=N&flowVersion=REACT&AOC=1868&RPC=0531&cfgCode=INDBIZCC#/origination/cardDetails/index/indexBusinessCreditCard"
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

        # Add more fields here
        businessMobileNumber = data.get("personal").get("businessMobileNumber")
        bonvoyNumber = data.get("personal").get("bonvoyNumber")
        businesslegalname = data.get("personal").get("businesslegalname")
        no_of_employees = data.get("personal").get("no_of_employees")
        EIN = data.get("personal").get("EIN")
        businessPhoneNumber = data.get("personal").get("businessPhoneNumber")
        businessEstablishedDate = data.get(
            "personal").get("businessEstablishedDate")
        annualBusinessRevenue = data.get(
            "personal").get("annualBusinessRevenue")
        estimatedMonthlySpend = data.get(
            "personal").get("estimatedMonthlySpend")
        businessDescription = data.get("personal").get("businessDescription")
        businessCategory = data.get("personal").get("businessCategory")
        percentOwnership = data.get("personal").get("percentOwnership")
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
        # Authorizing
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver, 
                    '//*[@id="applicant-officertitleselect"]'
                )
                random_sleep(1)
                send_click(
                    driver, 
                    '//*[@id="Owner"]'
                )
        
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="applicant-officertitleselect"]'
                # )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", select_element, 'OWNER')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # First Name
        write_delay(
            driver,
            '//*[@id="applicant-firstName"]',
            firstName
        )

        random_sleep(1)

        # Middle name
        if len(middleName):
            write_delay(
                driver,
                '//*[@id="applicant-middleName"]',
                middleName
            )
            random_sleep(1)
            # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")

        # Last name
        write_delay(
            driver,
            '//*[@id="applicant-lastName"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)

        # Date of birth
        write_delay(
            driver,
            '//*[@id="root"]/div/div[2]/div/div[3]/main/form/div/div[6]/div[2]/mds-datepicker',
            dob
        )
        random_sleep(1)
        random_sleep(1)

        # Mother name
        write_delay(
            driver,
            '//*[@id="applicant.identity.motherMaidenName-maidenName"]',
            motherMaidenName
        )
        random_sleep(1)

        # SSN Number
        write_delay(
            driver,
            '//*[@id="applicant-taxIdentifier"]',
            ssn
        )

        random_sleep(1)

        # Home address
        write_delay(
            driver,
            '//*[@id="applicant.address.0-addressLine1"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="applicant.address.0-addressPostalCode"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="applicant.address.0-addressCityName"]',
            city,
            clear=True
        )

        random_sleep(1)

        # State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="applicant.address.0-addressStateCode"]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Email
        write_delay(
            driver,
            '//*[@id="applicant-email"]',
            email
        )

        random_sleep(1)
        random_sleep(1)

        # Phone number
        write_delay(
            driver,
            '//*[@id="applicant-primaryContactPhoneNumber-0"]',
            mobileNumber
        )

        random_sleep(1)

        # Gross annual income
        write_delay(
            driver,
            '//*[@id="applicant.financialInformation.incomeDetails.0.totalAnnualIncomeAmount-genericmoneyinput"]',
            grossIncome
        )

        # Business Legal Name
        write_delay(
            driver,
            '//*[@id="business.companyName"]',
            businesslegalname
        )

        # Skip DBA Name
        send_click(
            driver,
            '//*[@id="RadioGroup-skipAppCap.DbaName"]'
        )
        random_sleep(2)
        # retry_count = 0
        # while retry_count < 600:
        #     try:
        #         select_element = driver.find_element(
        #             by=By.XPATH,
        #             value='//*[@id="RadioGroup-skipAppCap.DbaName"]'
        #         )
        #         driver.execute_script(
        #             "arguments[0].setAttribute('value',arguments[1])", select_element, False)
        #         break
        #     except:
        #         driver.execute_script("window.scrollBy(0,5)")
        #         random_sleep(0.1)
        #         retry_count += 1

        # random_sleep(1)

        # Number of Employees
        write_delay(
            driver,
            '//*[@id="business.organizationRevenueTierRangeCode-numberOfEmployees"]',
            no_of_employees
        )

        # EIN
        write_delay(
            driver,
            '//*[@id="business-taxIdentifierEin"]',
            EIN
        )

        # Same Physical Address as Personal Address
        send_click(
            driver,
            '//*[@id="RadioGroup-skipAppCap.samePhysicalAsPersonalAddress-fieldset"]'
        )
        
        # Business structure
        random_sleep(1)
        # retry_count = 0
        # while retry_count < 600:
        #     try:
        #         select_element = driver.find_element(
        #             by=By.XPATH,
        #             value='//*[@id="business-businessstructure"]'
        #         )

        #         value = 'CORPORATION'
        #         driver.execute_script(
        #             "arguments[0].setAttribute('value',arguments[1])", select_element, value)
        #         break
        #     except:
        #         driver.execute_script("window.scrollBy(0,5)")
        #         retry_count += 1
        #         random_sleep(0.1)
        # random_sleep(1)

        # Business Phone Number
        write_delay(
            driver,
            '//*[@id="business-primaryContactPhoneNumber-0"]',
            businessPhoneNumber
        )

        # Business Established Date
        write_delay(
            driver,
            '//*[@id="businessEstablishedDateLabel"]',
            businessEstablishedDate
        )

        # Annual Business Revenue
        write_delay(
            driver,
            '//*[@id="business.organizationAnnualRevenueUnitedStatesDollarAmount-genericmoneyinput"]',
            annualBusinessRevenue
        )

        # Estimated Monthly Spend
        write_delay(
            driver,
            '//*[@id="business.estimatedMonthlySpendAmount-genericmoneyinput"]',
            estimatedMonthlySpend
        )

        # Business Description
        write_delay(
            driver,
            '//*[@id="textinput-business.organizationPurposeDescriptionText"]',
            businessDescription
        )

        # Business Category
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="skipAppCap-category-businessOwner"]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, 81)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Business type
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="skipAppCap-type-businessOwner"]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, 8111)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Business type
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="business-naics-naicsCode-businessOwner"]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, 811111)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Percent of Ownership
        write_delay(
            driver,
            '//*[@id="skipAppCap-businessOwnershipPercentage"]',
            100
        )

        # Checkbox No
        # send_click(
        #     driver,
        #     '//*[@id="skipAppCap.certificationsAgreement-checkbox-0"]'
        # )

        # Checkbox 1
        send_click(
            driver,
            '//*[@id="skipAppCap.certificationsAgreement-Fieldset"]'
        )
        
         # Business type
        retry_count = 0
        while retry_count < 600:
            try:
                driver.execute_script('document.querySelector("#root > div > div:nth-child(2) > div > div:nth-child(3) > main > form > div > div:nth-child(30) > div > mds-fieldset").querySelector("div > div > div > mds-checkbox").shadowRoot.querySelector("div").click()')
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="input-skipAppCap.certificationsAgreement-checkbox-0"]'
                # )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", select_element, 811111)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        # Submit Button
        send_click(
            driver,
            '//*[@id="primary-nav-button"]'
        )

        random_sleep(10)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Southwest Rapid Rewards Performance Business Credit Card"
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
        card_name = "Southwest Rapid Rewards Performance Business Credit Card"

        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

