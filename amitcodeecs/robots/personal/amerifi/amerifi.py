from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Amerifi
# ------------------------------------------------------

def Amerifi(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "companyName": "CompanyName",
        #         "grossIncome": 876655,
        #         "mobileNumber": 7349303040,
        #     }
        # }
        driver.get("https://www.amerificapital.com/apply-now")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        email = data.get("email")
        companyName = data.get("personal").get("companyName")
        mobileNumber = data.get("personal").get("mobileNumber")
        grossIncome = data.get("personal").get("householdIncome")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="input_comp-kehwqoov"]', firstName)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="input_comp-kehwqopg"]', email)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="input_comp-kehwqopk"]', companyName)
        random_sleep(1)

        # Phone Number
        write_delay(driver, '//*[@id="input_comp-kehwqopm2"]', mobileNumber)
        random_sleep(1)

        # Average monthly gross income
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="collection_comp-kmmluy0x"]'
                )                  
                select = Select(select_element)
                select.select_by_value('$75,000 - $125,000')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # write_delay(driver, '//*[@id="collection_comp-kmmluy0x"]', grossIncome)
        random_sleep(1)

        # Apply
        send_click(driver, '//*[@id="comp-kehwqopx"]/button/span')
        random_sleep(10)

        # Screenshot and upload
        full_name = f"{firstName} {companyName}"
        card_name = "Amerifi"
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
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('companyName')}"
        card_name = "Amerifi"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
