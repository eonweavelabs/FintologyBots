from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Arcarius Funding
# -----------------------------------------------------------------

def ArcariusFunding(driver, data, product_id):
    try:
        #data = {
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
        #     }
        # }
        
        driver.get("https://arcariusfunding.com/apply-now.php")
        random_sleep(15)

        personal = data.get("personal")
        business = data.get("business")
        email = data.get("email")

        random_sleep(20)
        
        # Funding
        write_delay(driver, '//*[@id="tab1"]/div[2]/div/input', personal.get("fundingAmount"))
        random_sleep(1)
        send_click(driver, '//*[@id="tab1"]/div[3]/a')
        random_sleep(1)
        
        # Time in Business
        write_delay(driver, '//*[@id="carss"]',personal.get("years"))
        random_sleep(1)
        send_click(driver, '//*[@id="tab2"]/div[3]/a[2]')
        random_sleep(1)
        
        # Finance Purpose
        # send_click(driver, '//*[@id="tab3"]/div[1]/div/div[2]/div/div[10]/label')
        random_sleep(1)
        send_click(driver, '//*[@id="tab3"]/div[2]/a[2]')
        random_sleep(1)
        
        # Average Monthly
        write_delay(driver, '//*[@id="tab4"]/div[2]/div/input', personal.get("monthlyRevenue"))
        random_sleep(1)
        send_click(driver, '//*[@id="tab4"]/div[3]/a[2]')
        random_sleep(1)
        
        # Credit Score
        send_click(driver, '//*[@id="tab5"]/div[2]/label[1]')
        random_sleep(1)
        send_click(driver, '//*[@id="tab5"]/div[3]/a[2]')
        random_sleep(1)
        
        # Industry Type
        # write_delay(driver, '//*[@id="carss"]', business.get("industry"))
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="carss"]')
                select = Select(select_element)
                select.select_by_value(business.get("industry"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        send_click(driver, '//*[@id="tab6"]/div[3]/a[2]')
        random_sleep(1)
        
        # Business Information
        write_delay(driver, '//*[@id="tab7"]/div[2]/input', business.get("legalName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="tab7"]/div[3]/div[1]/input', business.get("phoneNumber"))
        random_sleep(1)
        write_delay(driver, '//*[@id="tab7"]/div[3]/div[2]/input', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="tab7"]/div[3]/div[3]/input', business.get("address"))
        random_sleep(1)
        write_delay(driver, '//*[@id="tab7"]/div[3]/div[4]/input', business.get("city"))
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="cars"]')
                select = Select(select_element)
                select.select_by_value(personal.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        write_delay(driver, '//*[@id="tab7"]/div[3]/div[5]/input', business.get("zipcode"))
        random_sleep(1)
        send_click(driver, '//*[@id="tab7"]/div[4]/a[2]')
        random_sleep(1)
        
        # Business Start year
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="cars"]')
                select = Select(select_element)
                select.select_by_value(business.get('startYear'))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        # Business Start month
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="cars"]')
                select = Select(select_element)
                select.select_by_value(business.get('startMonth'))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        random_sleep(1)
        send_click(driver, '//*[@id="tab8"]/div[3]/p/label[2]')
        random_sleep(1)
        write_delay(driver, '//*[@id="txtnumber"]', business.get("taxId"))
        random_sleep(1)
        send_click(driver, '//*[@id="more-info-cont"]')
        random_sleep(1)
        
        # Personal Information
        write_delay(driver, '//*[@id="name"]', personal.get("firstName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="name"]', personal.get("lastName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="tab9"]/div[3]/div/input', personal.get("homeAddress"))
        random_sleep(1)
        write_delay(driver, '//*[@id="tab9"]/div[4]/div/input', personal.get("city"))
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="cars"]')
                select = Select(select_element)
                select.select_by_value(personal.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        write_delay(driver, '//*[@id="tab9"]/div[5]/div[2]/input', personal.get("zipcode"))
        random_sleep(1)
        write_delay(driver, '//*[@id="name"]', personal.get("mobileNumber"))
        random_sleep(1)
        write_delay(driver, '//*[@id="name"]', personal.get("dob"))
        random_sleep(1)
        write_delay(driver, '//*[@id="soc_sec_num"]', personal.get("ssn"))
        random_sleep(1)
        write_delay(driver, '//*[@id="about-you"]/input', 100)
        random_sleep(1)
        send_click(driver, '//*[@id="about-you-cont"]')
        random_sleep(1)
        
        # Final Steps
        send_click(driver, '//*[@id="accordion01"]/div[5]/label[1]')
        random_sleep(1)
        send_click(driver, '//*[@id="accordion01"]/div[5]/label[2]')
        random_sleep(1)
        send_click(driver, '//*[@id="submit"]')
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Arcarius Funding"
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
        card_name = "Arcarius Funding"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
