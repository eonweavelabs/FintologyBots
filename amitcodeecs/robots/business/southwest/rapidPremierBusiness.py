from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


def rapidPremierBusiness(driver, data, product_id):
    try:
        # data = {
        #     "personal": {
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "dob",
        #         "ssn": "ssn",
        #         "housingStatusDict": "housingStatusDict",
        #         "housingStatus": "housingStatus",
        #         "grossIncome": "grossIncome",
        #         "mobileNumber": "mobileNumber",
        #         "employmentType": "employmentType",
        #         "email": "email",
        #         "state": "state",
        #         "zipcode": "zipcode",
        #         "city": "city",
        #         "homeAddress": "homeAddress",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }

        driver.get(
            "https://creditcards.chase.com/a1/southwest/AEPBiz624120?REF=FULLSITE&CELL=6PNG#PremierBiz")
        send_click(
            driver, '/html/body/div[1]/div/div[1]/div/div/header/div[3]/div[2]/div/div[2]/div[1]/div[3]/a')
        random_sleep(15)
        # driver.switch_to.window(driver.window_handles[-1])
        print(driver, 'driver')
        authorizing = data.get("personal").get("authorizing")
        firstName = data.get("personal").get("firstName")
        middleName = data.get("personal").get("middleName")
        lastName = data.get("personal").get("lastName")
        suffix = data.get("personal").get("suffix")
        dob = data.get("personal").get("dob")
        motherMaidenName = data.get("personal").get("motherMaidenName")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
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
        # send_click(driver, "//div[@class='mds-col-at-576-6 mds-col-12 mds-mb-5']")
        # while count < 50:
        #     try:
        #         driver.find_element(
        #             by=By.XPATH,
        #             value="//input[@id='blx-nameBlock-firstName-text-validate-input-field']",
        #         )
        #         break
        #     except Exception as e:
        #         print(e)
        #         driver.execute_script("window.scrollBy(0,15)")
        #         count += 1
        #         random_sleep(0.5)
        print(123)
        random_sleep(1)
        write_delay(driver, '//*[@id="applicant-firstName-input"]', firstName)
        random_sleep(1)
        if len(middleName):
            write_delay( driver, '//*[@id="blx-nameBlock-middleName-text-validate-input-field"]', middleName)
            random_sleep(1)
            # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")
        write_delay(
            driver, '//*[@id="blx-nameBlock-lastName-text-validate-input-field"]', lastName)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='lastName']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="dateOfBirth-text-validate-input-field"]', dob)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='dateOfBirth']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="mothersMaidenName-text-validate-input-field"]', motherMaidenName)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="maskedSocialSecurityNumber-text-validate-input-field"]', ssn)

        random_sleep(1)
        write_delay(
            driver, '//*[@id="streetAddress-blx-residentialAddressBlock-text-validate-input-field"]', homeAddress)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='streetAddress']").send_keys(Keys.TAB)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="#apartmentNumber-blx-residentialAddressBlock-text-validate-input-field").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="zipCode-blx-residentialAddressBlock-text-validate-input-field"]', zipcode)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='zipCode']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="city-blx-residentialAddressBlock-text-validate-input-field"]', city, clear=True)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='cityId']").send_keys(Keys.TAB)
        random_sleep(1)
        send_click(
            driver, '//*[@id="select-state-blx-residentialAddressBlock-select-validate"]')
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, value='//*[@id="select-state-blx-residentialAddressBlock-select-validate"]')
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value='//select[@name="stateId"]').send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="emailAddressId-text-validate-input-field"]', email)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='emailAddress']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="phoneNumberId-text-validate-input-field"]', mobileNumber)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='phoneNumber']").send_keys(Keys.TAB)
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="input-socialSecurityAdministrationDisclosureAcceptance"]',
        )

        random_sleep(1)
        send_click(
            driver, '//*[@id="select-residenceOwnership-select-validate"]')
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                # driver.find_element(
                #     by=By.XPATH, value='//select[@name="residenceOwnershipOptionId"]'
                # ).find_element(
                #     by=By.XPATH,
                #     value=f'.//option[@value="{housingStatusDict.get(housingStatus)}"]',
                # ).click()
                select_element = driver.find_element(
                    by=By.XPATH, value='//*[@id="select-residenceOwnership-select-validate"]')
                select = Select(select_element)
                select.select_by_value(housingStatusDict.get(housingStatus))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        send_click(
            driver, '//*[@id="select-primaryIncomeSourceName-select-validate"]')
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                # driver.find_element(
                #     by=By.XPATH, value='//*[@id="select-primaryIncomeSourceName-select-validate"]'
                # ).find_element(
                #     by=By.XPATH,
                #     value=f'.//option[@value="{employmentTypeDict.get(employmentType)}"]',
                # ).click()

                select_element = driver.find_element(
                    by=By.XPATH, value='//*[@id="select-primaryIncomeSourceName-select-validate"]')
                select = Select(select_element)
                select.select_by_value(employmentTypeDict.get(employmentType))
                break
            except:
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        write_delay(
            driver, '//*[@id="grossAnnualIncome-text-validate-input-field"]', grossIncome)

        random_sleep(1)

        random_sleep(1)

        try:
            send_click(driver, '//*[@id="input-navigationAdvisory"]')
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Southwest rapid reward plus.png"
            )
        random_sleep(1)
        send_click(driver, "#SUBMIT-nav-ctr-btn")
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
        card_name = "Southwest rapid reward plus"
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
        card_name = "Southwest rapid reward plus"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
