from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot

from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


def freedom(driver, data, product_id):
    try:

        driver.get("https://creditcards.chase.com/cash-back-credit-cards/Freedom")
        send_click(driver, '//a[contains(@data-lh-name, "ApplyNowCategoryPage")]')
        random_sleep(3)
        driver.switch_to.window(driver.window_handles[-1])

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

        # if not firstName or not lastName or not dob or not motherMaidenName or not ssn or not homeAddress or not city or not zipcode or not state or not email or not mobileNumber or not residencyStatus or not grossIncome:
        #     raise Exception("Missing personal data.")
        random_sleep(20)


        count = 0
        send_click(driver, "//div[@class='mds-col-at-576-6 mds-col-12 mds-mb-5']")
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
        write_delay(driver, "//input[@name='applicant.name.firstName']", firstName)
        random_sleep(1)
        if len(middleName):
            write_delay(driver, "//input[@name='applicant.name.middleName']", middleName)
            random_sleep(1)
            # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")
        write_delay(driver, "//input[@name='applicant.name.lastName']", lastName)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='lastName']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(driver, "//input[@id='applicant-birthDate-input']", dob)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='dateOfBirth']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(driver, "//input[@name='applicant.identity.motherMaidenName']", motherMaidenName)
        random_sleep(1)
        write_delay(driver, "//input[@name='applicant-taxIdentifier-input']", ssn)

        random_sleep(1)
        write_delay(driver, "//input[@name='skipAppCap.applicant.address.0.addressLine1']", homeAddress)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='streetAddress']").send_keys(Keys.TAB)
        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="#apartmentNumber-blx-residentialAddressBlock-text-validate-input-field").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(driver, "//input[@name='skipAppCap.applicant.address.0.addressPostalCode']", zipcode)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='zipCode']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(driver, "//input[@id='applicant.address.0-addressCityName-input']", city, clear=True)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='cityId']").send_keys(Keys.TAB)
        random_sleep(1)
        send_click(driver, '//button[@id="select-applicant.address.0-addressStateCode"]')
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value='//button[@id="select-applicant.address.0-addressStateCode"]'
                ).find_element(
                    by=By.XPATH, value=f'.//mds-select-option[@value="{state}"]'
                ).click()
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value='//select[@name="stateId"]').send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(driver, "//input[@name='emailAddress']", email)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='emailAddress']").send_keys(Keys.TAB)
        random_sleep(1)
        write_delay(driver, "//input[@name='phoneNumber']", mobileNumber)

        random_sleep(1)
        # driver.find_element(by=By.XPATH, value="//input[@name='phoneNumber']").send_keys(Keys.TAB)
        random_sleep(1)
        send_click(
            driver,
            "//label[@for='input-socialSecurityAdministrationDisclosureAcceptance']",
        )

        random_sleep(1)
        send_click(driver, '//select[@name="residenceOwnershipOptionId"]')
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value='//select[@name="residenceOwnershipOptionId"]'
                ).find_element(
                    by=By.XPATH,
                    value=f'.//option[@value="{housingStatusDict.get(housingStatus)}"]',
                ).click()
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        send_click(driver, '//select[@name="primaryIncomeSourceId"]')
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value='//select[@name="primaryIncomeSourceId"]'
                ).find_element(
                    by=By.XPATH,
                    value=f'.//option[@value="{employmentTypeDict.get(employmentType)}"]',
                ).click()
                break
            except:
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        write_delay(driver, "//input[@name='grossAnnualIncome']", grossIncome)

        random_sleep(1)

        random_sleep(1)

        try:
            send_click(driver, "#input-navigationAdvisory")
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png"
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
        card_name = "Chase Freedom"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Chase Freedom"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
