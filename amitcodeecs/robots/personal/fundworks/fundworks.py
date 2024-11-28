from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Fundworks
# ------------------------------------------------------

def Fundworks(driver, data, product_id):
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
        driver.get("https://thefundworks.com/application/")
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
        mobileNumber = data.get("personal").get("mobileNumber")
        grossIncome = data.get("personal").get("householdIncome")
        business = data.get("business")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="nf-field-38"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="nf-field-39"]', lastName)
        random_sleep(1)

        # DOB
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                random_sleep(1)
                write_delay(driver, '//*[@id="nf-field-62-wrap"]/div[2]/div/input[2]', dob)
                random_sleep(1)
                send_click(driver, '/html/body/div[2]/div[2]/div/div[2]/div/span[11]')
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-62"]'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, dob)
                   
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        

        # SSN
        write_delay(driver, '//*[@id="nf-field-61"]', ssn)
        random_sleep(1)

        # Address
        write_delay(driver, '//*[@id="nf-field-43"]', homeAddress)
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="nf-field-45"]', city)
        random_sleep(1)

        # US States
        # write_delay(driver, '//*[@id="nf-field-46"]', state)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-46"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                   
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="nf-field-47"]', zipcode)
        random_sleep(1)

        # Phone
        write_delay(driver, '//*[@id="nf-field-42"]', mobileNumber)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="nf-field-41"]', email)
        random_sleep(1)

        # Percent Owned
        write_delay(driver, '//*[@id="nf-field-63"]', "100")
        random_sleep(1)

        # How many other owners?
        write_delay(driver, '//*[@id="nf-field-64"]', "0")
        random_sleep(1)

        # Business Legal Name
        write_delay(driver, '//*[@id="nf-field-48"]',business.get('name'))
        random_sleep(1)

        # DBA
        write_delay(driver, '//*[@id="nf-field-49"]', business.get('DBA'))
        random_sleep(1)

        # EIN
        write_delay(driver, '//*[@id="nf-field-50"]', business.get('EIN'))
        random_sleep(1)

        # Legal Entities
        write_delay(driver, '//*[@id="nf-field-66"]', "LLC")
        random_sleep(1)

        # Business Start Date
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-80-wrap"]/div[2]/div/input[2]'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, business.get('date'))
                   
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # write_delay(driver, '//*[@id="nf-field-80-wrap"]/div[2]/div/input[2]', "01/01/2010")
        # random_sleep(1)

        # Industry
        # write_delay(driver, '//*[@id="nf-field-105"]', "Industry")
        random_sleep(1)

        # Business Address
        write_delay(driver, '//*[@id="nf-field-53"]', business.get('address'))
        random_sleep(1)

        # Business City
        write_delay(driver, '//*[@id="nf-field-55"]', business.get('City'))
        random_sleep(1)

        # Business US States
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-56"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                   
                select = Select(select_element)
                select.select_by_value(business.get('state'))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Business ZIP
        write_delay(driver, '//*[@id="nf-field-57"]', business.get('zip'))
        random_sleep(1)

        # Business Phone
        write_delay(driver, '//*[@id="nf-field-58"]', business.get('phone'))
        random_sleep(1)

        # Business Email
        write_delay(driver, '//*[@id="nf-field-67"]', business.get('email'))
        random_sleep(1)

        # Is the business seasonal
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-51"]'
                )                   
                select = Select(select_element)
                select.select_by_value('no')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Description of Business
        write_delay(driver, '//*[@id="nf-field-52"]', business.get('description'))
        random_sleep(1)

        # Gross Annual Sales
        write_delay(driver, '//*[@id="nf-field-69"]', grossIncome)
        random_sleep(1)

        # Recent Month Business Deposits
        write_delay(driver, '//*[@id="nf-field-71"]', business.get('recentMonthDeposits'))
        random_sleep(1)

        # Do you have a current loan or business advance?
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-70"]'
                )                   
                select = Select(select_element)
                select.select_by_value('no')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # Current Balance
        write_delay(driver, '//*[@id="nf-field-72"]', business.get('balance'))
        random_sleep(1)

        # Pmt. Amount
        write_delay(driver, '//*[@id="nf-field-73"]', business.get('"pmtAmount"'))
        random_sleep(1)

        # Pmt Frequency
        write_delay(driver, '//*[@id="nf-field-74"]', business.get("pmtFrequency"))
        random_sleep(1)

        # Months Remaining
        write_delay(driver, '//*[@id="nf-field-75"]', business.get('remaining'))
        random_sleep(1)

        # Any Pending Litigation? Claims? Judgements?
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-76"]'
                )                   
                select = Select(select_element)
                select.select_by_value('no')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # Are you contemplating Bankruptcy, Reorganization, or Sale of the Business?
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="nf-field-77"]'
                )                   
                select = Select(select_element)
                select.select_by_value('no')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # Disclaimer
        send_click(driver, '//*[@id="nf-field-132-wrap"]/div[2]/form/div/label')
        random_sleep(1)
        send_click(driver, '//*[@id="nf-field-133-wrap"]/div[2]/form/div/label')
        random_sleep(1)

        # SUBMIT
        send_click(driver, '//*[@id="nf-field-40"]')
        random_sleep(1)

        # Sign Here
        send_click(driver, '//*[@id="signatureCanvas2"]')
        random_sleep(1)

        # Insert Signature
        send_click(driver, '//*[@id="tabs-1"]/div/button')
        random_sleep(1)

        # Agree & Sign
        send_click(driver, '//*[@id="esig-agreed"]')
        random_sleep(1)

        # Select Files
        # send_click(driver, '//*[@id="nf-field-88-wrap"]/div[2]/button[1]')
        # random_sleep(1)

        # SUBMIT
        send_click(driver, '//*[@id="nf-field-89"]')
        random_sleep(15)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Fundworks"
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
        card_name = "Fundworks"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
