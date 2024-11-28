from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ---------------------------------------------------------------
# Marriott Bonvoy Boundless Credit Card
# ---------------------------------------------------------------

def bonvoyBoundless(driver,data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "15/06/2000",
        #         "ssn": "ssn",
        #         # "housingStatusDict": "housingStatusDict",
        #         "housingStatus": "Own",
        #         "grossIncome": "grossIncome",
        #         "mobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "employmentType": "EMPLOYED",
        #         "state": "Guam",
        #         "zipcode": 302012,
        #         "city": "Jaipur",
        #         "homeAddress": "homeAddress",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get(
            "https://secure.chase.com/web/oao/application/card?sourceCode=HFFX&action=guest#/origination/cardDetails/index/initiateConFullApp;cellCode=61DS;cfgCode=FULLAPPCONCC;channel=C30;sourceCode=HFFX;AOC=5056;RPC=0513;combo=N;params=,,,no,no,,,"
        )
        # send_click(
        #     driver, '/html/body/div[1]/div/div[1]/div/div/header/div[3]/div[2]/div/div[2]/div[1]/div[1]/a')
        random_sleep(15)
        # driver.switch_to.window(driver.window_handles[-1])
        print(driver, 'driver')
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

        print(123)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="blx-nameBlock-firstName-text-validate-input-field"]', 
            firstName
        )
        random_sleep(1)
        if len(middleName):
            write_delay(driver, '//*[@id="blx-nameBlock-middleName-text-validate-input-field"]', middleName)
            random_sleep(1)
            # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")
        write_delay(driver, '//*[@id="blx-nameBlock-lastName-text-validate-input-field"]', lastName)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='lastName']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="dateOfBirth-text-validate-input-field"]', 
            dob
        )
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='dateOfBirth']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="mothersMaidenName-text-validate-input-field"]',
            motherMaidenName
        )
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="maskedSocialSecurityNumber-text-validate-input-field"]', 
            ssn
        )

        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="streetAddress-blx-residentialAddressBlock-text-validate-input-field"]', 
            homeAddress
        )

        random_sleep(1)
        random_sleep(1)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="zipCode-blx-residentialAddressBlock-text-validate-input-field"]', 
            zipcode
        )

        random_sleep(1)
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="city-blx-residentialAddressBlock-text-validate-input-field"]',
            city, 
            clear=True
        )

        random_sleep(1)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="select-state-blx-residentialAddressBlock-select-validate"]'
                )
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="emailAddressId-text-validate-input-field"]', 
            email
        )

        random_sleep(1)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="phoneNumberId-text-validate-input-field"]', 
            mobileNumber
        )

        random_sleep(1)
        send_click(
            driver,
            '//*[@id="input-socialSecurityAdministrationDisclosureAcceptance"]',
        )
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="marriottBonvoyId-text-validate-input-field"]', 
            bonvoyNumber
        )

        random_sleep(1)
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="select-residenceOwnership-select-validate"]'
                )
                select = Select(select_element)
                select.select_by_value(housingStatusDict.get(housingStatus))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="select-primaryIncomeSourceName-select-validate"]'
                )
                select = Select(select_element)
                select.select_by_value(employmentTypeDict.get(employmentType))
                break
            except:
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="grossAnnualIncome-text-validate-input-field"]',
            grossIncome
        )

        random_sleep(1)

        random_sleep(1)

        try:
            send_click(driver, '//*[@id="input-navigationAdvisory"]')
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Marriott Bonvoy Boundless Credit Card.png"
            )
        random_sleep(1)
        send_click(driver, '//*[@id="SUBMIT-nav-ctr-btn"]')
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
        card_name = "Marriott Bonvoy Boundless Credit Card"
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
        card_name = "Marriott Bonvoy Boundless Credit Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
