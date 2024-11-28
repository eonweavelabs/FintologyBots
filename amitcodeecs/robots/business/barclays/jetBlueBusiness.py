from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ----------------------------------------------
# Barclays Jet Blue Business
# ----------------------------------------------

def barclaysJetBlueBusiness(driver, data, product_id):
    
    try:
        driver.get("https://cards.barclaycardus.com/credit-card/08c20534-3ecc-4a6b-a569-857a4b6a05f9?referrerid=BCSCD&xsessionid=333F2ADD0AFAD3A08F2C7BBDCF633BA9")
        random_sleep(15)
        
        # data = {
        #     "personal": {
        #         "mobileNumber": "1234567890",
        #         "firstName": "John",
        #         "lastName": "Doe",
        #         "dob": "01/01/1980",
        #         "ssn": "123-45-6789",
        #         "homeAddress": "123 Main St",
        #         "zipcode": "12345",
        #         "city": "Anytown",
        #         "state": "NY",
        #         "grossIncome": "50000"
        #     },
        #     "business": {
        #         "legalName": "John's Business",
        #         "legalStructure": "LLC",
        #         "ageRange": "5",
        #         "numberOfEmployees": "10",
        #         "annualRevenue": "100000",
        #         "phoneNumber": "0987654321",
        #         "address": "456 Business Rd",
        #         "city": "Businesstown",
        #         "state": "NY",
        #         "zipcode": "54321",
        #         "industry": "Retail",
        #         "businessSubcategory": "Clothing",
        #         "role": "Owner",
        #         "ownershipPercentage": "100"
        #     },
        #     "email": "bhawani@bhawani.com",
        # }

        personal = data.get("personal")
        business = data.get("business")
        email = data.get("email")

        random_sleep(20)
        
        # Business Legal Name
        write_delay(driver, '//*[@id="legalBusinessName"]', business.get("legalName"))
        random_sleep(1)
        
        # Business Legal Entity Type
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="legalEntityType"]')
                select = Select(select_element)
                select.select_by_value("SOLE_PROPRIETOR")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Years in Business
        write_delay(driver, '//*[@id="yearsInBusiness"]', business.get("ageRange"))
        random_sleep(1)
        
        # Number of Employees
        write_delay(driver, '//*[@id="numberOfEmployees"]', business.get("numberOfEmployees"))
        random_sleep(1)
        
        # Annual Business Revenue
        write_delay(driver, '//*[@id="annualBusinessRevenue"]', business.get("annualRevenue"))
        random_sleep(1)
        
        # Business Phone Number
        write_delay(driver, '//*[@id="businessPhoneNumber"]', business.get("phoneNumber"))
        random_sleep(1)
        
        # Business Address
        write_delay(driver, '//*[@id="businessAddressLine1"]', business.get("address"))
        random_sleep(1)
        
        # Business City
        write_delay(driver, '//*[@id="businessCity"]', business.get("city"), clear=True)
        random_sleep(1)
        
        # Business State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="businessState"]')
                select = Select(select_element)
                select.select_by_value(business.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Business ZIP Code
        write_delay(driver, '//*[@id="businessZip"]', business.get("zipcode"))
        random_sleep(1)
        
        # Nature of Business
        # write_delay(driver, '//*[@id="natureOfBusiness"]', business.get("industry"))
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="natureOfBusiness"]')
                select = Select(select_element)
                select.select_by_value("17")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Nature of Business Subcategory
        # write_delay(driver, '//*[@id="natureOfBusinessSubcategory"]', business.get("businessSubcategory"))
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="natureOfBusinessSubcategory"]')
                select = Select(select_element)
                select.select_by_value("453998")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # ?
        send_click(driver, '//*[@id="countryCheck-N"]')
        random_sleep(1)
        
        
        # Email Address
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)
        
        # Primary Phone Number
        write_delay(driver, '//*[@id="primaryPhone"]', personal.get("mobileNumber"))
        random_sleep(1)
        
        # Legal First Name
        write_delay(driver, '//*[@id="firstName"]', personal.get("firstName"))
        random_sleep(1)
        
        # Legal Last Name
        write_delay(driver, '//*[@id="lastName"]', personal.get("lastName"))
        random_sleep(1)
        
        # DOB
        write_delay(driver, '//*[@id="dateOfBirth"]', personal.get("dob"))
        random_sleep(1)
        
        # SSN or Individual tax id
        write_delay(driver, '//*[@id="socialSecurityNumber"]', personal.get("ssn"))
        random_sleep(1)
        
        # Residential Address
        # write_delay(driver, '//*[@id="address.residential.addressLine1"]', personal.get("homeAddress"))
        # random_sleep(1)
        
        # ZIP Code
        # write_delay(driver, '//*[@id="address.residential.zipcode"]', personal.get("zipcode"))
        # random_sleep(1)
        
        # City
        # write_delay(driver, '//*[@id="address.residential.city"]', personal.get("city"), clear=True)
        # random_sleep(1)
        
        # State
        # random_sleep(2)
        # retry_count = 0
        # while retry_count < 600:
        #     try:
        #         select_element = driver.find_element(by=By.XPATH, value='//*[@id="address.residential.state"]')
        #         select = Select(select_element)
        #         select.select_by_value(personal.get("state"))
        #         break
        #     except:
        #         driver.execute_script("window.scrollBy(0,5)")
        #         random_sleep(0.1)
        #         retry_count += 1
        # random_sleep(1)
        
        # Total Annual Income
        write_delay(driver, '//*[@id="grossIncome"]', personal.get("grossIncome"))
        random_sleep(1)
        
       
        
        # Is your business headquartered in the U.S.?
        # send_click(driver, '//*[@id="countryCheck-N"]')
        # random_sleep(1)
        
        # Position in Business
        write_delay(driver, '//*[@id="positionInBusiness"]', business.get("role"))
        random_sleep(1)
        
        # Percentage of Ownership
        # write_delay(driver, '//*[@id="percentageOfOwnership"]', business.get("ownershipPercentage"))
        # random_sleep(1)
        
        # Are you a United States citizen?
        send_click(driver, '//*[@id="unitedStateCitizen-T"]')
        random_sleep(1)
        
        # Resident Status
        send_click(driver, '//*[@id="residentStatus-O"]')
        random_sleep(1)
        
        # Checkbox for electronic delivery
        send_click(driver, '//*[@id="electronicDelivery-container"]/label')
        random_sleep(1)
        
        # Submit Application
        send_click(driver, '//*[@id="applyNow"]')
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Barclays Jet Blue Business"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
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
        full_name = data.get("personal").get("firstName") + " " + data.get("personal").get("lastName")
        card_name = "Barclays Jet Blue Business"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
