from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ---------------------------------------------------------------
# Wells Fargo Signify Business Cashservice Mark Card
# ---------------------------------------------------------------

def wellsFargoSignifyBusinessCashserviceMarkCard(driver, data, product_id):
    try:
        driver.get(
            "https://apply.wellsfargo.com/businesscreditcard?token=jTyIaDy1lllN_jVNaZpJk79_IPivUrgJ#OSMA_APPL_BUSINESS_CREDITCARD_LOGIN_PAGE"
        )
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        )
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        employmentType = data.get("personal").get("employmentType")
        mobileNumber = data.get("personal").get("mobileNumber")
        grossIncome = data.get("personal").get("householdIncome")
        housingStatus = data.get("personal").get("housingStatus")

        random_sleep(20)

        # First Name
        write_delay(
            driver,
            '//*[@id="personal_information.first_name"]',
            firstName
        )

        random_sleep(1)

        # Last name
        write_delay(
            driver,
            '//*[@id="personal_information.last_name"]',
            lastName
        )
        random_sleep(1)

        # Date of birth
        write_delay(
            driver,
            '//*[@id="personal_information.date_of_birth"]',
            dob
        )
        random_sleep(1)

        # SSN Number
        write_delay(
            driver,
            '//*[@id="masked_personal_information.ssn"]',
            ssn
        )

        random_sleep(1)

        # Home address
        write_delay(
            driver,
            '//*[@id="personal_information.domestic_address.address_line_1"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="personal_information.domestic_address.postal_code"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="personal_information.domestic_address.city"]',
            city,
            clear=True
        )

        random_sleep(1)

        # State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="personal_information.domestic_address.state_code"]',
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="personal_information.domestic_address.state_code"]'
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
            '//*[@id="personal_information.email_address"]',
            email
        )

        random_sleep(1)

        # Phone number
        write_delay(
            driver,
            '//*[@id="personal_information.phone_number"]',
            mobileNumber
        )

        random_sleep(1)

        # Checkbox One
        send_click(
            driver,
            '//*[@id="ssa_consent"]',
        )
        random_sleep(1)

        # Type of residence
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="financial_information.housing_status"]',
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="financial_information.housing_status"]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])",
                    select_element,
                    housingStatus
                )
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
                send_click(
                    driver,
                    '//*[@id="single_form"]/div[2]/fieldset/div[2]/div[1]/div/div/div[1]/div/div[2]',
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="single_form"]/div[2]/fieldset/div[2]/div[1]/div/div/div[1]/div/div[2]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])",
                    select_element,
                    employmentType
                )
                break
            except:
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        # Gross annual income
        write_delay(
            driver,
            '//*[@id="financial_information.total_annual_income"]',
            grossIncome
        )

        random_sleep(1)

        # I Agree
        try:
            send_click(driver, '//*[@id="single_form"]/div[1]/fieldset/div[2]/div[1]/div[1]')
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Wells Fargo Signify Business Cashservice Mark Card.png"
            )
        random_sleep(1)

        # Submit button
        send_click(driver, '//*[@id="btn_submit"]')
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
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Wells Fargo Signify Business Cashservice Mark Card"
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
        card_name = "Wells Fargo Signify Business Cashservice Mark Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
