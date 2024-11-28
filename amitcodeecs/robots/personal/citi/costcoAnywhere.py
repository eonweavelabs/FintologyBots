from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Citi Costco Anywhere
# -----------------------------------------------------

def costcoAnywhere(driver,data, product_id):
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
        #         "membership": 456836297456,
        #         "housingStatus": "Own",
        #         "grossIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "rent": 15000,
        #         "employmentType": "EMPLOYED",
        #         "state": 'AK',
        #         "zipcode": 30201,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get(
            "https://www.citicards.com/cards/credit/application/flow.action?app=UNSOL&prodType=CitiCardCostco&HKOP=0bedd33ea2e219ef0047f46c5426be8724121594b518e11bda37818bd6908748&ID=3000&ProspectID=PcydTveGMaAan7snlLAxP2PcqrauCu7F&intc=7~7~66~1~PDP~1~CMSDefaultOffer&pid=520&afc=1C2&adobe_mc=MCMID%3D02802470873384425531468361853807654197%2CMCAID%3DNONE"
        )
        # send_click(
        #     driver, '/html/body/div[1]/div/div[1]/div/div/header/div[3]/div[2]/div/div[2]/div[1]/div[1]/a')
        random_sleep(15)

        membership = data.get("personal").get("membership")
        citizenship = data.get("personal").get("citizenship")
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
        rent = data.get("personal").get("rent")
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
        
        # Membership number
        write_delay(
            driver,
            '//*[@id="AFFINITY_NUMBER_PRIMARY-citiTextBlur"]', 
            membership
        )
        
        # First Name
        write_delay(
            driver,
            '//*[@id="FIRST_NAME"]', 
            firstName
        )
        
        random_sleep(1)
        
        # Middle name
        if len(middleName):
            write_delay(
                driver, 
                '//*[@id="MIDDLE_NAME"]', 
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
            '//*[@id="LAST_NAME"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)
        
        # Date of birth
        write_delay(
            driver,
            '//*[@id="DOB-citiTextBlur"]', 
            dob
        )
        random_sleep(1)
        random_sleep(1)
        
        random_sleep(1)
        
        # SSN Number
        write_delay(
            driver, 
            '//*[@id="SSN-citiTextBlur"]', 
            ssn
        )

        random_sleep(1)
        
        # Home address
        write_delay(
            driver, 
            '//*[@id="ADDRESS_LINE1"]', 
            homeAddress
        )

        random_sleep(1)
        
        # ZIP Code
        write_delay(
            driver, 
            '//*[@id="ZIP"]', 
            zipcode
        )

        random_sleep(1)
        
        # City
        write_delay(
            driver,
            '//*[@id="CITY"]',
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
                    value='//*[@id="STATE"]'
                )
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="applicant.address.0-addressStateCode"]'
                # )
                select = Select(select_element)
                select.select_by_value(state)
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)
        
        # Email
        write_delay(
            driver, 
            '//*[@id="EMAIL_ADDRESS"]', 
            email
        )

        random_sleep(1)
        random_sleep(1)
        
        # Phone number
        write_delay(
            driver,
            '//*[@id="MOBILE_PHONE-citiTextBlur"]', 
            mobileNumber
        )

        random_sleep(1)
        
        # Checkbox One
        # send_click(
        #     driver,
        #     '//*[@id="input-socialSecurityAdministrationDisclosureAcceptance"]',
        # )
        # random_sleep(1)

        random_sleep(1)
        
        # Security Word Hint 
        # send_click(
        #     driver,
        #     '//*[@id="SECPASSTYPE_CODE"]'
        # )
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="SECPASSTYPE_CODE"]'
                )
                select = Select(select_element)
                select.select_by_value('T')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        
        # Mother name
        write_delay(
            driver, 
            '//*[@id="MOTHERS_MAIDEN_NAME-citiTextBlur"]',
            motherMaidenName
        )
        

        # Country of Citizenship
        random_sleep(1)
        # retry_count = 0
        # while retry_count < 600:
        #     try:
        #         select_element = driver.find_element(
        #             by=By.XPATH, 
        #             value='//*[@id="COUNTRY_OF_CITIZENSHIP"]'
        #         )
        #         select = Select(select_element)
        #         select.select_by_value(citizenship)
        #         break
        #     except:
        #         retry_count += 1
        #         random_sleep(0.1)
        # random_sleep(1)
        
        # Gross annual income
        write_delay(
            driver, 
            '//*[@id="ANNUAL_INCOME"]',
            grossIncome
        )
        
        write_delay(
            driver, 
            '//*[@id="MRTG_RENT_AMT"]',
            rent
        )

        random_sleep(1)

        random_sleep(1)

        # Second Checkbox
        try:
            send_click(driver, '//*[@id="TERMS_DISCLOSURE"]')
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Citi Costco Anywhere.png"
            )
        random_sleep(1)
        
        # Submit button
        send_click(driver, '//*[@id="step1_submit"]')
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
        card_name = "Citi Costco Anywhere"
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
        card_name = "Citi Costco Anywhere"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

