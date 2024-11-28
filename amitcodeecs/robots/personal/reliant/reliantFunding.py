from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Reliant Funding
# ------------------------------------------------------

def reliantFunding(driver, data, product_id):
    try:
        # data = {
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
        #     }
        # }
        driver.get("https://reliantfunding.com/reliant-apply-now/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        # dob = data.get("personal").get("dob")
        # ssn = data.get("personal").get("ssn")
        # homeAddress = data.get("personal").get("homeAddress")
        # city = data.get("personal").get("city")
        # zipcode = data.get("personal").get("zipcode")
        # state = data.get("personal").get("state")
        email = data.get("email")
        # employmentType = data.get("personal").get("employmentType")
        mobileNumber = data.get("personal").get("mobileNumber")
        # grossIncome = data.get("personal").get("householdIncome")
        # housingStatus = data.get("personal").get("housingStatus")
        personal = data.get("personal")

        random_sleep(20)

        # Desired Funding Amount
        # write_delay(driver, '//*[@id="form-field-funding_amount"]', "50000")
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="form-field-funding_amount"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('Over $500,000')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # First Name
        write_delay(driver, '//*[@id="form-field-fname"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="form-field-lname"]', lastName)
        random_sleep(1)

        # Phone Number
        write_delay(driver, '//*[@id="form-field-phone"]', mobileNumber)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="form-field-email"]', email)
        random_sleep(1)

        # Business Name
        write_delay(driver, '//*[@id="form-field-business_name"]', personal.get('businessName'))
        random_sleep(1)

        # Monthly Revenue
        # write_delay(driver, '//*[@id="form-field-monthly_revenue"]', grossIncome)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="form-field-monthly_revenue"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('$100,000 - $249,999')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Business Bank Account
        # send_click(driver, '//*[@id="form-field-biz_account"]')
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="form-field-biz_account"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('No')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Agree to Terms
        send_click(driver, '//*[@id="form-field-field_221b644"]')
        random_sleep(1)

        # Apply Now
        send_click(driver, '//*[@id="funding-submit"]/span')
        random_sleep(15)
        

        # Continue
        # send_click(driver, '//*[@id="continue-btn"]/div/div/a/span')
        # random_sleep(1)

        # # Business Legal Name
        # write_delay(driver, '//*[@id="form-field-field_eb9a8fc"]', "My Business Legal Name")
        # random_sleep(1)

        # # Business DBA Name
        # write_delay(driver, '//*[@id="form-field-biz_dba_name"]', "My DBA Name")
        # random_sleep(1)

        # # Legal Entity Proprietor
        # write_delay(driver, '//*[@id="form-field-legal_entity"]', "Proprietor")
        # random_sleep(1)

        # # Business Start Date
        # write_delay(driver, '//*[@id="form-field-biz_start_date"]', "01/01/2010")
        # random_sleep(1)

        # # Federal Tax ID (EIN)
        # write_delay(driver, '//*[@id="form-field-fed_tax_id"]', "123456789")
        # random_sleep(1)

        # # Business Address
        # write_delay(driver, '//*[@id="form-field-address"]', homeAddress)
        # random_sleep(1)

        # # Business City
        # write_delay(driver, '//*[@id="form-field-city"]', city)
        # random_sleep(1)

        # # Business State
        # write_delay(driver, '//*[@id="form-field-state"]', state)
        # random_sleep(1)

        # # Business ZIP Code
        # write_delay(driver, '//*[@id="form-field-zipcode"]', zipcode)
        # random_sleep(1)

        # # Mobile Number
        # write_delay(driver, '//*[@id="form-field-biz_number"]', mobileNumber)
        # random_sleep(1)

        # # Website URL
        # write_delay(driver, '//*[@id="form-field-web_url"]', "https://mybusiness.com")
        # random_sleep(1)

        # # Type of Business
        # write_delay(driver, '//*[@id="form-field-biz_type"]', "Retail")
        # random_sleep(1)

        # # Owner Name
        # write_delay(driver, '//*[@id="form-field-owner_name"]', f"{firstName} {lastName}")
        # random_sleep(1)

        # # Ownership Percentage
        # write_delay(driver, '//*[@id="form-field-ownership_percentage"]', "100")
        # random_sleep(1)

        # # Multiple Owners
        # send_click(driver, '//*[@id="form-field-multiple_owner-1"]')  # NO
        # random_sleep(1)

        # # Date of Birth
        # write_delay(driver, '//*[@id="form-field-dob"]', dob)
        # random_sleep(1)

        # # Social Security Number
        # write_delay(driver, '//*[@id="form-field-ssn"]', ssn)
        # random_sleep(1)

        # # Home Address
        # write_delay(driver, '//*[@id="form-field-home_address"]', homeAddress)
        # random_sleep(1)

        # # Home City
        # write_delay(driver, '//*[@id="form-field-home_city"]', city)
        # random_sleep(1)

        # # Home State
        # write_delay(driver, '//*[@id="form-field-home_state"]', state)
        # random_sleep(1)

        # # Home ZIP Code
        # write_delay(driver, '//*[@id="form-field-home_zip"]', zipcode)
        # random_sleep(1)

        # # Do you own multiple businesses?
        # send_click(driver, '//*[@id="form-field-field_60c3a5c-1"]')  # NO
        # random_sleep(1)

        # # Are you working with a Reliant Funding rep?
        # send_click(driver, '//*[@id="form-field-field_d15d1d9-0"]')  # YES
        # random_sleep(1)

        # # Who is your rep?
        # write_delay(driver, '//*[@id="form-field-field_82bb601"]', "John Doe")
        # random_sleep(1)

        # # Acceptance
        # send_click(driver, '//*[@id="form-field-acceptance"]')
        # random_sleep(1)

        # # Agree to Terms
        # send_click(driver, '//*[@id="form-field-field_d023a75"]')
        # random_sleep(1)

        # # Affirmation
        # send_click(driver, '//*[@id="form-field-field_b4203d4"]')
        # random_sleep(1)

        # # Signature
        # write_delay(driver, '//*[@id="form-field-signature"]', f"{firstName} {lastName}")
        # random_sleep(1)

        # # Signed Date
        # write_delay(driver, '//*[@id="form-field-sign_date"]', "01/01/2023")
        # random_sleep(1)

        # # Submit
        # send_click(driver, '//*[@id="funding-submit"]/span/span')
        # random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Reliant Funding"
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
        card_name = "Reliant Funding"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
