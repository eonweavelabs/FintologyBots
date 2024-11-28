from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click


def customCashRewards(driver, data, product_id):
    try:
        print(driver)
        driver.get(
            "https://www.bankofamerica.com/credit-cards/products/cash-back-credit-card/"
        )

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
        mobileNumber = data.get("personal").get("mobileNumber")
        residencyStatus = data.get("personal").get("housingStatus")
        householdIncome = data.get("personal").get("householdIncome")
        position = data.get("personal").get("position")
        employer = data.get("personal").get("currentEmployer")
        employmentType = data.get("personal").get("employmentType")
        incomeSource = data.get("personal").get("incomeSource")
        monthlyPayment = data.get("personal").get("monthlyPayment")
        employmentTypeDict = {
            "full-time": "Employed",
            "part-time": "Employed",
            "freelance": "Employed",
            "internship": "Employed",
        }
        print("before")
        random_sleep(10)
        send_click(driver, "//a[contains(text(), 'Apply Now')]")
        print("after")
        random_sleep(10)

        write_delay(driver, "#customerFirstName", firstName)

        random_sleep(1)
        if "middleName" in data.get("personal", {}):
            write_delay(driver, "#customerMiddleName", middleName)

            random_sleep(1)

            driver.find_element(By.CSS_SELECTOR, "#customerMiddleName").send_keys(
                Keys.TAB
            )
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")

        write_delay(driver, "#customerLastName", lastName)

        random_sleep(1)
        write_delay(driver, "#customerResidentialAddressOne", homeAddress)

        random_sleep(1)
        write_delay(driver, "#customerAddressCity", city)

        random_sleep(1)
        send_click(driver, "#customerAddressState")
        send_click(driver, f'//option[@value="{state}"]')
        random_sleep(1)
        write_delay(driver, "#customerAddressInput", zipcode)

        random_sleep(1)
        write_delay(driver, "#customerPrimaryPhoneNumber", mobileNumber)

        random_sleep(1)
        send_click(driver, "#phoneNumberHome")
        random_sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#phoneNumberMobile").send_keys(
            Keys.ARROW_UP
        )
        random_sleep(1)
        write_delay(driver, "#customerEmailAddress", email)

        random_sleep(1)

        send_click(driver, "//a[@id='icaiContinueButton']")

        random_sleep(3)
        random_sleep(1)

        send_click(driver, "#customerUsCitizenNo")
        random_sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#customerUsCitizenNo").send_keys(
            Keys.ARROW_UP
        )
        random_sleep(1)
        write_delay(driver, "#customerSocialSecurityNumber", ssn)

        random_sleep(1)
        send_click(driver, "#customerDualCitizenshipYes")
        random_sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#customerDualCitizenshipYes").send_keys(
            Keys.ARROW_DOWN
        )
        random_sleep(1)
        Select(
            driver.find_element(By.CSS_SELECTOR, "#customerCountryOfResidence")
        ).select_by_index(1)

        write_delay(driver, "#customerBirthDate", dob)

        random_sleep(1)
        send_click(driver, "//a[@id='icaiContinueButton']")

        random_sleep(5)

        send_click(driver, '//select[@id="employmentStatus"]')

        random_sleep(1)
        print(employmentTypeDict.get(employmentType))
        driver.find_element(
            by=By.XPATH, value='//select[@id="employmentStatus"]'
        ).find_element(
            by=By.XPATH,
            value=f'.//option[@value="{employmentTypeDict.get(employmentType)}"]',
        ).click()
        random_sleep(1)

        send_click(driver, '//select[@id="occupation"]')
        random_sleep(1)
        driver.find_element(
            by=By.XPATH, value='//select[@id="occupation"]'
        ).find_elements(by=By.TAG_NAME, value="option")[-1].click()
        random_sleep(2)
        try:
            tempdropdown = driver.find_elements(
                by=By.XPATH, value='//a[@data-aaclickevent="true"]'
            )
        except:
            random_sleep(5)
            tempdropdown = driver.find_elements(
                by=By.XPATH, value='//a[@data-aaclickevent="true"]'
            )
        position = position.lower().replace("salesperson", "sales")
        for tempoccupation in tempdropdown:
            if position.lower() in tempoccupation.text.lower():
                tempoccupation.click()
                break
        random_sleep(4)
        write_delay(driver, "#annualSalary", householdIncome)
        random_sleep(1)
        send_click(driver, '//select[@id="incomeSource"]')
        random_sleep(1)
        driver.find_element(
            by=By.XPATH, value='//select[@id="incomeSource"]'
        ).find_elements(by=By.TAG_NAME, value="option")[1].click()
        random_sleep(1)
        write_delay(driver, "#monthlyHousingPayment", monthlyPayment)
        send_click(driver, "//a[@id='icaiContinueButton']")

        random_sleep(3)
        send_click(driver, '//input[@id="termsAndConditionsCheckBox"]')
        random_sleep(10)

        random_sleep(2)
        send_click(driver, "//a[@id='icaiContinueButton']")

        random_sleep(2)
        send_click(driver, "//a[@id='icaiContinueButton']")

        random_sleep(100)
        input(1)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - BOFA Custom Cash Rewards.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "BOFA Custom Cash Rewards"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

    except Exception as e:
        "//button[@id='continueBtn']"
        "//input[@name='consentCheckbox' and @id='checkbox']"
        print(e)
        input("Error in application")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "BOFA Custom Cash Rewards"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
