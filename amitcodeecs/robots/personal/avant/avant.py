from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Avant
# ------------------------------------------------------

def avant(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "ssn": 124365888,
        #         "grossIncome": 876655,
        #         "mobileNumber": 7349303040,
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "city": "Jaipur",
        #         "homeAddress": "123 street",
        #         "loanAmount": 5000,
        #         "loanPurpose": "personal",
        #         "netIncome": 5000,
        #         "bankBalance": 10000,
        #         "monthlyHousingPayment": 1200,
        #         "password": "password123",
        #         "passwordConfirm": "password123"
        #     }
        # }
        driver.get("https://www.avant.com/credit-card")
        random_sleep(15)
        send_click(driver, '//*[@id="gatsby-focus-wrapper"]/div/section/div[2]/div/div/a[1]')

        personal = data.get("personal")
        email = data.get("email")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="person_first_name"]', personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="person_last_name"]', personal.get("lastName"))
        random_sleep(1)

        # Mobile Number
        write_delay(driver, '//*[@id="person_home_phone"]', personal.get("mobileNumber"))
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="customer_email"]', email)
        random_sleep(1)

        # SSN
        write_delay(driver, '//*[@id="person_ssn"]', str(personal.get("ssn"))[-4:])
        random_sleep(1)

        # Date of Birth
        write_delay(driver, '//*[@id="person_date_of_birth"]', personal.get("dob"))
        random_sleep(1)

        # Create Password
        write_delay(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-stage/article/form/fieldset[6]/div/div[1]/div/input', personal.get("password"))
        random_sleep(1)

        # Confirm Password
        write_delay(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-stage/article/form/fieldset[6]/div/div[2]/div/input', personal.get("passwordConfirm"))
        random_sleep(1)

        # Checkbox
        send_click(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-stage/article/form/div[3]/div/span/input')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-stage/article/form/button')
        random_sleep(1)

        # Net Income
        write_delay(driver, '//*[@id="income_monthly_net_income"]', personal.get("netIncome"))
        random_sleep(1)

        # Bank Balance
        write_delay(driver, '//*[@id="customer_application_metadata_current_bank_account_balance"]', personal.get("bankBalance"))
        random_sleep(1)

        # Street Address
        write_delay(driver, '//*[@id="customer_address_address_1"]', personal.get("homeAddress"))
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="customer_address_city"]', personal.get("city"))
        random_sleep(1)

        # State
        write_delay(driver, '//*[@id="customer_address_state"]', personal.get("state"))
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="customer_address_zip"]', personal.get("zipcode"))
        random_sleep(1)

        # Rent or Own
        send_click(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-continued-stage/article/form/fieldset[5]/div/div/div/div[2]/label')
        random_sleep(1)

        # Monthly Housing Payment
        write_delay(driver, '//*[@id="customer_address_monthly_housing_payment"]', personal.get("monthlyHousingPayment"))
        random_sleep(1)

        # Checkbox
        send_click(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-continued-stage/article/form/div[3]/div/span/input')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="maincontent"]/div/div/customer-applications-personal-continued-stage/article/form/button')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Avant"
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
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Avant"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)