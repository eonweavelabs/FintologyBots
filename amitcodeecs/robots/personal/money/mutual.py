from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Money Mutual
# ------------------------------------------------------

def moneyMutual(driver, data, product_id):
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
        
        driver.get("https://moneymutual.com/")
        random_sleep(15)

        personal = data.get("personal")
        email = data.get("email")

        # random_sleep(20)

        send_click(driver, '//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[3]/div/div[1]/div[3]/button')
        random_sleep(1)

        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="state"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value(personal.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formStateStep"]/div[3]/button')
        random_sleep(5)

        # First Name
        write_delay(driver, '//*[@id="nameFirst"]', personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="nameLast"]', personal.get("lastName"))
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
        send_click(driver, '//*[@id="formInitialInfoStep"]/div[1]/div[4]/div/label')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formInitialInfoStep"]/div[3]/button[2]')
        random_sleep(5)

        # Mobile Number
        write_delay(driver, '//*[@id="primaryPhone"]', personal.get("mobileNumber"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formPhoneStep"]/div[3]/button[2]')
        random_sleep(5)

        # Income Source
        # write_delay(driver, '//*[@id="incomeSourceComposite"]', personal.get("grossIncome"))
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="incomeSourceComposite"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('3:')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formIncomeTypeStep"]/div[3]/button[2]')
        random_sleep(5)

        # Street Address
        write_delay(driver, '//*[@id="street"]', personal.get("homeAddress"))
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="city"]', personal.get("city"))
        random_sleep(1)

        # State
        # write_delay(driver, '//*[@id="state"]', personal.get("state"))
        # random_sleep(1)

        # Time at Residence
        # write_delay(driver, '//*[@id="residenceLengthMonths"]', "12")
        # random_sleep(1)

        # Select Residence
        send_click(driver, '//*[@id="field_residence_status"]/div[2]/label')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formResidenceStep"]/div[3]/button[2]')
        random_sleep(1)

        # Military Step
        send_click(driver, '//*[@id="formMilitaryStep"]/div[1]/div[3]/div/div[1]/label')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formMilitaryStep"]/div[3]/button[2]')
        random_sleep(5)

        # own a car
        send_click(driver, '//*[@id="formTitleLoanStep"]/div[1]/div[3]/div/div[3]/label')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formTitleLoanStep"]/div[3]/button[2]')
        random_sleep(5)

        # Monthly Income
        write_delay(driver, '//*[@id="incomeMonthly"]', personal.get("netIncome"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formMonthlyIncomeStep"]/div[3]/button[2]')
        random_sleep(5)

        # Have Bank Account
        send_click(driver, '//*[@id="receiveIncomeType"]/div[1]/label')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formBankAccountStep"]/div[3]/button[2]')
        random_sleep(5)

        # Credit cards
        send_click(driver, '//*[@id="formCCDebtStep"]/div[1]/div[3]/div/div[2]/label')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formCCDebtStep"]/div[3]/button[2]')
        random_sleep(5)

        # How often are you paid?
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="payFrequency"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('5')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # When is your NEXT pay date?
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="formPayDatesStep"]/div[1]/input'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, '11/18/2024')
                # select = Select(select_element)
                # select.select_by_value('3:')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # write_delay(driver , '//*[@id="formPayDatesStep"]/div[1]/input' , '12/18/2024')
        # send_click(driver, '//*[@id="formCCDebtStep"]/div[1]/div[3]/div/div[2]/label')
        # random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formPayDatesStep"]/div[3]/button[2]')
        random_sleep(5)

        # Employer 
        write_delay(driver, '//*[@id="employerName"]', personal.get("employer"))
        random_sleep(1)

        # Work Phone 
        write_delay(driver, '//*[@id="workPhone"]', personal.get("workPhone"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formEmploymentInfoStep"]/div[3]/button[2]')
        random_sleep(5)
        
        # id number
        write_delay(driver, '//*[@id="legalIdNumber"]', personal.get("idNumber"))
        random_sleep(1)

        random_sleep(1)

        # State
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="legalIdState"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value(personal.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formValidIdStep"]/div[3]/button[2]')
        random_sleep(5)

        # ssn
        write_delay(driver, '//*[@id="ssn"]', personal.get("ssn"))
        random_sleep(1)
        # dob
        write_delay(driver, '//*[@id="dateOfBirth"]', personal.get("dob"))
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="formPiiStep"]/div[3]/button[2]')
        random_sleep(5)

        # bank
        write_delay(driver, '//*[@id="bankName"]', personal.get("bank"))
        random_sleep(1)

        # Routing 
        write_delay(driver, '//*[@id="bankAba"]', personal.get("routingNumber"))
        random_sleep(1)

        # Account Number 
        write_delay(driver, '//*[@id="bankAccount"]', personal.get("accountNumber"))
        random_sleep(1)

        # Submit
        send_click(driver, '//*[@id="formDepositInfoStep"]/div[3]/div/button')
        random_sleep(15)
        
        

        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Money Mutual"
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
        card_name = "Money Mutual"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)