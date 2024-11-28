from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# One Main Financial
# ------------------------------------------------------

def oneMainFinancial(driver, data, product_id):
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
        #         "desiredLoanAmount": 5000,
        #         "loanPurpose": "Bill Consolidation",
        #         "vehicleOwnership": "Own",
        #         "applyingForLoan": "INDIVIDUALLY",
        #         "moveInMonth": "01",
        #         "moveInYear": "2020",
        #         "propertyOwnership": "YES",
        #         "netIncome": 5000,
        #         "incomeSource": "Employed",
        #         "currentEmployer": "ABC Corp",
        #         "monthHired": "01",
        #         "yearHired": "2015",
        #         "accountType": "Checking"
        #     }
        # }
        driver.get("https://www.onemainfinancial.com/apply")
        random_sleep(15)

        personal = data.get("personal")
        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        dob = personal.get("dob")
        ssn = personal.get("ssn")
        homeAddress = personal.get("homeAddress")
        city = personal.get("city")
        zipcode = personal.get("zipcode")
        state = personal.get("state")
        email = data.get("email")
        employmentType = personal.get("employmentType")
        mobileNumber = personal.get("mobileNumber")
        grossIncome = personal.get("grossIncome")
        desiredLoanAmount = personal.get("desiredLoanAmount")
        loanPurpose = personal.get("loanPurpose")
        vehicleOwnership = personal.get("vehicleOwnership")
        applyingForLoan = personal.get("applyingForLoan")
        moveInMonth = personal.get("moveInMonth")
        moveInYear = personal.get("moveInYear")
        propertyOwnership = personal.get("propertyOwnership")
        netIncome = personal.get("netIncome")
        incomeSource = personal.get("incomeSource")
        currentEmployer = personal.get("currentEmployer")
        monthHired = personal.get("monthHired")
        yearHired = personal.get("yearHired")
        accountType = personal.get("accountType")

        random_sleep(20)

        # Fill out the form
        write_delay(driver, '//*[@id="form-field-firstname"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-lastname"]', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-email"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-phone"]', mobileNumber)
        
        random_sleep(1)
        write_delay(driver, '//*[@id="requested_amount"]', desiredLoanAmount)
        random_sleep(1)
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[1]/div/div[2]/div[2]/fieldset/div[1]/label[6]')  # other it
        random_sleep(1)
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[1]/div/div[2]/div[3]/fieldset/div/label[3]')  # no vehicle
        random_sleep(1)
        # Click on full name
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[3]/div[1]')
        random_sleep(1)
        write_delay(driver, '//*[@id="applicant_first_name"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="applicant_last_name"]', lastName)
        random_sleep(1)
        # Click on Address
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[4]/div[1]')
        random_sleep(1)
        write_delay(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[4]/div[1]', homeAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[6]/div[1]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[7]/div[1]', mobileNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_birth_date_month"]', dob.split('/')[0])
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_birth_date_day"]', dob.split('/')[1])
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_birth_date_year"]', dob.split('/')[2])
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_current_address_move_in_month"]', moveInMonth)
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_current_address_move_in_year"]', moveInYear)
        random_sleep(1)
        send_click(driver, '//*[@id="applicant_diff_mailing_address"]')
        random_sleep(1)
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[4]/div[2]/div[8]/fieldset/div/label[2]')  # Own property
        random_sleep(1)
        write_delay(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[9]/div[1]', ssn)
        random_sleep(1)
        write_delay(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[10]/div[1]', netIncome)
        random_sleep(1)
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[11]/div[2]/div[1]/div/div[1]/fieldset/div/label[1]')  # Employed
        random_sleep(1)
        write_delay(driver, '//*[@id="applicant_current_employment_name"]', currentEmployer)
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_current_employment_month"]', monthHired)
        random_sleep(1)
        write_delay(driver, '//*[@id="date_applicant_current_employment_year"]', yearHired)
        random_sleep(1)
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[1]/div[11]/div[2]/div[3]/fieldset/div/label[1]')  # Checking account
        random_sleep(1)
        send_click(driver, '//*[@id="consolidated_consents"]')
        random_sleep(1)
        send_click(driver, '//*[@id="toggle_consent"]')
        random_sleep(1)
        send_click(driver, '//*[@id="maincontent"]/div[3]/div/div/form/div[4]/div[2]/input[2]')  # Submit Loan Application
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "One Main Financial"
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
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "One Main Financial"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
