from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# United Club Infinite Card
# ------------------------------------------------------

def infiniteCard(driver,data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "citizenship": "Indiam",
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         # "housingStatusDict": "housingStatusDict",
        #         "housingStatus": "Own",
        #         "grossIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "employmentType": "EMPLOYED",
        #         "state": 'AK',
        #         "zipcode": 30201,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get(
            "https://secure.chase.com/web/oao/application/card?sourceCode=HDTD&action=guest&cellCode=TKV&combo=Y&flowVersion=REACT&AOC=5058&RPC=0437&cfgCode=FULLAPPCONCC#/origination/cardDetails/index/initiateConFullApp"
        )
        # send_click(
        #     driver, 
        #     '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        # )
        random_sleep(15)
        firstName = data.get("personal").get("firstName")
        middleName = data.get("personal").get("middleName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        motherMaidenName = data.get("personal").get("motherMaidenName")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        employmentType = data.get("personal").get("employmentType")
        mobileNumber = data.get("personal").get("mobileNumber")
        bonvoyNumber = data.get("personal").get("bonvoyNumber")
        residencyStatus = data.get("personal").get("housingStatus")
        grossIncome = data.get("personal").get("householdIncome")
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}

        employmentTypeDict = {
            "full-time": "EMPLOYED",
            "part-time": "EMPLOYED",
            "freelance": "EMPLOYED",
            "internship": "EMPLOYED",
        }
        
        random_sleep(20)
        
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
            '//*[@id="root"]/div/div[2]/div/div[3]/main/form/div/div[4]/div[2]/mds-datepicker', 
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
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
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
        
        # Checkbox One
        send_click(
            driver,
            '//*[@id="ssaDisclosure-checkbox-0"]',
        )
        random_sleep(1)
        
        # Type of residense
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="applicant-residenceOwnershipSelect"]'
                )

                value = housingStatusDict.get(housingStatus)
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, value)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        # Employment status
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="applicant-primaryIncomeSourceSelect"]'
                )
                value = employmentTypeDict.get(employmentType)
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, value)
                break
            except:
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        
        # Gross annual income
        write_delay(
            driver,
            '//*[@id="applicant.financialInformation.incomeDetails.0.totalAnnualIncomeAmount-genericmoneyinput"]',
            grossIncome
        )

        random_sleep(1)

        random_sleep(1)

        # I Agree
        try:
            # send_click(
            #     driver, 
            #     '//*[@id="skipAppCap.consumerCertificationsAgreement-checkbox-0"]'
            # )
            driver.execute_script('document.querySelector("#root > div > div.mds-container-fluid.mds-px-at-768-0.containerLock > div > div.mds-col-at-576-8.mds-col-at-768-8.mds-col-at-992-6.mds-col-12.mds-mt-4 > main > form > div > div:nth-child(18) > mds-fieldset").querySelector("div> div> div> mds-checkbox").shadowRoot.querySelector("div>div").click()' )
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - United Club Infinite Card.png"
            )
        random_sleep(1)
        
        # Submit button
        send_click(driver, '//*[@id="primary-nav-button"]')
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value='//*[@id="CONFIRMATION_ADVISORY"]'
                )
                break
            except:
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "United Club Infinite Card"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
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
        card_name = "United Club Infinite Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

