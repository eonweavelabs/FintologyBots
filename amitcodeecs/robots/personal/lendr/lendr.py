from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Lendr
# ------------------------------------------------------

def lendr(driver, data, product_id):
    try:
        #data = {
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
        driver.get("https://lendr.online/apply/")
        random_sleep(15)

        personal = data.get("personal")
        email = data.get("email")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="nameFirst"]', personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="nameLast"]', personal.get("lastName"))
        random_sleep(1)

        # Mobile Number
        write_delay(driver, '//*[@id="primaryPhone"]', personal.get("mobileNumber"))
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)

        # Re-enter Email
        write_delay(driver, '//*[@id="emailConfirm"]', email)
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="zip"]', personal.get("zipcode"))
        random_sleep(1)

        # Checkbox
        send_click(driver, '//*[@id="legalCertification"]')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formInitialInfoStep"]/div[3]/button[2]')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formPhoneStep"]/div[3]/button[2]')
        random_sleep(1)

        # Income Source
        write_delay(driver, '//*[@id="incomeSourceComposite"]', personal.get("grossIncome"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formIncomeStep"]/div[3]/button[2]')
        random_sleep(1)

        # Street Address
        write_delay(driver, '//*[@id="street"]', personal.get("homeAddress"))
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="city"]', personal.get("city"))
        random_sleep(1)

        # State
        write_delay(driver, '//*[@id="state"]', personal.get("state"))
        random_sleep(1)

        # Time at Residence
        write_delay(driver, '//*[@id="residenceLengthMonths"]', "12")
        random_sleep(1)

        # Select Residence
        send_click(driver, '//*[@id="field_residence_status"]/div[2]/label/input')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formResidenceStep"]/div[3]/button[2]')
        random_sleep(1)

        # Military Step
        send_click(driver, '//*[@id="formMilitaryStep"]/div[1]/div[3]/div/div[2]/label/input')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formMilitaryStep"]/div[3]/button[2]')
        random_sleep(1)

        # Title Loan Step
        send_click(driver, '//*[@id="formTitleLoanStep"]/div[1]/div[3]/div/div[3]/label/input')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formTitleLoanStep"]/div[3]/button[2]')
        random_sleep(1)

        # Monthly Income
        write_delay(driver, '//*[@id="incomeMonthly"]', personal.get("netIncome"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formMonthlyIncomeStep"]/div[3]/button[2]')
        random_sleep(1)

        # Have Bank Account
        send_click(driver, '//*[@id="receiveIncomeType"]/div[2]/label/input')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formBankAccountStep"]/div[3]/button[2]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Lendr"
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
        card_name = "Lendr"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
