from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Scale Funding
# ------------------------------------------------------

def scaleFunding(driver, data, product_id):
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
        #         "companyName": "My Company",
        #         "businessType": "LLC",
        #         "monthlySales": 50000
        #     }
        # }
        driver.get("https://getscalefunding.com/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        companyName = data.get("personal").get("companyName")
        businessType = data.get("personal").get("businessType")
        monthlySales = data.get("personal").get("monthlySales")

        random_sleep(20)
        
        send_click(driver, '//*[@id="fl-button-group-button-o63t2zjmiyv9-0"]/div/a')

        # First Name
        write_delay(driver, '//*[@id="input_65_4"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="input_65_6"]', lastName)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="input_65_7"]', email)
        random_sleep(1)

        # Phone number
        write_delay(driver, '//*[@id="input_65_8"]', mobileNumber)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="input_65_9"]', companyName)
        random_sleep(1)

        # Business Type
        write_delay(driver, '//*[@id="input_65_10"]', businessType)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="input_65_10"]'
                )
                select = Select(select_element)
                select.select_by_value('Other')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)


        # Monthly Sales
        write_delay(driver, '//*[@id="input_65_12"]', monthlySales)
        random_sleep(1)

        # I'm Not a Robot
        send_click(driver, '//*[@id="recaptcha-anchor"]')
        random_sleep(1)

        # Get Funded
        send_click(driver, '//*[@id="gform_submit_button_65"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Scale Funding"
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
        card_name = "Scale Funding"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
