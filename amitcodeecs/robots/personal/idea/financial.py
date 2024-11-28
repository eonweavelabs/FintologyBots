from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Idea Financial
# -----------------------------------------------------------------

def ideaFinancial(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Krishan Pratap",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "mobileNumber": 7349303040,
        #         "homeAddress": "1600 Pennsylvania Avenue NW",
        #         "state": 'DC',
        #         "zipcode": 20500,
        #         "city": "Washington",
        #     },
        #     "business": {
        #         "legalName": "Test Business LLC",
        #         "address": "1600 Pennsylvania Avenue NW",
        #         "zipcode": 20500,
        #         "city": "Washington",
        #         "state": 'DC',
        #         "phoneNumber": 7349303042,
        #         "taxId": "12-3456789",
        #         "industry": "Retail",
        #         "annualRevenue": 1000000,
        #         "monthlySpend": 50000,
        #         "startYear": "2020",
        #         "startMonth": "01",
        #         "ownershipPercentage": 100
        #     }
        # }
        
        driver.get("https://www.ideafinancial.com/application")
        random_sleep(15)

        personal = data.get("personal")
        business = data.get("business")
        email = data.get("email")


        random_sleep(20)
        
        # Personal Information
        write_delay(driver, '//*[@id="FirstName"]', personal.get("firstName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="LastName"]', personal.get("lastName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="Company"]', business.get("legalName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="Email"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="Phone"]', business.get("phoneNumber"))
        random_sleep(1)
        send_click(driver, '//*[@id="appForm1"]/div[22]/label')
        random_sleep(1)
        send_click(driver, '//*[@id="getStarted"]')
        random_sleep(1)
        
        # Age of your business
        send_click(driver, '//*[@id="appForm2"]/div[3]/div/label[3]/div[1]')  # Assuming "two years or more"
        random_sleep(1)
        
        # Entity Type
        send_click(driver, '//*[@id="appForm2"]/div[5]/div/label[1]/div[1]')  # Assuming "Limited liability company"
        random_sleep(1)
        
        # Average Monthly Sales
        write_delay(driver, '//*[@id="average_monthly_sales"]', business.get("monthlySpend"))
        random_sleep(1)
        write_delay(driver, '//*[@id="tax_id"]', business.get("taxId"))
        random_sleep(1)
        send_click(driver, '//*[@id="showStep3"]')
        random_sleep(1)
        
        # Business Address
        write_delay(driver, '//*[@id="autocomplete1"]', business.get("address"))
        random_sleep(1)
        write_delay(driver, '//*[@id="Business_Address_Unit__c"]', "")
        random_sleep(1)
        write_delay(driver, '//*[@id="city1"]', business.get("city"))
        random_sleep(1)
        write_delay(driver, '//*[@id="state1"]', business.get("state"))
        random_sleep(1)
        write_delay(driver, '//*[@id="zipCode1"]', business.get("zipcode"))
        random_sleep(1)
        send_click(driver, '//*[@id="showStep4"]')
        random_sleep(1)
        
        # Additional Contact Info
        write_delay(driver, '//*[@id="SSN__c"]', personal.get("ssn"))
        random_sleep(1)
        write_delay(driver, '//*[@id="MobilePhone"]', personal.get("mobileNumber"))
        random_sleep(1)
        
        # Select month
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="month_1"]'
                )
                select = Select(select_element)
                select.select_by_value( personal.get("dob").split('/')[0])
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Select days
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="day_1"]'
                )
                select = Select(select_element)
                select.select_by_value( personal.get("dob").split('/')[1])
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Select Year
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="year_1"]'
                )
                select = Select(select_element)
                select.select_by_value( personal.get("dob").split('/')[2])
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        send_click(driver, '//*[@id="appForm4"]/div[8]/div/label[6]')
        random_sleep(1)

        
        # Home Address
        write_delay(driver, '//*[@id="autocomplete2"]', personal.get("homeAddress"))
        random_sleep(1)
        write_delay(driver, '//*[@id="Address_Unit_1__c"]', "")
        random_sleep(1)
        write_delay(driver, '//*[@id="city2"]', personal.get("city"))
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="state2"]'
                )
                select = Select(select_element)
                select.select_by_value(personal.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="zipCode2"]', personal.get("zipcode"))
        random_sleep(1)
        send_click(driver, '//*[@id="showStep5"]')
        random_sleep(1)
        
        # Ownership Percentage
        write_delay(driver, '//*[@id="Ownership_Pct__c"]', 100)
        random_sleep(1)
        send_click(driver, '//*[@id="showStepLast"]')
        random_sleep(1)
        
        # Link Your Bank
        # send_click(driver, '//*[@id="bank-link-btn"]')
        # random_sleep(1)
        
        # Upload Documents
        # driver.find_element(by=By.XPATH, value='//*[@id="appFormLast"]/div[5]/div[1]/input').send_keys("path/to/file1")
        # random_sleep(1)
        # driver.find_element(by=By.XPATH, value='//*[@id="appFormLast"]/div[5]/div[2]/input').send_keys("path/to/file2")
        # random_sleep(1)
        # driver.find_element(by=By.XPATH, value='//*[@id="appFormLast"]/div[5]/div[3]/input').send_keys("path/to/file3")
        # random_sleep(1)
        send_click(driver, '//*[@id="submitApp"]')
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Idea Financial"
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
        full_name = data.get("personal").get("firstName") + " " + data.get("personal").get("lastName")
        card_name = "Idea Financial"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
