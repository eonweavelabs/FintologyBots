from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Citi Aadvantage Business World Elite Mastercard
# -----------------------------------------------------

def citiAadvantageBusinessWorldEliteMastercard(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "citizenship": "Indiam",
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "membership": 456836297456,
        #         "housingStatus": "Own",
        #         "grossIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "rent": 15000,
        #         "employmentType": "EMPLOYED",
        #         "state": 'AK',
        #         "zipcode": 30201,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #         "nameofbusiness": "My Business Name",
        #         "businessaddress": "456 Business Rd., Suite 100, New York",
        #         "businessphonenumber": 1234567890,
        #         "legalstructureofbusiness": "Corporation",
        #         "typeoffinancialinstitute": "Bank",
        #         "taxIdNumber": "12-3456789",
        #         "lineofbusiness": "Retail",
        #         "numberofemployees": 50,
        #         "yearinbusiness": 10,
        #         "countryofbusinessformation": "USA",
        #         "securitywordhint": "Pet's name",
        #         "securityword": "Fluffy"
        #     }
        # }
        
        
        email = data.get("email")
        personal = data.get("personal")
        citizenship = personal.get("citizenship")
        firstName = personal.get("firstName")
        middleName = personal.get("middleName")
        lastName = personal.get("lastName")
        dob = personal.get("dob")
        ssn = personal.get("ssn")
        membership = personal.get("membership")
        housingStatus = personal.get("housingStatus")
        grossIncome = personal.get("grossIncome")
        mobileNumber = personal.get("mobileNumber")
        rent = personal.get("rent")
        employmentType = personal.get("employmentType")
        state = personal.get("state")
        zipcode = personal.get("zipcode")
        city = personal.get("city")
        homeAddress = personal.get("homeAddress")
        motherMaidenName = personal.get("motherMaidenName")
        nameofbusiness = personal.get("nameofbusiness")
        businessaddress = personal.get("businessaddress")
        businessphonenumber = personal.get("businessphonenumber")
        legalstructureofbusiness = personal.get("legalstructureofbusiness")
        typeoffinancialinstitute = personal.get("typeoffinancialinstitute")
        taxIdNumber = personal.get("taxIdNumber")
        lineofbusiness = personal.get("lineofbusiness")
        numberofemployees = personal.get("numberofemployees")
        yearinbusiness = personal.get("yearinbusiness")
        countryofbusinessformation = personal.get("countryofbusinessformation")
        securitywordhint = personal.get("securitywordhint")
        securityword = personal.get("securityword")

        driver.get(
            "https://online.citi.com/US/ag/cards/application?ID=3006&HKOP=b6dd8eef275e958878cf3eec81bd35824ce6ca43a28ec06c676ffea617b9866d&app=UNSOL"
        )
        # random_sleep(15)

        random_sleep(20)

        # Membership number
        # write_delay(
        #     driver,
        #     '//*[@id="cds-input-1"]',
        #     membership
        # )

        # Name of Business
        write_delay(
            driver,
            '//*[@id="business-name"]',
            nameofbusiness
        )

        # Business Address
        write_delay(
            driver,
            '//*[@id="cds-input-11"]',
            businessaddress
        )
        
        # ZIP Code
        write_delay(
            driver,
            '//*[@id="cds-input-12"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="cds-input-2"]',
            city,
            clear=True
        )
        random_sleep(2)
        
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/app-dynamic-renderer/div/app-div/div/app-div[1]/div/app-row/cds-row/div/app-column/div/cds-column/address-fields/cds-row/div/cds-column[5]/cds-form-field/div[1]/cds-dropdown2')
                random_sleep(0.1)
                send_click(driver, '//*[@id="cds-option2-30"]')
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/app-dynamic-renderer/div/app-div/div/app-div[1]/div/app-row/cds-row/div/app-column/div/cds-column/address-fields/cds-row/div/cds-column[5]/cds-form-field/div[1]/cds-dropdown2'
                )
                # select = Select(select_element)
                # select.select_by_value(state)
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # Business Phone Number
        write_delay(
            driver,
            '//*[@id="cds-input-3"]',
            businessphonenumber
        )
        
        

        # Annual Business Revenue
        write_delay(
            driver,
            '//*[@id="businessrevenue"]',
            grossIncome
        )
        
        random_sleep(1)
        # legal structure of business
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/app-dynamic-renderer/div/app-div/div/app-div[2]/div/app-column/div/cds-column/app-business-financial-information/form/cds-row[1]/div/cds-column[2]/cds-form-field/div[1]/cds-dropdown2')
                random_sleep(0.1)
                send_click(driver, '//*[@id="cds-option2-61"]')
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="state-5AD7DD2499FEC7D4FE40852F66885FF7-button-value"]'
                # )
                # select = Select(select_element)
                # select.select_by_value(state)
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Organization Type
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="organization-type"]')
                random_sleep(0.1)
                send_click(driver, '//*[@id="cds-option2-70"]')
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="state-5AD7DD2499FEC7D4FE40852F66885FF7-button-value"]'
                # )
                # select = Select(select_element)
                # select.select_by_value(state)
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # tax Id Number
        write_delay(
            driver,
            '//*[@id="taxIdNumber"]',
            taxIdNumber
        )
        
        random_sleep(1)
        
        
        # Line of business
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="line-of-business-button-value"]')
                random_sleep(0.1)
                send_click(driver, '//*[@id="cds-option2-74"]')
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="state-5AD7DD2499FEC7D4FE40852F66885FF7-button-value"]'
                # )
                # select = Select(select_element)
                # select.select_by_value(state)
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        
        # Number of employees
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="no-employees-button-value"]')
                random_sleep(0.1)
                send_click(driver, '//*[@id="cds-option2-87"]')
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="state-5AD7DD2499FEC7D4FE40852F66885FF7-button-value"]'
                # )
                # select = Select(select_element)
                # select.select_by_value(state)
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1


        # Years in Business
        write_delay(
            driver,
            '//*[@id="years-in-business"]',
            yearinbusiness
        )
        random_sleep(1)
        
        # Country of Business Formation
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/app-dynamic-renderer/div/app-div/div/app-div[3]/div/app-column/div/cds-column/app-business-other-information/form/cds-row[2]/div/cds-column[2]/cds-form-field/div[1]/cds-dropdown2')
                random_sleep(0.1)
                send_click(driver, '//*[@id="cds-option2-89"]')
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="state-5AD7DD2499FEC7D4FE40852F66885FF7-button-value"]'
                # )
                # select = Select(select_element)
                # select.select_by_value(state)
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        
        
        # First Name
        write_delay(
            driver,
            '//*[@id="cds-input-13"]',
            firstName
        )
        random_sleep(1)

        # Middle name
        # if len(middleName):
        #     write_delay(
        #     driver,
        #     '//*[@id="MIDDLE_NAME"]',
        #     middleName
        #     )
        #     random_sleep(1)
        # else:
        #     print("Middle name not provided. Skipping...")

        # Last name
        write_delay(
            driver,
            '//*[@id="cds-input-15"]',
            lastName
        )
        random_sleep(1)

        # Date of birth
        write_delay(
            driver,
            '//*[@id="cds-input-5"]',
            dob
        )
        random_sleep(1)

        # SSN Number
        write_delay(
            driver,
            '//*[@id="cds-input-4"]',
            ssn
        )

        random_sleep(1)
        
        # Same address as business
        send_click(driver, '//*[@id="cds-checkbox-0-label"]') 
        random_sleep(1)

        # Home address
        # write_delay(
        #     driver,
        #     '//*[@id="cds-input-16"]',
        #     homeAddress
        # )

        random_sleep(1)

        # ZIP Code
        # write_delay(
        #     driver,
        #     '//*[@id="cds-input-17"]',
        #     zipcode
        # )

        random_sleep(1)

        # City
        # write_delay(
        #     driver,
        #     '//*[@id="cds-input-7"]',
        #     city,
        #     clear=True
        # )
        random_sleep(2)
        # retry_count = 0
        # while retry_count < 600:
        #     try:
        #         select_element = driver.find_element(
        #             by=By.XPATH, 
        #             value='//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/app-dynamic-renderer/div/app-div/div/app-div[4]/div/app-column[5]/div/cds-column/app-row[2]/cds-row/div/app-column/div/cds-column/address-fields/cds-row/div/cds-column[5]/cds-form-field/div[1]/cds-dropdown2'
        #         )
        #         select = Select(select_element)
        #         select.select_by_value(state)
        #         break
        #     except:
        #         driver.execute_script("window.scrollBy(0,5)")
        #         random_sleep(0.1)
        #         retry_count += 1

        # random_sleep(1)
        random_sleep(1)
        
        # Email
        write_delay(
            driver, 
            '//*[@id="email"]', 
            email
        )

        random_sleep(1)
        random_sleep(1)
        
        # Phone number
        write_delay(
            driver,
            '//*[@id="cds-input-8"]', 
            mobileNumber
        )

        random_sleep(1)
        
        # Security Word Hint 
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/app-dynamic-renderer/div/app-div/div/app-div[5]/div/app-div/div/app-column/div/cds-column/security-word/cds-row/div/cds-column[3]/cds-form-field/div[1]/cds-dropdown2')
                send_click(driver, '//*[@id="cds-option2-405"]')
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="securityWordHint"]'
                # )
                # select = Select(select_element)
                # select.select_by_value('T')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        
        # Mother name
        write_delay(
            driver, 
            '//*[@id="securityWord"]',
            motherMaidenName
        )
        
        # Gross annual income
        write_delay(
            driver, 
            '//*[@id="cds-input-9"]',
            grossIncome
        )
        random_sleep(1)
        write_delay(
            driver, 
            '//*[@id="beneficial-owner-information"]',
            100
        )

        random_sleep(1)
        send_click(driver, '//*[@id="percentageRadioNORadioBtn-label"]')
        random_sleep(1)

        random_sleep(1)

        # Second Checkbox
        try:
            send_click(driver, '//*[@id="cds-checkbox-10-label"]')
        except:
            driver.save_screenshot(
            f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Citi Aadvantage Business World Elite Mastercard.png"
            )
        random_sleep(1)
        
        # Submit button
        send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application2/cds-row/div/cds-column/div/aa-business-card-application/form/cds-column/div/button')
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
        card_name = "Citi Aadvantage Business World Elite Mastercard"
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
        card_name = "Citi Aadvantage Business World Elite Mastercard"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
