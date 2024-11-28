from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
from Utils.send_click2 import send_click2
import traceback


# ------------------------------------------------------
# Torro
# ------------------------------------------------------

def torro(driver, data, product_id):
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
        #         "businessName": "My Business",
        #         "businessPhone": 1234567890,
        #         "industryType": "Retail",
        #         "timeInBusiness": "2 years",
        #         "personalCreditScore": 700,
        #         "password": "securepassword123"
        #     }
        # }
        driver.get("https://www.gotorro.com/asv1/secure/index.php")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        grossIncome = data.get("personal").get("householdIncome")
        businessName = data.get("personal").get("businessName")
        businessPhone = data.get("personal").get("businessPhone")
        industryType = data.get("personal").get("industryType")
        timeInBusiness = data.get("personal").get("timeInBusiness")
        personalCreditScore = data.get("personal").get("personalCreditScore")
        password = data.get("personal").get("password")

        random_sleep(20)

        # Business I want to start
        send_click(driver, '//*[@id="submitloan"]/div/div[1]/div[3]/div[2]/div[1]/div/div/div/label')
        random_sleep(1)

        # Name Of Business
        write_delay(driver, '//*[@id="businessname"]', businessName)
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="zipcode"]', zipcode)
        random_sleep(1)

        # Industry Type
        write_delay(driver, '//*[@id="businesstype"]', industryType)
        random_sleep(1)

        # Time in Business
        write_delay(driver, '//*[@id="beeninbusiness"]', timeInBusiness)
        random_sleep(1)

        # First Name
        write_delay(driver, '//*[@id="firstname"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastname"]', lastName)
        random_sleep(1)

        # Business Phone
        write_delay(driver, '//*[@id="businessphone"]', businessPhone)
        random_sleep(1)

        # Mobile Phone
        write_delay(driver, '//*[@id="mobilephone"]', mobileNumber)
        random_sleep(1)

        # Monthly Sales Volume
        write_delay(driver, '//*[@id="monthlyincome"]', grossIncome)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="submitloan"]/div/div[1]/div[3]/div[7]/div[1]/div[2]'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="MWFCNCGB"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="monthlyincome"]'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, state)

                select = Select(select_element)
                select.select_by_value('$500,000+')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # Personal Credit Score
        write_delay(driver, '//*[@id="credit"]', personalCreditScore)
        random_sleep(1)

        # Email Address
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)

        # Create Password
        write_delay(driver, '//*[@id="client_password"]', password)
        random_sleep(1)

        # Email my Torro login information.
        send_click2(driver, '//*[@id="submitloan"]/div/div[1]/div[5]/div')
        random_sleep(1)

        # By Submitting this form, you agree to receive occasional emails and reoccurring automated text messages from Torro, LLC regarding your application.
        send_click(driver, '//*[@id="submitloan"]/div/div[1]/div[5]/div')
        random_sleep(1)

        # GET FUNDING OPTIONS
        send_click(driver, '//*[@id="submitloan"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Torro"
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
        card_name = "Torro"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
