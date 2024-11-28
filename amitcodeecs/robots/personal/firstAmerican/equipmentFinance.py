from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# First American Equipment Finance
# ------------------------------------------------------

def firstAmericanEquipmentFinance(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "ssn": 124365888,
        #         "housingStatus": "own",
        #         "grossIncome": 876655,
        #         "mobileNumber": 7349303040,
        #         "employmentType": "full-time",
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "city": "Jaipur",
        #         "homeAddress": "123 street",
        #         "motherMaidenName": "motherMaidenName",
        #         "loanAmount": 5000,
        #         "loanPurpose": "personal",
        #         "timeAtResidence": 24,
        #         "timeEmployed": 36,
        #         "nextPaydate": "01/15/2023",
        #         "employerName": "ABC Corp",
        #         "jobTitle": "Software Engineer",
        #         "workPhone": 1234567890,
        #         "payFrequency": "bi-weekly",
        #         "directDeposit": "yes",
        #         "routingNumber": "123456789",
        #         "bankName": "XYZ Bank",
        #         "accountType": "checking",
        #         "monthsAtBank": 12,
        #         "bankPhone": 9876543210,
        #         "bankAccountNumber": "123456789012",
        #         "driversLicenseNumber": "D1234567",
        #         "issuingState": "AK",
        #         "creditScore": 700,
        #     }
        # }

        driver.get("https://www.faef.com/contact-us")
        random_sleep(15)

        personal = data.get("personal")
        email = data.get("email")

        random_sleep(20)
        driver.switch_to.frame(0)
        # First Name
        write_delay(driver, '//*[@id="391892_203619pi_391892_203619"]', 'Kanha')
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastNameTextInput"]', personal.get("lastName"))
        random_sleep(1)

        # Mobile Number
        write_delay(driver, '//*[@id="mobilePhoneNumberTextInput"]', personal.get("mobileNumber"))
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="emailTextInput"]', email)
        random_sleep(1)

        # SSN
        write_delay(driver, '//*[@id="ssnTextInput"]', (personal.get("ssn")))
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="zipCodeTextInput"]', personal.get("zipcode"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="gettingStartedContinueButton"]')
        random_sleep(1)

        # Date of Birth
        write_delay(driver, '//*[@id="dateOfBirthTextInput"]', personal.get("dob"))
        random_sleep(1)

        # Street Address
        write_delay(driver, '//*[@id="streetAddressTextInput"]', personal.get("homeAddress"))
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="cityTextInput"]', personal.get("city"))
        random_sleep(1)

        # Loan Amount
        write_delay(driver, '//*[@id="requestedAmountNumberInput"]', personal.get("loanAmount"))
        random_sleep(1)

        # Disclosure Agreement Checkbox
        send_click(driver, '//*[@id="disclosureAgreementCheckbox"]')
        random_sleep(1)

        # SSN Verification Checkbox
        # send_click(driver, '//*[@id="disclosureSsnVerificationCheckbox"]')
        # random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="moreInfoContinueButton"]')
        random_sleep(1)

        # Correct Information Confirmation Checkbox
        send_click(driver, '//*[@id="correctInformationConfirmationCheckBox"]')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="verifyContinueButton"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "First American Equipment Finance"
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
        card_name = "First American Equipment Finance"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
